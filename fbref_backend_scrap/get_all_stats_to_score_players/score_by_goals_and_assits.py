

###### Este script se encarga de obtener los goles y asistencias de los jugadores en un partido y calcular su puntuación
#
# Importar librerías necesarias
import pandas as pd
from pyspark.sql.functions import col
from w_read_dataframe_to_mysql_file import read_data_with_spark
from pyspark.sql.types import StructType

# Por cada gol se le da 0.3 y por cada asistencia 0.15, por lo que si un jugador tiene 2 goles y 1 asistencia, se le da 0.3*2 + 0.15*1 = 0.75
def get_score_by_goals_and_assist(spark, jdbc_url, db_properties, match_id, league_id):
    
    print("Comienzo con la adición de segun los goles y asistencias de los jugadores")
    
    spark_df = get_goals_assists_of_match(spark, jdbc_url, db_properties, match_id, league_id)
    
    if spark_df.count() > 0:
        spark_df = spark_df.withColumn("score", (col("goals") * 0.3) + (col("assists") * 0.15))

    else:
        print("No hay jugadores en el partido")
        spark_df = spark.createDataFrame([], StructType([]))
        
    return spark_df
    
     
    
def get_goals_assists_of_match(spark, jdbc_url, db_properties, match_id, league_id):
    
    query = f"""
        SELECT ms.player_id, ms.goals, ms.assists FROM match_statistics ms WHERE ms.match_id = {match_id}
    """
    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
            
    return spark_df


