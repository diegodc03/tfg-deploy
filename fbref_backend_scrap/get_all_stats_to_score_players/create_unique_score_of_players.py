
   
# IMPORTS
from pyspark.sql import functions as F   
from get_all_stats_to_score_players.create_unique_df import create_unique_df
    
##########################################################################################################################
#
#   score_players_by_zone_of_field
#
#   Function that scores the players by zone of field
#
#   Parameters:
#       - dict_stats_basic_position: Dictionary with the stats of the players by position , ONLY PART OF STATS OF AVG OF ALL LEAGUE
#       - spark_df_score_goals_and_assists: DataFrame with the stats of the players by goals and assists, ONLY PART OF STATS OF AVG OF ALL LEAGUE
#       - spark_df_visitant_win_lose: DataFrame with the stats of the players by winning or losing the match and if they are local or visitant, ONLY PART OF STATS OF AVG OF ALL LEAGUE
#
#   Returns:
#       - DataFrame with the stats of the players by zone of field
###############################################################################################################################  
def score_players_by_zone_of_field(dict_stats_basic_position, spark_df_score_goals_and_assists, spark_df_visitant_win_lose):
    print("Puntuación de los jugadores en base a la zona del campo")
    
    
    # En este tipo de puntuación se le va a dar al jugador:
    # - 60% de la puntuación por la media de toda la liga
    # - 35% por la puntuación del partido en comparación con los jugadores de su posición
    # - 5% por goles, asistencias y ganar el partido
    
    avg_dfs = [dict_stats["avg"] for dict_stats in dict_stats_basic_position.values()]
    match_comp_dfs = [dict_stats["match_comp"] for dict_stats in dict_stats_basic_position.values()]
    
    # Crear listas de los DataFrames de estadísticas    
    final_avg_dfs = create_unique_df(avg_dfs)
    final_match_comp_dfs = create_unique_df(match_comp_dfs)

    
    # Alias para los DataFrames
    df_avg_alias = final_avg_dfs.withColumnRenamed("total_score", "avg_score").alias("avg")
    df_match_comp_alias = final_match_comp_dfs.withColumnRenamed("total_score", "match_comp_score").alias("match_comp")
    df_goals_assists_alias = spark_df_score_goals_and_assists.withColumnRenamed("score", "goals_assists_score").alias("goals_assists")
    df_visitant_win_lose_alias = spark_df_visitant_win_lose.withColumnRenamed("score", "visitant_win_lose_score").alias("visitant_win_lose")
    
    # Realizar los joins solo una vez
    df_combined = df_avg_alias.join(df_match_comp_alias,  ["player_id", "basic_position_id"], "left") \
                             .join(df_goals_assists_alias, "player_id", "left") \
                             .join(df_visitant_win_lose_alias, "player_id", "left")
                             
    
    # Ahora podemos calcular el score final
    df_combined = df_combined.withColumn(
        "score", 
        (F.col("avg_score") * 0.35) + 
        (F.col("match_comp_score") * 0.6) + 
        (F.col("goals_assists_score")) + (F.col("visitant_win_lose_score"))
    ).select("player_id", "basic_position_id", "score")
    
    print("La puntuación de los jugadores por zona del campo es ")
    for row in df_combined.collect():
        print(row)
    
    return df_combined
    
    
    
    
     
def score_players_by_type_of_play(dict_stats_basic_position, dict_stats_type_of_play, spark_df_score_goals_and_assists, spark_df_visitant_win_lose, spark, jdbc_url, db_properties):
    
    print("Puntuación de los jugadores en base al tipo de juego")
    
    # En este tipo de puntuación se le va a dar al jugador:
        # - 70% de la puntuación por la media de toda la liga con el tipo de la posicion específica
        # - 15% de la puntuación por la media de toda la liga por su posicion (defensores, centrocampistas y delanteros)
        # - 10% por la puntuación del partido en comparación con los jugadores de su posición
        # - 5% por goles, asistencias y ganar el partido
    
    dict_stats_type_of_play_scored = {}
    
    for game_mode, stats in dict_stats_type_of_play.items():
        print(f"Game Mode: {game_mode}")
        
        
        specific_positon = []
            
        for position, data in stats.items():
            
            print(f"  Position: {position}")
            
            avg_specific = data["avg"]
            
            avg_dfs = [dict_stats["avg"] for dict_stats in dict_stats_basic_position.values()]
            match_comp_dfs = [dict_stats["match_comp"] for dict_stats in dict_stats_basic_position.values()]
            
            final_avg_dfs = create_unique_df(avg_dfs)
            final_match_comp_dfs = create_unique_df(match_comp_dfs)            
            
            avg_speceific_dfs_alias = avg_specific.withColumnRenamed("total_score", "avg_specific_score").alias("avg_specific")
            df_avg_alias = final_avg_dfs.withColumnRenamed("total_score", "avg_score").alias("avg")
            df_match_comp_alias = final_match_comp_dfs.withColumnRenamed("total_score", "match_comp_score").alias("match_comp")
            df_goals_assists_alias = spark_df_score_goals_and_assists.withColumnRenamed("score", "goals_assists_score").alias("goals_assists")
            df_visitant_win_lose_alias = spark_df_visitant_win_lose.withColumnRenamed("score", "visitant_win_lose_score").alias("visitant_win_lose")
                 
            df_combined = avg_speceific_dfs_alias \
                .join(df_avg_alias, ["player_id", "basic_position_id"], "inner") \
                .join(df_match_comp_alias, ["player_id", "basic_position_id"], "inner") \
                .join(df_goals_assists_alias, ["player_id"], "inner") \
                .join(df_visitant_win_lose_alias, ["player_id"], "inner")

            
            # Ahora podemos calcular el score final
            df_combined = df_combined.withColumn(
                "score", 
                (F.col("avg_specific_score") * 0.7) + 
                (F.col("avg_score") * 0.20) + 
                (F.col("match_comp_score") * 0.10) + 
                (F.col("goals_assists_score")) + (F.col("visitant_win_lose_score"))
            ).select("player_id", "basic_position_id", "specific_position_id", "game_mode_id", "score")
            
            specific_positon.append(df_combined)
        
        if len(specific_positon) > 0:
            
            union_df = create_unique_df(specific_positon)
            dict_stats_type_of_play_scored[game_mode] = union_df
    
    
    return dict_stats_type_of_play_scored
    
     
    