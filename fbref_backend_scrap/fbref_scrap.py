from bs4 import BeautifulSoup as soup
import requests
import time



from main import signal_handler
from pyspark.sql.types import StructType

import pandas as pd
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col, to_date


from constants import required_football_match_columns, football_match_league_columns, football_match_cup_columns
from fbref_get_general_match_data import get_general_match_data
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_match_id_by_teams_and_tournament, get_match_of_tournaments
from spark_schema import get_football_match_schema, get_match_stats_gen_schema
from spark_configuration import create_spark_session
from fbref_functions_stats_introduce import get_all_data_of_player
from write_dataframe_to_mysql_file import write_dataframe_to_mysql
from clean_dataframe_file import clean_dataframe
from fbref_delete_football_match import delete_football_match
from fbref_get_teams_of_each_comp import get_teams_of_competition



# Variable global para almacenar el último partido insertado
last_match_id = -1



##############################################################################
# recoge los links de los partidos de la liga
#
# url: url de todos los partidos de una liga y temporada
# league: nombre de la liga
#
##############################################################################
def get_match_links(url, league): 
  
    print('Getting player data links...')
    # access and download content from url containing all fixture links    
    match_links = []
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        links = soup(html.content, "html.parser").find_all('a')
        # filter list to return only needed links
        key_words_good = ['/en/matches/', f'{league}']
        for l in links:
            href = l.get('href', '')
            if all(x in href for x in key_words_good):
                if 'https://fbref.com' + href not in match_links:                 
                    match_links.append('https://fbref.com' + href)
    except Exception as e:
        print(f"Error al obtener los links de los partidos: {e}")
        match_links = []
        return match_links
    print('Player data links collected...')
    return match_links








        
##############################################################################
# recoge los datos de los partidos de la liga
#
# url: url de todos los partidos de una liga y temporada
# league: nombre de la liga
# season: temporada
# type_of_competition: tipo de competicion --> league o cup
#
##############################################################################
def get_fixture_data(url, league, league_id, season, season_id, type_of_competition, spark, jdbc_url, db_properties):
    
    global last_match_id
    returning_value = pd.DataFrame()
    match_not_inserted = []
    try:
        print('Getting fixture data...')

        tables = pd.read_html(url)
        type_of_competition = 'league'

        if type_of_competition == 'league':
            fixtures = tables[0][football_match_league_columns]
        elif type_of_competition == 'cup':
            fixtures = tables[0][football_match_cup_columns]
            fixtures.loc[:, 'Round'] = fixtures['Round'].astype(str)
            fixtures.rename(columns={'Round': 'Wk'}, inplace=True)

        fixtures = fixtures.copy()
        fixtures['Season'] = url.split('/')[6]

        fixtures = fixtures.dropna(subset=['Home', 'Away'])

        clean_dataframe(fixtures)

        match_links = get_match_links(url, league)
        if not match_links:
            print('No existen links de partidos para la liga')
            returning_value = pd.DataFrame()
        
        else:
                
            if len(match_links) != len(fixtures):
                match_links = match_links[:len(fixtures)]
                fixtures = fixtures[:len(match_links)]
                
            fixtures = get_only_new_match_filter(fixtures, match_links, league_id, spark, jdbc_url, db_properties)
            if fixtures.empty:
                print('No se han encontrado partidos nuevos')
                returning_value = pd.DataFrame({"Mensaje": ["No se han encontrado partidos nuevos"]})
        
            else:
                
                max_fails_allowed = 15
                fails = 0
                #Se hace un bucle para asociar a cada partido el link del report de este, ya que este link hay mas informacion de los jugadores
                for index, row in fixtures.iterrows(): 
                    print(f"Procesando partido {row['Home']} vs {row['Away']}")

                    local = row['Home']
                    visitor = row['Away']

                    match_id = add_info_general_match_to_database(row, league_id, spark, jdbc_url, db_properties)
                    if match_id < 0:
                        if match_id == -1:
                            print(f"Error al añadir el partido {local} vs {visitor} a la base de datos")
                        elif match_id == -2:
                            print(f"Error: Faltan columnas obligatorias en el partido {local} vs {visitor}")
                        elif match_id == -3:
                            print(f"El partido {local} vs {visitor} ya existe en la base de datos")
                            
                        match_not_inserted.append((local, visitor, row['match_link'], row['Wk']))
                        if fails >= max_fails_allowed:
                            print("Se ha alcanzado el máximo de errores permitidos, compruebe los errores")
                            
                            for match in match_not_inserted:
                                print(match)
                                print("") 
                            return pd.DataFrame(), match_not_inserted
                        else:
                            fails += 1
                            continue
                    else:
                        last_match_id = match_id

                    #if local in link_element and visitor in link_element:
                    if player_data(league, league_id, season, season_id, match_id, row['match_link'], local, visitor, spark, jdbc_url, db_properties).empty:
                        print(f"Error al obtener los datos de los jugadores del partido {local} vs {visitor}")
                        match_not_inserted.append((local, visitor, row['match_link'], row['Wk']))
                        delete_football_match(spark, jdbc_url, db_properties, match_id)
                        
                        if fails >= max_fails_allowed:
                            print("Se ha alcanzado el máximo de errores permitidos, compruebe los errores")
                            
                            for match in match_not_inserted:
                                print(match)
                                print("")
                            returning_value = pd.DataFrame()
                        else:
                            fails += 1
                            continue
                    else:
                        print('Fixture data collected...')
                        returning_value = pd.DataFrame({"Mensaje": ["No se han encontrado partidos nuevos"]})
                        last_match_id = -1

    except KeyboardInterrupt:
        signal_handler(None, None)

    except Exception as e:
        print(f"Error al obtener los datos de los partidos: {e}")
        returning_value = pd.DataFrame()

    return returning_value, match_not_inserted



            
def get_only_new_match_filter(df_partidos, match_links, league_id, spark, jdbc_url, db_properties):
    # Obtener el máximo de jornada almacenada en la BD
    print("Obteniendo los partidos que no están en la base de datos de la temporada: ", league_id)
    success = pd.DataFrame()
    try:

        # Agregar la columna match_links a df_partidos antes de hacer el merge
        df_partidos["match_link"] = match_links

        team_df = spark.read.jdbc(
            url=jdbc_url, 
            table="team", 
            properties=db_properties
        ).select("team_id", "team_name").filter(f"tournament_team_id = {league_id}").toPandas()

        team_dict = dict(zip(team_df["team_name"], team_df["team_id"]))

        df_partidos["Home"] = df_partidos["Home"].map(team_dict)
        df_partidos["Away"] = df_partidos["Away"].map(team_dict)

        print("Partidos después de mapear los equipos:")
        print(df_partidos)
        
        # Eliminar partidos donde no se haya encontrado el ID
        df_partidos = df_partidos.dropna(subset=["Home", "Away"])

        stored_matches_df = spark.read.jdbc(
            url=jdbc_url, 
            table="football_match", 
            properties=db_properties
        ).select("Home", "Away").filter(f"season = {league_id}").toPandas()

    
        if stored_matches_df.empty:
            print("Se van a añadir todos los partidos, ya que no hay registros previos.")
            success = df_partidos
        else:
            # Unir por Home y Away para encontrar partidos ya existentes
            df_filtered = df_partidos.merge(stored_matches_df, on=['Home', 'Away'], how='left', indicator=True)

            # Filtrar solo los partidos que no están en la base de datos
            df_nuevos_partidos = df_filtered[df_filtered['_merge'] == 'left_only'].drop(columns=['_merge'])
            success = df_nuevos_partidos
            print(f"Se han encontrado {len(df_nuevos_partidos)} partidos nuevos para añadir.")

    except Exception as e:
        print(f"Error al filtrar los partidos nuevos: {e}")
        success = pd.DataFrame()

    return success



######################################################################################
# Insertar la informacion básica del partido en la base de datos partido
# 
# connection:     Conexión con la base de datos
# row:            Información del partido
# league:         Nombre de la liga
#
######################################################################################
def add_info_general_match_to_database(row, league_id, spark, jdbc_url, db_properties):
    print("Inserting football_match_info")
    
    returning_value = -1
    
    try:
        
        for column in required_football_match_columns:
            if pd.isna(row[column]) or row[column] is None:
                returning_value = -2
                break
        
        if returning_value != -2:    
        
            # Rellenar valores por defecto en columnas no críticas
            if pd.isna(row.get('Attendance')) or row['Attendance'] is None:
                row['Attendance'] = 0
            else:
                row['Attendance'] = int(row['Attendance'])

            for optional_col in ['Venue', 'Referee']:
                if pd.isna(row.get(optional_col)) or row[optional_col] is None:
                    row[optional_col] = ""
            
            local_team_id = row['Home']
            visitor_team_id = row['Away']
            row['Season'] = league_id

            existing_match = get_match_id_by_teams_and_tournament(local_team_id, visitor_team_id, league_id, spark, jdbc_url, db_properties)
            if existing_match > 0:
                print(" Match already exists")
                returning_value = -3

            else:
                row['Date'] = pd.to_datetime(row['Date'], errors='coerce')
                row['Date'] = row['Date'].date()

                schema = get_football_match_schema()
                row_dict = row.to_dict()

                match_df = spark.createDataFrame([row_dict], schema)

                spark_df = match_df.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd")) \
                                    .withColumn("Attendance", col("Attendance").cast(IntegerType()))

                print("DataFrame creado")
                print(spark_df.show())
                
                write_dataframe_to_mysql(spark_df, jdbc_url, db_properties, "football_match")
                match = get_match_id_by_teams_and_tournament(local_team_id, visitor_team_id, league_id, spark, jdbc_url, db_properties)
                
                print("Match inserted")
                returning_value = match

    except Exception as e:
        print(f"Error al insertar la información general del del partido, {row['Home']} vs {row['Away']}: {e}")
        return -1
    
    return returning_value

    







######################################################################################
# Insertar un registro en la base de datos de las estadísticas generales del partido totales del equipo local y visitante
#
# df:           Dataframe con las estadísticas generales del partido
# connection:   Conexión con la base de datos
# match_id:     ID del partido al que pertenecen las estadísticas
#
######################################################################################   
def insert_dataframe_general_match_stats_into_database(df_final, match_id, spark, jdbc_url, db_properties):

    returning_value = spark.createDataFrame([], StructType([]))

    
    try:
        print("Inserting general match stats")

        df_final['match_id'] = match_id
        """for column in df_final.columns:
            print(f"Column: {column}, Type: {df_final[column].dtype}")"""
        
        match_stats_schema = get_match_stats_gen_schema()
        df_spark = spark.createDataFrame(df_final, match_stats_schema)

        write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "estadisticas_partido_gen")
        returning_value = df_spark
        
    except Exception as e:
        print(f"Error al insertar los datos en la base de datos: {e}")
        returning_value = spark.createDataFrame([], StructType([]))

    return returning_value




##############################################################################
# inserta los datos de los jugadores en la base de datos, a partir de aqui se inserta los datos basicos, asistencia y goles, y a partir de esta función se llama a la funcion para insertar el resto de estadisticas
#
# league: nombre de la liga
# season: temporada
# match_id: id del partido
# link_element: link del partido
# local: nombre del equipo local
# visitor: nombre del equipo visitante
#
# return: False si hay un error, True si no hay error
#
##############################################################################
def player_data(league, league_id, season, season_id, match_id, link_element, local, visitor, spark, jdbc_url, db_properties):

    player_data = pd.DataFrame([])
    df_final = pd.DataFrame([])

    try:
        dataframe_pct, dataframe_general_data = get_general_match_data(link_element)
        if dataframe_pct.empty or dataframe_general_data.empty:
            print(f"Error al obtener los datos generales del partido {local} vs {visitor}")
            return pd.DataFrame()

        df_combined = pd.concat([dataframe_pct, dataframe_general_data], ignore_index=True)

        df_pivot = df_combined.pivot_table(index=None, columns='Statistic', values=['local', 'visitor'])
        df_final = pd.DataFrame()

        for stat in df_pivot.columns:
            for team in df_pivot.index:
                stat1 = stat.lower()
                column_name = f"{team}_{stat1.replace(' ', '_')}"
                value = df_pivot.at[team, stat]  # Usa .at para acceder directamente a los valores

                if column_name not in df_final.columns:
                    df_final[column_name] = [value]  # Almacenamos el valor en una lista

        df_final.reset_index(drop=True, inplace=True)
        
        if insert_dataframe_general_match_stats_into_database(df_final, match_id, spark, jdbc_url, db_properties).isEmpty():
            print(f"Error al insertar los datos de los jugadores del partido {local} vs {visitor}")
            return pd.DataFrame()

        player_data = pd.read_html(link_element)

        result = get_all_data_of_player(match_id, league, league_id, season, season_id, local, visitor, player_data, spark, jdbc_url, db_properties)
        if result is None or result.isEmpty():
            print(f"Error al obtener los datos de los jugadores del partido {local} vs {visitor}")
            return pd.DataFrame()
        

    except Exception as e:
        print(f'{link_element}: error {e}')
        return pd.DataFrame()
    # sleep for 3 seconds after every game to avoid IP being blocked
    time.sleep(3)
    return pd.DataFrame({"Mensaje": ["Datos de los jugadores procesados correctamente."]})




# Function to get the leagues from the database
def get_5_leagues(spark, jdbc_url, db_properties):
    
    try:

        spark_data = get_match_of_tournaments(spark, jdbc_url, db_properties)
        
        league_df = spark_data.filter(col('nombre_liga') == "La Liga")
        print(league_df.show())

        for row in league_df.collect():
            
            season_id = row["season_tournament_id"]
            season_year = row["season_year"]
            tournament_id = row["tournament_id"]
            tournament_name = row["nombre_liga"]
            tournament_name = tournament_name.replace(' ', '-')
            tournament_fbref_id = row["tournament_fbref_id"]
            type_of_competition = row["type_of_competition"]

            url = f'https://fbref.com/en/comps/{tournament_fbref_id}/{season_year}/schedule/{season_year}-{tournament_name}-Scores-and-Fixtures'
        
            if get_teams_of_competition(spark, jdbc_url, db_properties, tournament_name, tournament_fbref_id, season_year, tournament_id).rdd.isEmpty():
                print(f"Error al obtener los equipos de la competición {tournament_name}")
                continue

            error_fixture_data, match_errors = get_fixture_data(url, tournament_name, tournament_id, season_year, season_id, type_of_competition, spark, jdbc_url, db_properties)
            if not error_fixture_data.empty:

                if error_fixture_data["Mensaje"].iloc[0] == "No se han encontrado partidos nuevos":
                    print("No se han encontrado partidos nuevos.")
                    continue
                else:
                    print(f"Error al obtener los siguientes partidos: ")
                    for match in match_errors:
                        print(match)
                        print("")
                    error_fixture_data.to_excel("fallos_partidos.xlsx", index=False)

            elif error_fixture_data.empty:
                print("Ha habido demasiados errores, se ha detenido el proceso.")
                print(error_fixture_data)
                break

                    
    
    except FileNotFoundError as e:
        print(f"Error encontrado: {e}")
        print("Reiniciando Spark y volviendo a intentar...")
        
        spark.stop()
        time.sleep(5)  # Pequeña pausa antes de reiniciar

        spark = create_spark_session()
        get_5_leagues(spark, jdbc_url, db_properties)
    
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()
    
    return pd.DataFrame({"Mensaje": ["Datos de los partidos procesados correctamente."]})

            





