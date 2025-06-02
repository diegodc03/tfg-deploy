

from pyspark.sql import functions as F
import pandas as pd
from pyspark.sql.functions import col
from pyspark.sql.types import StructType

from constants import table_dic_to_insert

from simple_functions.functions import fill_stats_dict, introduce_in_data
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_match_of_tournaments
from functions_to_stract_of_dataBase.selects_of_positions import query_to_get_all_specific_positions, query_to_get_specific_position, query_to_select_all_positions_category
from get_average_stats.fbref_get_average_stats_by_specific_position import check_if_avg_stats_of_league_exists, check_if_avg_stats_of_league_exists_by_basic_position, init_dicts_specific, loop_throgh_all_columns_avg, loop_throgh_all_columns_basic_positions, query_to_get_stats, query_to_get_stats_by_position, query_to_get_stats_by_specific_position
from get_average_stats.spark_average_schema import get_average_spark_schema, get_average_spark_schema_by_positions_field_player, get_average_spark_schema_by_positions_gk
from write_dataframe_to_mysql_file import write_dataframe_to_mysql



def get_average_of_5_leagues(spark, jdbc_url, db_properties):
    print('Getting average of 5 leagues...')
    spark_data = get_match_of_tournaments(spark, jdbc_url, db_properties)
    
    returning_value = spark.createDataFrame([], StructType([]))
    
    # Filtar solo La Liga
    league_df = spark_data.filter(col('nombre_liga') == "La Liga")
    print(league_df.show())
    try:
        for row in league_df.collect():
            if row["tournament_id"] == 128:

                season_id = row["season_tournament_id"]
                season_year = row["season_year"]
                tournament_id = row["tournament_id"]
                tournament_name = row["nombre_liga"]
                tournament_name = tournament_name.replace(' ', '-')
                tournament_fbref_id = row["tournament_fbref_id"]
                type_of_competition = row["type_of_competition"]

                url = f'https://fbref.com/en/comps/{tournament_fbref_id}/{season_year}/schedule/{season_year}-{tournament_name}-Scores-and-Fixtures'
                
                df = get_average_of_competitions(spark, jdbc_url, db_properties, row["tournament_id"])
                print(df.show())
                if df.filter(col("Correcto") == "Error").count() > 0:   
                    continue
                elif df.filter(col("Correcto") == "Ya existe").count() > 0:
                    break
                
                print("")
                print("")
                df_basic = get_stats_avg_devs_tip_for_competition_by_players_position(spark, jdbc_url, db_properties, row["tournament_id"])
                if df_basic.isEmpty():
                    continue
                
                print("")
                print("")
                specific_df = get_stats_avg_devs_tip_for_competition_by_players_specific_position(spark, jdbc_url, db_properties, row["tournament_id"])
                if specific_df.isEmpty():
                    continue
                
                print(url)
                break
        returning_value = pd.DataFrame([{"Resultado": "Correcto"}])
    except Exception as e:
        print(f"Error: {e}")
        returning_value = spark.createDataFrame([], StructType([]))
    
    return returning_value
 
 
 
 


# Cambiar y tener dos tablas para cada liga, uno de jugadores, y otro unicamente de jugadores de campo, asegurandonos que asi sean estadísticas más reales
def get_average_of_competitions(spark, jdbc_url, db_properties, league_id):
    print('Getting average of competitions...')
    
    success = spark.createDataFrame([], StructType([]))
    try:
        if check_if_avg_stats_of_league_exists(spark, jdbc_url, db_properties, league_id):
            print("Ya existen las estadísticas medias de la liga")
            success = spark.createDataFrame([("Correcto",)], ["Ya existe"])
        else :
            dict_val_columns_average_stats_more = {"league_id": league_id, "starter_status": "starter"}
            dict_val_columns_average_stats_less = {"league_id": league_id, "starter_status": "substitute"}

            
            for num_tabla in table_dic_to_insert:
                table_name = table_dic_to_insert[num_tabla]

                if table_name == "stats_shots_summary":
                    continue
                
                if table_name == "stats_gk_summary":
                    spark_df_more_70, spark_df_less_70 = query_to_get_stats(spark, jdbc_url, db_properties, league_id, table_name, "GK")
                else:
                    spark_df_more_70, spark_df_less_70 = query_to_get_stats(spark, jdbc_url, db_properties, league_id, table_name, "Field")

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
        
            schema = get_average_spark_schema()
            
            df = spark.createDataFrame(data, schema)
            
            write_dataframe_to_mysql(df, jdbc_url, db_properties, "avg_player_stats")
            print("Average stats of the tables completed totalled by the league")
            success = spark.createDataFrame([("Correcto",)], ["Correcto"])
            
    except Exception as e:
        print(f"Error: {e}")
        success = spark.createDataFrame([("Error",)], ["Error"])
    
    return success




# Hay qyue mejorarlo, ya que se puede implementar para que mire cual esta hecho y cual no

def get_stats_avg_devs_tip_for_competition_by_players_position(spark, jdbc_url, db_properties, league_id):
    print("Getting stats for competition by players position...")
    
    returning_value = spark.createDataFrame([], StructType([]))
    
    try:
        type_schema = None
        boolean_gk = False
        spark_position_categories = query_to_select_all_positions_category(spark, jdbc_url, db_properties)
        data = []
        gk_data = []
        # Recorremos las posiciones
        for position in spark_position_categories.collect():
            print("Position: ", position.category_id, " - ", league_id)
            
            if check_if_avg_stats_of_league_exists_by_basic_position(spark, jdbc_url, db_properties, league_id, position.category_id):
                print("Ya existen las estadísticas medias de la liga para la posición", position.category_id)
                continue
            
            specific_positions_list = query_to_get_specific_position(spark, jdbc_url, db_properties, position)

            if any(row.position_id == 47 for row in specific_positions_list):
                boolean_gk = False
                type_schema = get_average_spark_schema_by_positions_gk()
            else:
                boolean_gk = True
                type_schema = get_average_spark_schema_by_positions_field_player()


            dict_val_columns, dict_val_desv_columns, dict_val_mode_columns = init_dicts_specific(league_id, position.category_id, "starter")
            dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less = init_dicts_specific(league_id, position.category_id, "substitute")

            for num_tabla in table_dic_to_insert:
                table_name = table_dic_to_insert[num_tabla]

                if table_name == "stats_shots_summary" or (boolean_gk and table_name == "stats_gk_summary"):
                    continue
            
                spark_df_more_70, spark_df_less_70 = query_to_get_stats_by_position(spark, jdbc_url, db_properties, league_id, specific_positions_list, table_name)
                    
                expected_columns = spark_df_more_70.columns

                
                fill_stats_dict(spark_df_more_70, expected_columns, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns, table_name)
                fill_stats_dict(spark_df_less_70, expected_columns, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less, table_name)
                
                                           
                print("Table: ", table_name, "added to the dictionary")
        
            if (len(dict_val_columns) == len(type_schema)) and (len(dict_val_desv_columns) == len(type_schema)) and (len(dict_val_columns_less) == len(type_schema)) and (len(dict_val_desv_columns_less) == len(type_schema)):                  
                    
                if position.category_id != 1:
                    introduce_in_data(data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                    introduce_in_data(data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)         

                else:
                    introduce_in_data(gk_data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                    introduce_in_data(gk_data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)
            
        spark_dfs = []
        if data:
            df_data = spark.createDataFrame(data, get_average_spark_schema_by_positions_field_player())
            spark_dfs.append(df_data)

        if gk_data:
            df_gk_data = spark.createDataFrame(gk_data, get_average_spark_schema_by_positions_gk())
            spark_dfs.append(df_gk_data)
            
        for df in spark_dfs:
            write_dataframe_to_mysql(df, jdbc_url, db_properties, "avg_player_stats_by_basic_positions")

                
        print("Average stats of the tables completed")
        returning_value = spark.createDataFrame([{"Resultado": "Correcto"}])
        

    except Exception as e:
        print(f"Error: {e}")
        return spark.createDataFrame([], StructType([]))
        
    return returning_value

def query_to_get_positions_of_specific_positions(spark, jdbc_url, db_properties, position):
    query = f"""
        SELECT position_id, position_name FROM position_on_the_field WHERE specific_position_id = {position}
    """
    spark_df = spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as positions",
        properties=db_properties
    )
    return spark_df



def get_stats_avg_devs_tip_for_competition_by_players_specific_position(spark, jdbc_url, db_properties, league_id):
    print("Getting stats for competition by specific players position...")
    GOALKEEPER = "goalkeeper"
    returning_value = spark.createDataFrame([], StructType([]))
    try:
        type_schema = 0
        boolean_gk = False

        # Return values of statistics of calculated positions
        spark_position_categories = query_to_get_all_specific_positions(spark, jdbc_url, db_properties)
        
        data = []
        gk_data = []
        for position_row in spark_position_categories.collect():
            
            especific_position = position_row.specific_position_id
            print("Position: ", position_row.specific_position_id)
            
            if check_if_avg_stats_of_league_exists(spark, jdbc_url, db_properties, league_id, especific_position):
                print("Ya existen las estadísticas medias de la liga para la posición", especific_position)
                continue
            
            # Cogemos las posiciones especificas de la posicion
            positions_list = query_to_get_positions_of_specific_positions(spark, jdbc_url, db_properties, especific_position)
            
            positions_ids = [row.position_id for row in positions_list.collect()]
            print("Positions: ", positions_ids)
            
            if position_row.specific_position_name == GOALKEEPER:
                boolean_gk = False
                type_schema = get_average_spark_schema_by_positions_gk()
            else:
                boolean_gk = True
                type_schema = get_average_spark_schema_by_positions_field_player()

            dict_val_columns, dict_val_desv_columns, dict_val_mode_columns = init_dicts_specific(league_id, especific_position, "starter")
            dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less = init_dicts_specific(league_id, especific_position, "substitute")

                
            for num_tabla in table_dic_to_insert:
                table_name = table_dic_to_insert[num_tabla]

                if table_name == "stats_shots_summary" or (boolean_gk and table_name == "stats_gk_summary"):
                    continue
            
                spark_df_more_70, spark_df_less_70 = query_to_get_stats_by_specific_position(spark, jdbc_url, db_properties, league_id, positions_ids, table_name)
                
                expected_columns = spark_df_more_70.columns
                  
                fill_stats_dict(spark_df_more_70, expected_columns, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns, table_name)
                fill_stats_dict(spark_df_less_70, expected_columns, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less, table_name)
                                                          
                print("Table: ", table_name, "added to the dictionary")       
                
                if (len(dict_val_columns) == len(type_schema)) and (len(dict_val_desv_columns) == len(type_schema)) and (len(dict_val_columns_less) == len(type_schema)) and (len(dict_val_desv_columns_less) == len(type_schema)) and (len(dict_val_mode_columns) == len(type_schema)) and (len(dict_val_mode_columns_less) == len(type_schema)):                
                    
                    if position_row.specific_position_name != GOALKEEPER:
                        
                        introduce_in_data(data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                        introduce_in_data(data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)
                                        
                    else:
                        
                        introduce_in_data(gk_data, dict_val_columns, dict_val_desv_columns, dict_val_mode_columns)
                        introduce_in_data(gk_data, dict_val_columns_less, dict_val_desv_columns_less, dict_val_mode_columns_less)


        spark_dfs = []
        if data:
            df_data = spark.createDataFrame(data, get_average_spark_schema_by_positions_field_player())
            spark_dfs.append(df_data)

        if gk_data:
            df_gk_data = spark.createDataFrame(gk_data, get_average_spark_schema_by_positions_gk())
            spark_dfs.append(df_gk_data)
        
        for df in spark_dfs:
            write_dataframe_to_mysql(df, jdbc_url, db_properties, "avg_player_stats_by_specific_positions")
        
            
        print("Average stats of the tables completed")
        returning_value = spark.createDataFrame([{"Resultado": "Correcto"}])

    except Exception as e:
        print(f"Error en funcion `get_stats_avg_devs_tip_for_competition_by_players_specific_position`: {e}")
        returning_value = spark.createDataFrame([], StructType([]))
    
    return returning_value
    




def calculate_mode(spark_df, column_name):
    mode_dict = {}
    for col in column_name:
        try:
            mode_val = spark_df.groupBy(col).count().orderBy(F.desc("count")).first()
            if mode_val:
                mode_dict[col] = mode_val[0]
            else:
                mode_dict[col] = None
        except:
            mode_dict[col] = None
    return mode_dict



 
