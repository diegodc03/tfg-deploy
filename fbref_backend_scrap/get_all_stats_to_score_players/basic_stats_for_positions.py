


from pyspark.sql.functions import lit
from dataBase.avg_select_by_positions import  dict_positions_avg
from dataBase.selects_of_stats_by_position import dict_stats_position
from functions_to_stract_of_dataBase.querys_score_match import get_number_of_scores_by_type_of_game_mode_and_basic_position_id
from functions_to_stract_of_dataBase.selects_of_positions import query_to_select_all_positions_category
from get_all_stats_to_score_players.score_elements import calculate_player_scores_by_avg_of_season, get_score_for_positions_with_only_match_stats
from w_read_dataframe_to_mysql_file import read_data_with_spark



def get_position_id_of_basic_positions(position_name):

    query = f"""
        SELECT category_id FROM position_category WHERE category_name = '{position_name}'
    """
    return query


def get_result_of_match(spark, jdbc_url, db_properties, match_id):
    query = f"""
        SELECT fm.Score, fm.Home, fm.Away FROM football_match fm WHERE match_id = {match_id}
    """
    return query



def get_stats_by_position(spark, jdbc_url, db_properties, match_id, league_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por posición")

    # Puedo hacerlo en una unica funcion, solo tengo que mandarle el string de forwards, midfielders, defenders y goalkeepers, si hago un diccionario con las posiciones y las funciones, puedo hacerlo en un for
    spark_positions = query_to_select_all_positions_category(spark, jdbc_url, db_properties)

    dict_stats_position = {}

    for position in spark_positions.collect():
        position_name = position["category_name"]
        position_id = position["category_id"]
        
        
        avg, comp_match = get_stats_basic_position(spark, jdbc_url, db_properties, match_id, league_id, position_name, position_id)
        if avg is None or comp_match is None:
            print("No hay jugadores en la posicion", position_name)
            continue
        dict_stats_position[position_name] = {"avg": avg, "match_comp": comp_match}
 
    return dict_stats_position


def get_stats_basic_position(spark, jdbc_url, db_properties, match_id, league_id, position_name, position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por posición,", position_name)

    query = dict_stats_position[position_name](match_id, league_id, position_id)
    players_df = read_data_with_spark(spark, jdbc_url, db_properties, query)

    if players_df is not None and players_df.count() > 0:

        # Calcula comparacion de los jugadores del partido
        score_comparison_with_players_of_match = get_score_for_positions_with_only_match_stats(players_df)
        if score_comparison_with_players_of_match.isEmpty():
            print("No hay jugadores en el partido")
            return None, None
  
        query_avg = dict_positions_avg[position_name](league_id, position_id)
        query_stats = read_data_with_spark(spark, jdbc_url, db_properties, query_avg)    

        # Calcula en comparacion de la media de la liga
        score_comparison_with_league_avg = calculate_player_scores_by_avg_of_season(players_df, query_stats)
        if score_comparison_with_league_avg.count() == 0:
            print("No hay jugadores en la liga")
            return None, None

        score_comparison_with_league_avg = add_position_id_to_df(score_comparison_with_league_avg, position_id)
        score_comparison_with_players_of_match = add_position_id_to_df(score_comparison_with_players_of_match, position_id)
        
        return score_comparison_with_league_avg, score_comparison_with_players_of_match

    else:
        print("No hay jugadores en la posicion", position_name)
        return None, None
        
        
def add_position_id_to_df(df, position_id):
    df = df.withColumn("basic_position_id", lit(position_id))
    return df



