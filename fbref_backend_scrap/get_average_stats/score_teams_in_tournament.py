
"""
    En este fichero se define la funcion score_teamns_inÇ_tournament, que se encarga de calcular la media segun las puntuaciones de los jugadores en los aprtidos jugados en el torneo    
"""

import pandas as pd
from pyspark.sql.functions import col
from pyspark.sql.types import StructType
from simple_functions.functions import fill_stats_dict, introduce_in_data
from get_average_stats.spark_average_teams_schema import get_teams_average_spark_schema, get_teams_average_spark_schema_by_positions_field_player_and_team, get_teams_average_spark_schema_by_positions_gk
from functions_to_stract_of_dataBase.selects_of_positions import query_to_get_specific_position, query_to_select_all_positions_category
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_match_of_tournaments, get_teams_in_competition
from get_average_stats.fbref_get_average_stats_by_specific_position import check_if_avg_teams_stats_of_league_exists, check_if_avg_teams_stats_of_league_exists_by_basic_position, init_dicts_specific_teams, loop_throgh_all_columns_avg, query_to_get_basic_positions_stats_with_teams, query_to_get_stats_by_position, query_to_get_stats_with_team
from constants import table_dic_to_insert
from write_dataframe_to_mysql_file import write_dataframe_to_mysql


def get_teams_average_of_5_leagues(spark, jdbc_url, db_properties):
    print('Getting average of 5 leagues...')
    spark_data = get_match_of_tournaments(spark, jdbc_url, db_properties)
    returning_value = pd.DataFrame()
    # Filtar solo La Liga
    league_df = spark_data.filter(col('nombre_liga') == "La Liga")
    print(league_df.show())
    try:
        for row in league_df.collect():
            
            season_id = row["season_tournament_id"]
            season_year = row["season_year"]
            tournament_id = row["tournament_id"]
            tournament_name = row["nombre_liga"]
            tournament_name = tournament_name.replace(' ', '-')
            tournament_fbref_id = row["tournament_fbref_id"]
            type_of_competition = row["type_of_competition"]
            
            if tournament_id == 130 or tournament_id == 128:
                continue

            url = f'https://fbref.com/en/comps/{tournament_fbref_id}/{season_year}/schedule/{season_year}-{tournament_name}-Scores-and-Fixtures'
            
            teams_on_competition_df = get_teams_in_competition(spark, jdbc_url, db_properties, row["tournament_id"])
            
      
            for teams in teams_on_competition_df.collect():
                team_id = teams["team_id"]
                print(f"Team ID: {team_id}")
                
                
                df = get_teams_average_of_competitions(spark, jdbc_url, db_properties, row["tournament_id"], team_id)
                if df.isEmpty():
                    continue

                
                print("")
                print("")
                
                df_basic = get_teams_stats_avg_devs_tip_for_competition_by_players_position(spark, jdbc_url, db_properties, row["tournament_id"], team_id)
                if df_basic.isEmpty():
                    continue
            
            
            print(url)
            
    except Exception as e:
        print(f"Error: {e}")
        returning_value = pd.DataFrame()
    
    return returning_value
 

 
 
def get_teams_average_of_competitions(spark, jdbc_url, db_properties, league_id, team_id):
    print('Getting average of competitions...')
    
    success = spark.createDataFrame([], StructType([]))
    try:
        if check_if_avg_teams_stats_of_league_exists(spark, jdbc_url, db_properties, league_id, team_id):
            print("Ya existen las estadísticas medias de la liga")
            success = spark.createDataFrame([("Repetido",)], ["Correcto"])
        else :
            dict_val_columns_average_stats_more = {"league_id": league_id, "starter_status": "starter", "team_id": team_id}
            dict_val_columns_average_stats_less = {"league_id": league_id, "starter_status": "substitute", "team_id": team_id}

            
            for num_tabla in table_dic_to_insert:
                table_name = table_dic_to_insert[num_tabla]

                if table_name == "stats_shots_summary":
                    continue
                
                if table_name == "stats_gk_summary":
                    spark_df_more_70, spark_df_less_70 = query_to_get_stats_with_team(spark, jdbc_url, db_properties, league_id, table_name, "GK", team_id)
                else:
                    spark_df_more_70, spark_df_less_70 = query_to_get_stats_with_team(spark, jdbc_url, db_properties, league_id, table_name, "Field", team_id)

                number_of_rows_more_70 = spark_df_more_70.count()
                number_of_rows_less_70 = spark_df_less_70.count()
                expected_columns = spark_df_more_70.columns

                if number_of_rows_more_70 > 0:
                    dict_val_columns_average_stats_more.update(loop_throgh_all_columns_avg(spark_df_more_70, number_of_rows_more_70))
                else:
                    for col in expected_columns:
                        if col not in dict_val_columns_average_stats_more:
                            dict_val_columns_average_stats_more[col] = 0.0
                
                if number_of_rows_less_70 > 0:
                    dict_val_columns_average_stats_less.update(loop_throgh_all_columns_avg(spark_df_less_70, number_of_rows_less_70))
                else:
                    for col in expected_columns:
                        if col not in dict_val_columns_average_stats_less:
                            dict_val_columns_average_stats_less[col] = 0.0  

                print("Table: ", table_name, "added to the dictionary")

            data = [tuple(dict_val_columns_average_stats_more.values()),
                    tuple(dict_val_columns_average_stats_less.values())]
        
            schema = get_teams_average_spark_schema()
            
            df = spark.createDataFrame(data, schema)
            
            write_dataframe_to_mysql(df, jdbc_url, db_properties, "avg_teams_stats")
            print("Average stats of the tables completed totalled by the league")
            success = spark.createDataFrame([("Correcto",)], ["Correcto"])
            
    except Exception as e:
        print(f"Error: {e}")
        success = spark.createDataFrame([("Error",)], ["Error"])
    
    return success




def get_teams_stats_avg_devs_tip_for_competition_by_players_position(spark, jdbc_url, db_properties, league_id, team_id):
    print("Getting stats for competition by players position...")
    
    returning_value = spark.createDataFrame([], StructType([]))
    
    try:
        type_schema = None
        boolean_gk = False
        spark_position_categories = query_to_select_all_positions_category(spark, jdbc_url, db_properties)
        print("Las posiciones son: ", spark_position_categories.show())
        data = []
        gk_data = []
        # Recorremos las posiciones
        for position in spark_position_categories.collect():
            print("Position: ", position.category_id, " - ", league_id)
            
            if check_if_avg_teams_stats_of_league_exists_by_basic_position(spark, jdbc_url, db_properties, league_id, position.category_id, team_id):
                print("Ya existen las estadísticas medias de la liga para la posición", position.category_id)
                continue
            
            specific_positions_list = query_to_get_specific_position(spark, jdbc_url, db_properties, position)

            if any(row.position_id == 47 for row in specific_positions_list):
                boolean_gk = False
                type_schema = get_teams_average_spark_schema_by_positions_gk()
            else:
                boolean_gk = True
                type_schema = get_teams_average_spark_schema_by_positions_field_player_and_team()


            dict_val_columns, dict_val_desv_columns, dict_val_mode_columns = init_dicts_specific_teams(league_id, position.category_id, "starter", team_id)
            dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less = init_dicts_specific_teams(league_id, position.category_id, "substitute", team_id)

            for num_tabla in table_dic_to_insert:
                table_name = table_dic_to_insert[num_tabla]

                if table_name == "stats_shots_summary" or (boolean_gk and table_name == "stats_gk_summary"):
                    continue
            
                spark_df_more_70, spark_df_less_70 = query_to_get_basic_positions_stats_with_teams(spark, jdbc_url, db_properties, league_id, specific_positions_list, table_name, team_id)
                    
                expected_columns = spark_df_more_70.columns

                
                fill_stats_dict(spark_df_more_70, expected_columns, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns, table_name)
                fill_stats_dict(spark_df_less_70, expected_columns, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less, table_name)
                                 
                print("Table: ", table_name, "added to the dictionary")
            # Comprobar longitus, ya que no entra en este if FACIL
            if (len(dict_val_columns) == len(type_schema)) and (len(dict_val_desv_columns) == len(type_schema)) and (len(dict_val_columns_less) == len(type_schema)) and (len(dict_val_desv_columns_less) == len(type_schema)):                  
                    
                if position.category_id != 1:
                    introduce_in_data(data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                    introduce_in_data(data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)         

                else:
                    introduce_in_data(gk_data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                    introduce_in_data(gk_data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)
            else:
                print("Error: Las longitudes no coinciden")
                print("Longitud de dict_val_columns:", len(dict_val_columns))
                print("Longitud de type_schema:", len(type_schema))
                print("Longitud de dict_val_desv_columns:", len(dict_val_desv_columns))
                print("Longitud de dict_val_columns_less:", len(dict_val_columns_less))
                print("Longitud de dict_val_desv_columns_less:", len(dict_val_desv_columns_less))
                print("Longitud de type_schema:", len(type_schema))
                
                returning_value = spark.createDataFrame([], StructType([]))
                return returning_value
                
                
        spark_dfs = []
        if data:
            
            df_data = spark.createDataFrame(data, get_teams_average_spark_schema_by_positions_field_player_and_team())
            spark_dfs.append(df_data)
            

        if gk_data:
            df_gk_data = spark.createDataFrame(gk_data, get_teams_average_spark_schema_by_positions_gk())
            spark_dfs.append(df_gk_data)
            
        for df in spark_dfs:
            write_dataframe_to_mysql(df, jdbc_url, db_properties, "avg_teams_stats_by_basic_positions")
      
        print("Average stats of the tables completed")
        returning_value = spark.createDataFrame([{"Resultado": "Correcto"}])
        

    except Exception as e:
        print(f"Error: {e}")
        return spark.createDataFrame([], StructType([]))
        
    return returning_value
