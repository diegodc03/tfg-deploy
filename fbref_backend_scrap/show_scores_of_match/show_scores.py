

from w_read_dataframe_to_mysql_file import read_data_with_spark

from functions_to_stract_of_dataBase.selects_of_positions import get_all_game_modes
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_result_of_match
from functions_to_stract_of_dataBase.querys_score_match import get_scores_by_type_of_game_mode

def show_scores_of_match(spark, jdbc_url, db_properties, match_id, league_id):
    
    spark_game_modes = get_all_game_modes(spark, jdbc_url, db_properties)   
    list_of_game_modes = spark_game_modes.select("game_mode_id", "game_mode_name").distinct().collect()
    
    
    # Get the result of the match
    result_df = get_result_of_match(spark, jdbc_url, db_properties, match_id)
    #result_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    if not result_df:
        print("No se ha podido obtener el resultado del partido")
        
    else:
        
        print("Que tipo de puntuacion quiere ver?")
        for game_mode in list_of_game_modes:
            print(f"{game_mode['game_mode_id']}: {game_mode['game_mode_name']}")
        
        input_game_mode = int(input("Introduce el id del modo de juego: "))
        
        if input_game_mode not in [game_mode["game_mode_id"] for game_mode in list_of_game_modes]:
            print("El modo de juego no existe")
            return
        
        spark = get_scores_by_type_of_game_mode(spark, jdbc_url, db_properties, match_id, input_game_mode, league_id)
        print(spark.show())



    
    
    
