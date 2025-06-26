




import sys
import pandas as pd
from pyspark.sql.functions import col
from pyspark.sql.functions import lit

from functions_to_stract_of_dataBase.querys_score_match import get_number_of_scores_by_type_of_game_mode_and_basic_position_id
from fbref_backend_scrap.utils.write_dataframe_to_mysql_file import write_dataframe_to_mysql
from pyspark.sql.types import StructType
from get_all_stats_to_score_players.specific_stats_for_type_game_mode import get_stats_by_type_of_play_form
from get_all_stats_to_score_players.score_local_visitant_win_lose import score_by_local_visitant_and_win_lose
from fbref_backend_scrap.functions_to_stract_of_dataBase.querys_scores_by_goals_and_assits import get_score_by_goals_and_assist
from get_all_stats_to_score_players.basic_stats_for_positions import get_stats_by_position 
from get_all_stats_to_score_players.create_unique_score_of_players import score_players_by_zone_of_field, score_players_by_type_of_play

from functions_to_stract_of_dataBase.selects_of_positions import get_id_of_specific_and_game_id_when_not_exists
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_all_matchs_ids_of_league_id, get_match_of_tournaments, get_rows_of_match_statistics, get_teams_in_competition

### PUNTUACIÓN DE LOS JUGADORES EN BASE UNICAMENTE A SUS ESTADÍSTICAS COMPARADAS CON ESE PARTIDO ###
############################################################################################################
# En este punto tengo un spark dataframe con todos los centrocampistas del partido y sus estadísticas más importantes,
# ahora tengo que coger cada una de las estadísticas y puntuarla sobre 10
# Para ello, voy a coger la media de cada estadística, es decir, la media de los centrocampistas de ese partido
# para conseguir eso, en pct sera facil, por que es 0 un 0 y un 10, 100, mientras que para los que no son valores, se cogera el menor y el mayor valor, poniendo a 0 el menor y a 10 el mayor
# Por último, con el min y el max, se hará una regla de tres para conseguir la puntuación de cada jugador





def get_score_of_5_leagues(spark, jdbc_url, db_properties):
    
    print('Getting score of 5 leagues...')
    spark_data = get_match_of_tournaments(spark, jdbc_url, db_properties)
    returning_value = spark.createDataFrame([], StructType([]))
    league_df = spark_data.filter(col('nombre_liga') == "La Liga")

    try:
        for row in league_df.collect():
            
            tournament_id = row["tournament_id"]
            tournament_name = row["nombre_liga"]
            tournament_name = tournament_name.replace(' ', '-')
            
            if tournament_id == 130 or tournament_id == 127:
                print("Skipping tournament with ID 130")
                continue
            
            print(f"Processing tournament: {tournament_name} with ID: {tournament_id}")
            
            match_ids = get_all_matchs_ids_of_league_id(spark, jdbc_url, db_properties, tournament_id)
            
            for match_id in match_ids.collect():
                print(f"Processing match ID: {match_id['match_id']} for tournament: {tournament_name}")

                returning_value = get_stats_score(spark, jdbc_url, db_properties, match_id['match_id'], tournament_id)
                if returning_value.isEmpty():
                    print('No data to collect')
                    continue
     
    except Exception as e:
        print(f"Error: {e}")
        returning_value = spark.createDataFrame([], StructType([]))
    
    return returning_value
 


############################################################################################################
#
#   get_stats_score
#
#  Function that gets the stats of the players and scores them
#
#   Parameters:
#       - spark: SparkSession
#       - jdbc_url: JDBC URL
#       - db_properties: Properties to connect to the database
#       - match_id: Match ID
#       - league_id: League ID --> contains the league_id of the match
############################################################################################################
def get_stats_score(spark, jdbc_url, db_properties, match_id, league_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores")

    returning_value = spark.createDataFrame([], StructType([]))

    dict_stats_basic_position = get_stats_by_position(spark, jdbc_url, db_properties, match_id, league_id)

    dict_stats_type_play_of_form = get_stats_by_type_of_play_form(spark, jdbc_url, db_properties, match_id, league_id)
    
    # Puntuacion que se da por ganar o perder el partido y si es local o visitante
    spark_df_visitant_win_lose = score_by_local_visitant_and_win_lose(spark, jdbc_url, db_properties, match_id, league_id)
    if spark_df_visitant_win_lose.isEmpty():
        print("No hay jugadores en el partido")
        returning_value = spark.createDataFrame([], StructType([]))
    else: 
        ## Puntuacion que se da por goles y asistencias
        spark_df_score_goals_and_assists = get_score_by_goals_and_assist(spark, jdbc_url, db_properties, match_id, league_id)

        if not spark_df_score_goals_and_assists.isEmpty():
            create_score_by_all_parts_of_scores(dict_stats_basic_position, spark_df_visitant_win_lose, spark_df_score_goals_and_assists, dict_stats_type_play_of_form, match_id, spark, jdbc_url, db_properties)
        
        returning_value = spark.createDataFrame([("Correcto",)], ["Correcto"])    
    return returning_value








#############################################################################################################
#
#   create_score_by_all_parts_of_scores
#
#############################################################################################################
def create_score_by_all_parts_of_scores(dict_stats_basic_position, spark_df_visitant_win_lose, spark_df_score_goals_and_assists, dict_stats_type_play_of_form, match_id, spark, jdbc_url, db_properties):
    print("Creando la puntuación de los jugadores en base a todas las puntuaciones obtenidas")
    
    if len(dict_stats_basic_position) != 0:
        # Devuelve un dictionario con los jugadores y la puntuacion por zona del campo y por tipo de juego
        dict_scores = score_players_by_type_of_play(dict_stats_basic_position, dict_stats_type_play_of_form, spark_df_score_goals_and_assists, spark_df_visitant_win_lose, spark, jdbc_url, db_properties)

        for game_mode, df_game_mode in dict_scores.items():
            introduce_scores_into_database(spark, jdbc_url, db_properties, df_game_mode, match_id)
     

    number_of_rows = get_number_of_scores_by_type_of_game_mode_and_basic_position_id(spark, jdbc_url, db_properties, match_id)
    if number_of_rows > 0:
        print("Ya existe las puntuaciones para el modo de juego y la posicion para  las posiciones básicas")
    else:
        # Retorna una unica puntuacion por cada jugador    
        df_scores = score_players_by_zone_of_field(dict_stats_basic_position, spark_df_score_goals_and_assists, spark_df_visitant_win_lose)
        # introduce_socores_into_database(spark, jdbc_url, db_properties, dict_scores, df_scores, match_id)
        introduce_scores_into_database(spark, jdbc_url, db_properties, df_scores, match_id)
    



    
def introduce_scores_into_database(spark, jdbc_url, db_properties, df_scores, match_id):

    # Obtener jugadores del partido en la base de datos
    players_df_of_match = get_rows_of_match_statistics(spark, jdbc_url, db_properties, match_id)

    # Join para obtener estadistica_id -> match_player_id
    df_scores_joined = df_scores.join(players_df_of_match, "player_id", "left").drop("player_id")
    df_scores_joined = df_scores_joined.withColumnRenamed("estadistica_id", "match_player_id")

    # Añadir columnas si no existen
    for col_name in ["specific_position_id", "game_mode_id"]:
        if col_name not in df_scores_joined.columns:
            # Obtener el id de la columna que no existe
            spark_df = get_id_of_specific_and_game_id_when_not_exists(spark, jdbc_url, db_properties, col_name)
            if spark_df.count() > 0:
                df_scores_joined = df_scores_joined.withColumn(col_name, lit(spark_df.collect()[0][col_name]))
            

    # Orden correcto de columnas
    df_scores_clean = df_scores_joined.select(
        "match_player_id", "specific_position_id", "basic_position_id", "score", "game_mode_id"
    )

    # Rellenar posibles nulos con 0 (para evitar errores en escritura)
    df_scores_clean = df_scores_clean.fillna({"specific_position_id": 0, "game_mode_id": 0, "score": 0})

    write_dataframe_to_mysql(df_scores_clean, jdbc_url, db_properties, "match_players_score")



    
    


