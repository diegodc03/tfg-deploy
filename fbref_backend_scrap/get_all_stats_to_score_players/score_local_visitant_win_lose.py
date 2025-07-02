 
    
    
    
import pandas as pd
from pyspark.sql.types import StructType
from pyspark.sql.functions import lit, when
from utils.read_dataframe_to_mysql_file import read_data_with_spark
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_team_id_from_player_id, select_football_match
    
###########################################################################
# 
# score_by_local_visitant_and_win_lose.py
#
# Parameters:
# - spark: Spark session object
# - jdbc_url: JDBC URL for the database connection
# - db_properties: Database connection properties
# - match_id: ID of the match
# - league_id: ID of the league
#
# Returns:
# - final_spark: DataFrame containing player scores based on match outcome and home/away status
###########################################################################
def score_by_local_visitant_and_win_lose(spark, jdbc_url, db_properties, match_id, league_id):
    print("Puntuación de los jugadores en base a la victoria o derrota del partido y si es local o visitante")
    # Coger quien ganó y los jugadores que jugadon y darles un 15% de la puntuación total, 10 % por ganar y 5% por ser local o visitante
    # En ese 5% solo se dará si es jugador visitante ya que no tiene sentido darles un 5% por que juegan en casa
    winning_team, lossing_team, home_away = get_winning_losing_match(spark, jdbc_url, db_properties, match_id)
    
    spark_df = get_team_id_from_player_id(spark, jdbc_url, db_properties, match_id, winning_team, lossing_team)
    
    if spark_df.count() > 0:
        
        if home_away != "Draw":
            value = 0.7 if home_away == "Home" else 1.0
            
            final_spark = spark_df.withColumn(
                "score",
                when(spark_df.team_id == winning_team, lit(value)).otherwise(lit(0.0))
            )
        else:
            final_spark = spark_df.withColumn("score", lit(0.5))
    else:
            print("No hay jugadores en el partido")
            final_spark = spark.createDataFrame([], StructType([]))
    
    return final_spark




############################################################################
#
# get_winning_losing_match.py
#
# Parameters:
# - spark: Spark session object
# - jdbc_url: JDBC URL for the database connection
# - db_properties: Database connection properties
# - match_id: ID of the match
#
# Returns:
# - winning_team: ID of the winning team
# - lossing_team: ID of the losing team
# - home_away: Indicates if the winning team is home or away
############################################################################
def get_winning_losing_match(spark, jdbc_url, db_properties, match_id):
    winning_team = None
    lossing_team = None
    home_away = None
    
    winning_losing_match = select_football_match(spark, jdbc_url, db_properties, match_id)
    
    if winning_losing_match is None:
        print("No se encontró el partido con el ID proporcionado.")

    else:
        home_score = winning_losing_match["Score"].split("–")[0]
        away_score = winning_losing_match["Score"].split("–")[1]
        home_team = winning_losing_match["Home"]
        away_team = winning_losing_match["Away"]
            
        if home_score > away_score:
            winning_team = home_team
            lossing_team = away_team
            home_away = "Home"
        elif away_score > home_score:
            winning_team = away_team
            lossing_team = home_team
            home_away = "Away"
        else:
            winning_team = away_team
            lossing_team = home_team
            home_away = "Draw"
    
    return winning_team, lossing_team, home_away


