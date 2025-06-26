########  IMPORTS  ######### 

from functions_to_stract_of_dataBase.querys_score_match import get_number_of_scores_by_type_of_game_mode_and_specific_position_id
from get_all_stats_to_score_players.score_elements import calculate_player_scores_by_avg_of_season, get_score_for_positions_with_only_match_stats
from fbref_backend_scrap.utils.read_dataframe_to_mysql_file import read_data_with_spark
from dataBase.functions.registry import FUNCTION_REGISTRY
from pyspark.sql.functions import lit
from functions_to_stract_of_dataBase.selects_of_positions import get_all_game_modes, get_all_positions_by_specific_position, get_specific_basic_positions_id





##################################################################################################################
########################################  CENTRAL FUNCTION  ######################################################
##################################################################################################################
    
     
def get_stats_by_type_of_play_form(spark, jdbc_url, db_properties, match_id, league_id):
    print("Comienzo recogiendo las estadísticas de los jugadores por tipo de juego")

    dict_stats_game_mode = {}
    
    # Cogiendo los tipos de positiones
    game_modes_df = get_all_game_modes(spark, jdbc_url, db_properties)
    type_of_positions_df = get_all_positions_by_specific_position(spark, jdbc_url, db_properties)
    relation_basic_specific_df = get_specific_basic_positions_id(spark, jdbc_url, db_properties)
    
    type_of_positions_df = type_of_positions_df.filter(~type_of_positions_df["specific_position_name"].contains("no_existencia"))
    game_modes_df = game_modes_df.filter(~game_modes_df["game_mode_name"].contains("no_existencia"))

    # Hacemos un for para cada una de las posiciones y tipos de juego, de esta manera podemos hacer un for para cada una de las posiciones y tipos de juego
    for game_mode in game_modes_df.collect():
        
        print("Estamos en el modo de juego ", game_mode["game_mode_name"])
        dict_stats_position = {}
        
        if game_mode["game_mode_name"] == "no_existencia":
            continue
        
        
        for position in type_of_positions_df.collect():
            print("Estamos en la posicion ", position["specific_position_name"])
            
            if position["specific_position_name"] == "no_existencia":
                continue
            
            game_mode_id = game_mode["game_mode_id"]
            game_mode_name = game_mode["game_mode_name"]
            type_of_game_name = game_mode["type_of_game_name"]
            
            specific_position_id = position["specific_position_id"]
            specific_position_name = position["specific_position_name"]
            
            # Comprobamos si existe en la base de datos la posicion y el modo de juego ya introducis para ese partido
            number_of_rows = get_number_of_scores_by_type_of_game_mode_and_specific_position_id(spark, jdbc_url, db_properties, match_id, game_mode_id, specific_position_id)
            if number_of_rows > 0:
                print("Ya existe las puntuaciones para el modo de juego y la posicion")
                continue
             
            function_name = FUNCTION_REGISTRY.get((type_of_game_name, specific_position_name, game_mode_name))
            
            basic_position_id = relation_basic_specific_df.filter(relation_basic_specific_df["stat_specific"] == specific_position_id).select("stat_basic").first()["stat_basic"]
                
            if function_name and isinstance(function_name, tuple):

                match_func, avg_func = function_name
                    
                query_match = match_func(match_id, league_id, specific_position_id)
                query_avg = avg_func(league_id, specific_position_id)
                  
                match_players_by_specific_position_df = read_data_with_spark(spark, jdbc_url, db_properties, query_match)
                avg_by_specific_position_df = read_data_with_spark(spark, jdbc_url, db_properties, query_avg)
                    
                if match_players_by_specific_position_df.count() == 0 or avg_by_specific_position_df.count() == 0:
                    print("No hay jugadores en el partido con la posicion ", specific_position_name)
                    continue
                    
                match_comparison = get_score_for_positions_with_only_match_stats(match_players_by_specific_position_df)    
                if match_comparison.isEmpty():
                    print("No hay jugadores en el partido con la posicion ", specific_position_name)
                    continue
                avg_comparison = calculate_player_scores_by_avg_of_season(match_players_by_specific_position_df, avg_by_specific_position_df)
                if avg_comparison.count() == 0:
                        print("No hay jugadores en la liga con la posicion ", specific_position_name)
                        continue     
                        
                match_comparison = match_comparison.withColumn("specific_position_id", lit(specific_position_id)).withColumn("basic_position_id", lit(basic_position_id)).withColumn("game_mode_id", lit(game_mode_id))
                avg_comparison = avg_comparison.withColumn("specific_position_id", lit(specific_position_id)).withColumn("basic_position_id", lit(basic_position_id)).withColumn("game_mode_id", lit(game_mode_id))
                        
                dict_stats_position[specific_position_name] = {"avg": avg_comparison, "match_comp": match_comparison}
        
        dict_stats_game_mode[game_mode_name] = dict_stats_position    
        print ("El modo de juego es ", game_mode_name)
        print ("El diccionario de posiciones es ", dict_stats_position)            
                
    print("\n\n")
    print("\n\n")
                 
    
    return dict_stats_game_mode               
        
        
  