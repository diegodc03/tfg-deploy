import pandas as pd
from pyspark.sql.functions import col, lit, when
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DoubleType
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.functions import udf


# ver como podemos poner si una estadistica es positiva o negativa

negative_stats = [
    "goals_against",
    "goals_conceded",
    "yellow_cards",
    "red_cards",
    "fouls_committed",
    "offside",
    "fouled",
    "aerials_lost",
    "errors",
    "dispossessed",
    "miscontrols",
    "gk_goals_against",
]



# Hacer las estadiscticas para los que han jugado menos de 70 minutos y menos de 20

############################################################################################################
#
#   get_score_for_positions
#
#  Function that gets the positions of the players
#       - This function calculates a score  from 0 to 10 for each player based on their stats and the stats of the same position
#
#   Parameters:
#       - spark_df: Spark DataFrame, cada fila tiene a un jugador y sus estadísticas
############################################################################################################
def get_score_for_positions_with_only_match_stats(players_spark_df):
    
    print("Comienzo con la adición de puntuación de stats de los jugadores por posición1")
    stats_schema = StructType([
        StructField("stat_name", StringType(), True),
        StructField("avg", FloatType(), True),
        StructField("desv", FloatType(), True),
        StructField("mode", FloatType(), True)
    ])
    stats = []
    spark_columns = players_spark_df.columns
    
    # Filtramos por los minutos para tener dos dataframes, uno para los que han jugado más de 70 minutos y otro para los que han jugado menos de 70 minutos
    players_spark_df_more_70 = players_spark_df.filter(F.col("minutes") >= 70)
    players_spark_df_less_70 = players_spark_df.filter(F.col("minutes") < 70)
    
    data = [players_spark_df_more_70, players_spark_df_less_70]
    all_scores = []
    
    if data[0].count() <= 0 and data[1].count() <= 0:
        print("No hay jugadores con estadísticas para puntuar")
        return players_spark_df.sparkSession.createDataFrame([], StructType([]))
    
    print("Comenzamos a calcular las puntuaciones de los jugadores")
    print("Número de jugadores con más de 70 minutos:", data[0].count())
    print("Número de jugadores con menos de 70 minutos:", data[1].count())
    
    for df in data:

        if df.count() == 0:
            print("No hay jugadores con estadísticas para puntuar")
            continue
        else:
            players_spark_df = df
            
            # Filtrar las columnas que no son estadísticas
            spark_columns = [col for col in spark_columns if col not in [
                "player_id", "match_id", "estadistica_id", "position_id", "category_id", "team_role", "team_id"    
            ]]
            
            stats = []  # reseteamos para cada grupo
            
            for column in spark_columns:
                if column == "player_id" or column == "match_id" or column == "estadistica_id" or column == "position_id":
                    continue
                # Calcular la media y la desviación estándar de cada estadística
                result = players_spark_df.agg(
                    F.avg(column).alias("avg"),
                    F.stddev(column).alias("desv")
                ).collect()[0]
                
                mode_val = players_spark_df.groupBy(column).count().orderBy(F.desc("count")).first()
                mode_value = float(mode_val[column]) if mode_val[column] is not None else 0.0
                
                # Crea una row para cada estadística
                stats.append(Row(stat_name=column, avg=result["avg"], desv=result["desv"], mode=mode_value))

            if players_spark_df.count() > 0:
                # Crear un DataFrame de Spark con las estadísticas
                stats_of_match_spark_df = players_spark_df.sparkSession.createDataFrame(stats, schema=stats_schema)
                players_score_spark_df = loop_of_stats(stats_of_match_spark_df, players_spark_df, spark_columns)
                all_scores.append(players_score_spark_df)
    
    if all_scores:
        final_df = all_scores[0]
        for df in all_scores[1:]:
            final_df = final_df.unionByName(df)
        return final_df
    else:
        return players_spark_df.sparkSession.createDataFrame([], StructType([]))

        






def calc_score(player_stat, avg, desv, stat_name, mode=None, base=6.5, multiplier=3.5, desviacion_umbral=0.7, peso_media=0.5):
    
    if avg is None or desv is None:
        return base
    
    if desv == 0:
        return base

    # Ajuste de la media usando moda si la desviación es muy alta
    if avg != 0 and desv / avg > desviacion_umbral and mode is not None:
        base = 5.6
        avg = (avg * peso_media) + (mode * (1 - peso_media))

    # Cálculo del score
    if stat_name in negative_stats:
        diff = (avg - player_stat) / desv
    else:
        diff = (player_stat - avg) / desv

    puntuacion = base + multiplier * diff

    if puntuacion > 10:
        puntuacion = 10.0
    elif puntuacion < 0:
        puntuacion = 0.0
    
    return puntuacion




# Convertimos la función calc_score a una UDF de PySpark
calc_score_udf = udf(calc_score, DoubleType())


def loop_of_stats(df_combined, spark_df, stats_columns):
    
    for stat in df_combined.collect():
        stat_name = stat["stat_name"]
        avg = stat["avg"]
        desv = stat["desv"]
        mode_value = stat["mode"]

        if stat_name in spark_df.columns:
            score_col = f"{stat_name}_score"
            spark_df = spark_df.withColumn(
                score_col,
                when(
                    col(stat_name).isNotNull(),
                    calc_score_udf(col(stat_name), lit(avg), lit(desv), lit(stat_name), lit(mode_value))
                ).otherwise(0)
            )
        else:
            print(f"Columna '{stat_name}' no encontrada en spark_df")
            
    length_of_stats_columns = len(stats_columns)

    spark_scores = spark_df.withColumn(
        "total_score",
        F.round(sum([col(f"{stat}_score") for stat in stats_columns]) / length_of_stats_columns, 2)
    ).select("player_id", "total_score")
    
    return spark_scores




# Cogemos el numero de estadísticas importantes para cada posición
    # Teniendo todas las stats importantes, cogemos el numero, eso se hace cogiendo el numero de columnas menos las que no son estadísticas

    # Para esta parte se le va a dar una puntuacion sobre 100
        # Haciendo que cada stat si es mayor que 


# meter el ganador
# Estars que son negativas
# mirar si las que tengan 0 tienen valor estadístico, ya que va a haber veces que no tenga sentido añadir esas estadísticas

# Si la estat tiene pct, si tieen 0 mirar a ver, ya que no tiene sentido puntuar si no ha habido nada


def calculate_player_scores_by_avg_of_season(spark_df, avg_df):
    # Hacer JOIN entre los DataFrames usando position_id y league_id
    returning_value = pd.DataFrame()
    
    # Filtrar los jugadores con >= 70 minutos y < 70 minutos de esta manera se podrá hacer la normalización de las estadísticas
    df_avg_starter = avg_df.filter(F.col("starter_status") == "starter")
    df_avg_substitute = avg_df.filter(F.col("starter_status") == "substitute")

    spark_df_substitute = spark_df.filter(F.col("minutes") < 70)
    spark_df_starter = spark_df.filter(F.col("minutes") >= 70)

    dict_stats = {
        "substitute": {
            "df": spark_df_substitute,
            "avg_df": df_avg_substitute
        },
        "starter": {
            "df": spark_df_starter,
            "avg_df": df_avg_starter
        }
    }

    stats_columns = [col for col in avg_df.columns if col not in ["league_id", "position_player", "starter_status", "type_of_stat"]]
    dataframe_to_return = None

    for df in dict_stats.values():
        spark_players = df["df"]
        df_avg = df["avg_df"]
        
        element = combine_all_stats_and_score_all(df_avg, spark_players, stats_columns)
        if element is None:
            print("No hay jugadores con estadísticas para puntuar en avg_of_season")
            continue
        else:
            dataframe_to_return = (
                dataframe_to_return.union(element)
                if dataframe_to_return is not None else element
            )
                
    return dataframe_to_return if dataframe_to_return is not None else pd.DataFrame()



    
           
           
def combine_all_stats_and_score_all(df_avg_lt_th_70, spark_df, stats_columns):
    
    
    # Lo que hace esto es -->
        # SelectExp permite aplicar SQL a un DataFrame
        # Seleccionamos las columnas que queremos, en este caso league_id, position_player, starter_status, type_of_stat
        # stack es una función que apila las columnas en una sola columna, en este caso, apila todas las columnas de estadísticas para tener una columna de estadísticas y otra de valores
        # stack(3, 'goals', goals, 'assists', assists, 'shots', shots) --> apila las columnas goals, assists y shots en una sola columna
        # El resultado es un DataFrame con las columnas league_id, position_player, starter_status, type_of_stat, stat_name y value
    df_melted = df_avg_lt_th_70.selectExpr("league_id", "position_player", "starter_status", "type_of_stat",
                                    "stack(" + str(len(stats_columns)) + ", " +
                                    ", ".join([f"'{col}', {col}" for col in stats_columns]) + ") as (stat_name, value)")

    # Dividir el DataFrame en dos: uno para 'avg' y otro para 'desv'
    # Se usa un alias para poder hacer el JOIN posteriormente, ya que ambos DataFrames tienen las mismas columnas
    df_avg = df_melted.filter(F.col("type_of_stat") == "avg").alias("avg_df")
    df_desv = df_melted.filter(F.col("type_of_stat") == "desv").alias("desv_df")
    df_mode = df_melted.filter(F.col("type_of_stat") == "mode").alias("mode_df")

    #    Unir los DataFrames 'avg' y 'desv' por 'stat_name'
    df_combined = df_avg.join(df_desv, on=["league_id", "position_player", "starter_status", "stat_name"], how="inner") \
                    .join(df_mode, on=["league_id", "position_player", "starter_status", "stat_name"], how="inner") \
                    .select(
                        df_avg["stat_name"],
                        # Hacer referencia explícita a las columnas de 'avg' y 'desv' usando los alias
                        F.col("avg_df.value").alias("avg"),
                        F.col("desv_df.value").alias("desv"),
                        F.col("mode_df.value").alias("mode")
                    )    
    
    players_scores = loop_of_stats(df_combined, spark_df, stats_columns)
    return players_scores
    








    