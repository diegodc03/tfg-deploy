


import math
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType
import pandas as pd
from pyspark.sql import functions as F
import traceback

from constants import table_dic_to_insert, basic_elements_of_player, basic_elements_of_gk, match_statisctics_of_player, match_statisctics_of_gk, stats_goalkeeper_summary, dic_stats
from w_read_dataframe_to_mysql_file import read_data_with_spark
from spark_schema import get_schema_by_index, get_shots_stats_schema, get_match_stats_schema, get_position_player_schema

from write_dataframe_to_mysql_file import write_dataframe_to_mysql
from fbref_db_call_outcome_shots_events import get_player, get_team_id_by_name_andleague_id, get_event_shots, get_body_part, get_outcome
from clean_dataframe_file import clean_dataframe
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import select_football_match


############################################################################
# recoge los datos de los jugadores, introduce en la base de datos todas las estadisticas de los jugadores
#
# match_id: id del partido
# league: nombre de la liga
# season: temporada
# local: nombre del equipo local
# visitor: nombre del equipo visitante
# player_data: datos de los jugadores
#
# return: False si hay un error, True si no hay error
#
##############################################################################

def get_all_data_of_player(match_id, league, league_id, season, season_id, local, visitor, player_data, spark, jdbc_url, db_properties):
    print('Getting all data of player...')
    
    try:
        local_field_player = [player_data[3], player_data[4], player_data[5], player_data[6], player_data[7], player_data[8]]
        local_goalkeeper = player_data[9]
        visitor_field_player = [player_data[10], player_data[11], player_data[12], player_data[13], player_data[14], player_data[15]]
        visitor_goalkeeper = player_data[16]
        
        print("\n\n")

        success1 = get_player_data(local_field_player, match_id, league, season, local, 0, spark, jdbc_url, db_properties)
        if success1 is None or success1.isEmpty():
            print("Error al procesar datos de algunos jugadores locales")
            return spark.createDataFrame([], StructType([]))   
        print("\n\n")

        success3 = get_player_data(visitor_field_player, match_id, league, season, visitor, 1, spark, jdbc_url, db_properties)
        if success3 is None or success3.isEmpty():
            print("Error al procesar datos de algunos jugadores visitantes")
            return spark.createDataFrame([], StructType([]))   
        print("\n\n")
        
        success2 = get_gk_data(local_goalkeeper, match_id, league, season, local, 0, spark, jdbc_url, db_properties)
        if success2 is None or success2.isEmpty():
            print("Error al procesar datos de los porteros locales")
            return spark.createDataFrame([], StructType([]))   
        print("\n\n")
        
        success4 = get_gk_data(visitor_goalkeeper, match_id, league, season, visitor, 1, spark, jdbc_url, db_properties)
        if success4 is None or success4.isEmpty():
            print("Error al procesar datos de los porteros visitantes")
            return spark.createDataFrame([], StructType([]))   
        print("\n\n")
        
        success5 = get_shots_data(player_data[17], match_id, league_id, season_id, local, visitor, spark, jdbc_url, db_properties)
        if success5 is None or success5.isEmpty():
            print("Error al procesar datos de los tiros")
            return spark.createDataFrame([], StructType([]))   

    except Exception as e:
        print(f"Error en get_all_data_of_player: {e}")
        return spark.createDataFrame([], StructType([]))   

    print('All data of player collected...')
    schema = StructType([StructField("message", StringType(), True)])
    data = [Row("Datos de jugadores y porteros procesados correctamente.")]
    return spark.createDataFrame(data, schema)
    



def get_shots_data(data_frame, match_id, league_id, season_id, local, visitor, spark, jdbc_url, db_properties):
    print('Getting shots data...')
    error_shots = []
    returning_value = spark.createDataFrame([], StructType([]))
    
    try:
        data_frame = data_frame.copy()
        all_data = []

        for index, row in data_frame.iterrows():
            # Comprobar que el row entero es Nan
            if row.isnull().all():
                continue

            # Acceder a los valores por índice
            minute = row.iloc[0]  # Índice 0
            player = get_player(row.iloc[1], spark, jdbc_url, db_properties)  # Índice 1
            squad = get_team_id_by_name_andleague_id(row.iloc[2], league_id, spark, jdbc_url, db_properties)  # Índice 2
            xG = row.iloc[3]  # Índice 3
            PSxG = row.iloc[4]  # Índice 4
            outcome = get_outcome(row.iloc[5], spark, jdbc_url, db_properties)  # Índice 5
            distance = row.iloc[6]  # Índice 6
            body_part = get_body_part(row.iloc[7], spark, jdbc_url, db_properties)  # Índice 7
            player_sca1 = get_player(row.iloc[9], spark, jdbc_url, db_properties)  # Índice 9
            event_sca1 = get_event_shots(row.iloc[10], spark, jdbc_url, db_properties)  # Índice 10
            player_sca2 = get_player(row.iloc[11], spark, jdbc_url, db_properties)  # Índice 11
            event_sca2 = get_event_shots(row.iloc[12], spark, jdbc_url, db_properties)  # Índice 12

            if player == -1 or squad == -1 or outcome == -1 or body_part == -1:
                print("Error al obtener los IDs de los datos de los tiros.")
                print("Player:", player, "Squad:", squad, "Outcome:", outcome, "Body Part:", body_part)
                error_shots.append(row)
                continue
            

            if isinstance(xG, str) and xG.lower() == 'nan':  # Si PSxG es 'NaN' como cadena
                xG = 0.0  # Asignar 0.0
            elif isinstance(xG, (int, float)) and math.isnan(xG):  # Si PSxG es NaN como valor numérico
                xG = 0.0  # Asignar 0.0PSxG, int):  # Si PSxG es 'NaN' como cadena
            
            if isinstance(distance, str) and distance.lower() == 'nan':  # Si PSxG es 'NaN' como cadena
                distance = 0.0  # Asignar 0.0
            elif isinstance(distance, (int, float)) and math.isnan(distance):  # Si PSxG es NaN como valor numérico
                distance = 0.0  # Asignar 0.0PSxG, int):  # Si PSxG es 'NaN' como cadena

            if isinstance(PSxG, str) and PSxG.lower() == 'nan':  # Si PSxG es 'NaN' como cadena
                PSxG = 0.0  # Asignar 0.0
            elif isinstance(PSxG, (int, float)) and math.isnan(PSxG):  # Si PSxG es NaN como valor numérico
                PSxG = 0.0  # Asignar 0.0PSxG, int):  # Si PSxG es 'NaN' como cadena

            # Crear nuevo diccionario con los valores modificados
            shot_data = {
                'shot_minute': minute,
                'player_shot': player,
                'team_shot': squad,
                'xg': xG,
                'psxg': PSxG,
                'outcome': outcome,
                'distance': distance,
                'body_part': body_part,
                'player_assisted_1': player_sca1,
                'event_type': event_sca1,
                'player_assisted_2': player_sca2,
                'event_type_2': event_sca2,
                'match_id': match_id
            }

            all_data.append(shot_data)

        if all_data:
            schema = get_shots_stats_schema()
            df = pd.DataFrame(all_data)  # Convertir lista de diccionarios en DataFrame
            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "stats_shots_summary")
            returning_value = df_spark

    except Exception as e:
        print(f"Error al obtener los datos de los tiros: {e}")
        returning_value = spark.createDataFrame([], StructType([]))
    
    if len(error_shots) > 3:
        print(f"Se encontraron {len(error_shots)} filas con errores en los datos de los tiros.")
        for i, row in enumerate(error_shots):
            print(f"Fila {i + 1}: {row}")
            
        returning_value = spark.createDataFrame([], StructType([]))

    print('Shots data collected...')
    return returning_value



def add_position_on_field_of_each_player(data_frame, spark, jdbc_url, db_properties):
    print('Adding position on field of each player...')
    returning_value = spark.createDataFrame([], StructType([]))
    
    #Se va a añadir la posición en el campo de cada jugador
    data_frame = data_frame.drop_duplicates()
 
    spark_df = spark.read.jdbc(
        url=jdbc_url, 
        table="position_on_the_field", 
        properties=db_properties
    ).select("position_id", "position_name")
    
    dict_positions = {}
    for row in spark_df.collect():
        dict_positions[row['position_name'].upper()] = row['position_id']

    try:
        # Crear una lista para almacenar las filas que vamos a insertar
        positions_to_insert = []
        data_frame = data_frame.toPandas()
        # Iterar sobre cada jugador
        for index, row in data_frame.iterrows():
            player_id = row['player_id']
            positions = row['position'].split(',')  # Dividir las posiciones separadas por comma
            match_id = row['match_id']

            # Crear una fila para cada posición
            for position in positions:
                position = position.strip().upper()  # Eliminar espacios adicionales

                # Verificar si la posición existe en el diccionario
                if position in dict_positions:
                    position_id = dict_positions[position]
                    positions_to_insert.append((position_id, match_id, player_id))
                else:
                    continue  # Si la posición no está en la tabla, se ignora

        # Crear un DataFrame a partir de las posiciones divididas
        positions_df = pd.DataFrame(positions_to_insert, columns=["position", "match_id", "player_id"])

        # Convertir el DataFrame a Spark DataFrame
        schema = get_position_player_schema()  # Asegúrate de que el esquema tiene player_id y position
        spark_df = spark.createDataFrame(positions_df, schema)

        # Insertar los datos en la base de datos
        write_dataframe_to_mysql(spark_df, jdbc_url, db_properties, "position_player")
        returning_value = spark_df
        print("Posiciones añadidas correctamente.")
        
    except Exception as e:
        print(f"Error al añadir la posición en el campo de cada jugador: {e}")
        returning_value = spark.createDataFrame([], StructType([]))

    return returning_value







        

##############################################################################
# recoge los datos de los jugadores, introduce en la base de datos todas las estadisticas de los jugadores
#
# list_tables_player: lista de tablas de los jugadores
# match_id: id del partido
# league: nombre de la liga
# season: temporada
# local_or_visitor_name_team: nombre del equipo local o visitante
# flag_local_visitor: 0 si es local, 1 si es visitante
#
##############################################################################
def get_player_data(list_tables_player, match_id, league, season, local_or_visitor_name_team, flag_local_visitor, spark, jdbc_url, db_properties):
    type_of_player = 0
    stats_element = dic_stats
    print('Getting player data...')
    index1 = 0

    try:
        for index, table in enumerate(list_tables_player):
            index1 = index + 1
            stats = stats_element[index + 1]
            data_frame = table
            
            data_frame = data_frame.iloc[:-1]

            # Asegurar que las columnas coinciden con stats_summary_player
            if len(data_frame.columns) != len(stats):
                raise ValueError("El número de columnas en la tabla no coincide con los que son en la columna stats")
                
            # Renombrar las columnas
            [col_name for col_name, _ in zip(stats, data_frame.columns)]
            data_frame.columns = stats
 
            if index == 0:
                data_frame_basic = data_frame[basic_elements_of_player]
                
                data_frame_basic = data_frame_basic.copy()
                data_frame_basic["shirt_number"] = data_frame_basic["shirt_number"].astype(int, errors="ignore")
                data_frame_basic["age"] = data_frame_basic["age"].str.split('-').str[0].astype(int, errors="ignore")
         
                inserts_of_player_and_basic_stats = insert_basic_elements_of_player_into_database(index1, type_of_player, data_frame_basic, match_id, league, season, local_or_visitor_name_team, flag_local_visitor, spark, jdbc_url, db_properties)
                if inserts_of_player_and_basic_stats.isEmpty():
                    return spark.createDataFrame([], StructType([]))

                df_selected = inserts_of_player_and_basic_stats[["position", "match_id", "player_id"]]
                if add_position_on_field_of_each_player(df_selected, spark, jdbc_url, db_properties).isEmpty():
                    return spark.createDataFrame([], StructType([]))

            data_frame = clean_dataframe(data_frame)

            df = insert_dataframe_into_database_of_player(index1, data_frame, local_or_visitor_name_team, match_id, spark, jdbc_url, db_properties)
            if df.isEmpty():
                print("Error al insertar los datos de los jugadores.")
                return spark.createDataFrame([], StructType([]))
            

    except Exception as e:
        print(f"Error procesando el equipo: {e} ")
        return spark.createDataFrame([], StructType([]))
    
    return df



#MEJORAR ESTO, se tiene que poder añadir a mathch_statistics un juygador si no está
##############################################################################
# recoge los datos de los porteros, introduce en la base de datos todas las estadisticas de los porteros
# 
# data_frame: tabla de los porteros
# match_id: id del partido
# league: nombre de la liga
# season: temporada
# local_or_visitor_name_team: nombre del equipo local o visitante
# flag_local_visitor: 0 si es local, 1 si es visitante
# 
# return: False si hay un error, True si no hay error
# 
# ##############################################################################     
def get_gk_data(data_frame, match_id, league, season, local_or_visitor_name_team, flag_local_visitor, spark, jdbc_url, db_properties):
    type_of_player = 1
    print('Getting goalkeeper data...')
    returning_value = spark.createDataFrame([], StructType([]))
    try:
        if len(data_frame.columns) != len(stats_goalkeeper_summary):
            raise ValueError("El número de columnas en la tabla no coincide con los que son en la columna stats")

        [col_name for col_name, _ in zip(stats_goalkeeper_summary, data_frame.columns)]
        data_frame.columns = stats_goalkeeper_summary
 
        data_frame_basic = data_frame[basic_elements_of_gk]   

        data_frame_basic = data_frame_basic.copy()
        data_frame_basic["age"] = data_frame_basic["age"].str.split('-').str[0].astype(int, errors="ignore")

        index = 0
        data_frame_copy = data_frame.copy()
        data_frame_cleaned = clean_dataframe(data_frame_copy)
                

        data_frame_cleaned["gk_passes_completed_launched"] = data_frame_cleaned["gk_passes_completed_launched"].fillna(0).astype(int, errors="ignore")
        data_frame_cleaned["gk_crosses_stopped"] = data_frame_cleaned["gk_crosses_stopped"].fillna(0).astype(int, errors="ignore")
        data_frame_cleaned["gk_goals_against"] = data_frame_cleaned["gk_goals_against"].fillna(0).astype(int, errors="ignore")
        data_frame_cleaned["gk_def_actions_outside_pen_area"] = data_frame_cleaned["gk_def_actions_outside_pen_area"].fillna(0).astype(int, errors="ignore")
        
        gk_data = insert_dataframe_into_database_of_player(index, data_frame_cleaned, local_or_visitor_name_team, match_id, spark, jdbc_url, db_properties)
        if not gk_data.isEmpty():
            returning_value = gk_data
        
        
    except Exception as e:
        print(f"Error procesando el equipo: {e} ")
        returning_value = spark.createDataFrame([], StructType([]))

    print('Goalkeeper data collected...')
    return returning_value



def insert_dataframe_into_database_of_player(index, df, local_visitor, match_id, spark, jdbc_url, db_properties):
    try:
        
        returning_value = spark.createDataFrame([], StructType([]))
        
        print("Insertando datos de jugadores en la base de datos, en la tabla: ", table_dic_to_insert[index])
        schema_to_insert = get_schema_by_index(index)
        
        if schema_to_insert is None:
            print(f"Esquema no encontrado para el índice {index}.")
        
        else: 
                    
            # Obtener la tabla de jugadores desde la BD
            jugadores_df = spark.read.jdbc(
                url=jdbc_url, 
                table="jugador", 
                properties=db_properties
            ).select("player", "player_id").alias("jugadores")
            
            # Obtener estadísticas existentes de match_statistics
            match_stats_df = spark.read.jdbc(
                url=jdbc_url, 
                table="match_statistics", 
                properties=db_properties
            ).select("player_id", "match_id", "estadistica_id").filter(F.col("match_id") == match_id).alias("match_stats")
        
            # Convertir el dataframe de entrada a Spark y unir con la tabla de jugadores
            df_spark = spark.createDataFrame(df).alias("df_spark")

            df_spark = df_spark.join(
                jugadores_df, 
                (F.col("df_spark.player") == F.col("jugadores.player")), 
                "left"
            ).select("df_spark.*",
            F.col("jugadores.player_id").alias("player_id"))

            df_spark = df_spark.drop("player")
            df_spark = df_spark.alias("df_spark")
            
            # Filtrar jugadores no encontrados
            missing_players = df_spark.filter(F.col("player_id").isNull())
            if missing_players.count() > 0:
                print(f"Se encontraron {missing_players.count()} jugadores no registrados en la BD:")
                missing_players.select("player_id").show()

            # Filtrar jugadores que sí tienen ID en la BD
            df_spark = df_spark.filter(F.col("player_id").isNotNull())
            df_spark = df_spark.alias("df_spark")
            # Unir con las estadísticas del partido para obtener `estadistica_id`
            df_spark = df_spark.join(
                match_stats_df, 
                (F.col("df_spark.player_id") == F.col("match_stats.player_id")), 
                "left"
            ).select("df_spark.*", 
            F.col("match_stats.estadistica_id").alias("estadistica_id"))

            # Filtrar jugadores sin estadísticas registradas para ese partido
            missing_stats = df_spark.filter(F.col("estadistica_id").isNull())
            if missing_stats.count() > 0:
                print(f"Se encontraron {missing_stats.count()} jugadores sin estadísticas registradas en el partido {match_id}.")
                missing_stats.select("player_id").show()

            # Filtrar solo aquellos que sí tienen `estadistica_id`
            df_spark = df_spark.filter(F.col("estadistica_id").isNotNull())
            df_spark = df_spark.drop("shirt_number", "nacionality", "position", "minutes", "goals", "assists")

            # Insertar solo si hay datos válidos
            if df_spark.count() > 0:
                table_name = table_dic_to_insert[index]

                df = spark.createDataFrame(df_spark.toPandas(), schema_to_insert)
                write_dataframe_to_mysql(df, jdbc_url, db_properties, table_name)
                returning_value = df
            else:
                print("No se insertaron datos, ya que no se encontraron jugadores o estadísticas adecuadas, datos insertados incorrectamente en la tabla.", table_dic_to_insert[index])
                
    except Exception as e:
        print("Error insertando datos en la base de datos:", e)
        returning_value = spark.createDataFrame([], StructType([]))
    print("Datos insertados correctamente.")
    return returning_value







def insert_basic_elements_of_player_into_database(index, type_of_player, data_frame_basic, match_id, league, season, local_visitor_team_name, local_visitor_flag, spark, jdbc_url, db_properties):
    try:

        print("Insertando estadísticas básicas de jugadores en la base de datos...")
        returning_value = spark.createDataFrame([], StructType([]))

        data_frame_basic = data_frame_basic.copy()
        data_frame_basic.loc[:, 'match_id'] = match_id

        league = league.replace("-", " ")

        spark_df = select_football_match(spark, jdbc_url, db_properties, match_id)
        if spark_df is None:
            print(f"Error: No se encontró el partido con match_id {match_id}.")
            return spark.createDataFrame([], StructType([]))
        else:
            # Verificar si el partido es local o visitante
            if local_visitor_flag == 0:
                team_id = spark_df["Home"]
            elif local_visitor_flag == 1:
                team_id = spark_df["Away"]
            else:
                print("Error: local_visitor_flag debe ser 0 o 1.")
                return spark.createDataFrame([], StructType([]))
        

        # Obtener IDs de los jugadores en la BD
        existing_players_df = spark.read.jdbc(
            url=jdbc_url, 
            table="jugador", 
            properties=db_properties
        ).select("player", "player_id")

        # Unir datos de jugadores con los IDs existentes
        data_frame_basic_spark = spark.createDataFrame(data_frame_basic)
        data_frame_basic_spark = data_frame_basic_spark.join(existing_players_df, "player", "left")
        
        # Insertar nuevos jugadores si no existen
        new_players_df = data_frame_basic_spark.filter(data_frame_basic_spark.player_id.isNull()).select("player", "nacionality").distinct()
   
        if new_players_df.count() > 0:
            print(f"Se encontraron {new_players_df.count()} jugadores nuevos. Insertando en la base de datos...")
            write_dataframe_to_mysql(new_players_df.drop("position"), jdbc_url, db_properties, "jugador")

            # Volver a cargar los jugadores con sus IDs
            existing_players_df = spark.read.jdbc(url=jdbc_url, table="jugador", properties=db_properties).select("player", "player_id")
            data_frame_basic_spark = data_frame_basic_spark.drop("player_id").join(existing_players_df, "player", "left")

        # Obtener `player_id` correctamente
        data_frame_basic_spark = data_frame_basic_spark.filter(data_frame_basic_spark.player_id.isNotNull())

        # Verificar si existe la relación `team_player`
        team_player_df = spark.read.jdbc(url=jdbc_url, table="team_player", properties=db_properties).select("player_id", "team_id")

        # Hacer alias de las columnas 'player_id' para evitar ambigüedad
        data_frame_basic_spark = data_frame_basic_spark.alias("df_basic")
        team_player_df = team_player_df.alias("df_team_player")

        # Realizar el join y usar los alias para evitar ambigüedad
        missing_team_player_df = data_frame_basic_spark.join(
            team_player_df, 
            (F.col("df_basic.player_id") == F.col("df_team_player.player_id")) & 
            (F.col("df_team_player.team_id") == team_id), 
            "left"
        ).filter(F.col("df_team_player.team_id").isNull()).select("df_basic.player_id").distinct()

        # Insertar nuevas relaciones `team_player`
        if missing_team_player_df.count() > 0:
            missing_team_player_df = missing_team_player_df.withColumn("team_id", F.lit(team_id))
            write_dataframe_to_mysql(missing_team_player_df, jdbc_url, db_properties, "team_player")

        # Obtener estadísticas de `match_statistics`
        match_stats_df = spark.read.jdbc(url=jdbc_url, table="match_statistics", properties=db_properties).select("player_id", "match_id")

        # Hacer alias de las columnas para evitar ambigüedad
        data_frame_basic_spark = data_frame_basic_spark.alias("df_basic")
        match_stats_df = match_stats_df.alias("match_stats")

        # Realizar el join y usar los alias para evitar ambigüedad
        missing_stats_df = data_frame_basic_spark.join(
            match_stats_df, 
            (F.col("df_basic.player_id") == F.col("match_stats.player_id")) & 
            (F.col("match_stats.match_id") == match_id), 
            "left"
        ).filter(F.col("match_stats.match_id").isNull())

        # Insertar estadísticas si faltan
        if missing_stats_df.count() > 0:
            stats_columns = match_statisctics_of_player if type_of_player == 0 else match_statisctics_of_gk
            stats_df = missing_stats_df.select(["df_basic.player_id", "df_basic.match_id"] + stats_columns)

            write_dataframe_to_mysql(stats_df, jdbc_url, db_properties, "match_statistics")
            
        else:
            print("No se encontraron estadísticas faltantes para insertar.")

    except Exception as e:
        print("Error al insertar estadísticas básicas de jugadores:")
        traceback.print_exc()
        return spark.createDataFrame([], StructType([]))

    print("Inserción completada correctamente.")
    return data_frame_basic_spark







