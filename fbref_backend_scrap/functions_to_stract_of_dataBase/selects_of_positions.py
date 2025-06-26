#################################################################################
# This script contains functions to extract data from the database.
# Game modes - position_specifics_by_category - basic_specific_positions_relation

from fbref_backend_scrap.utils.read_dataframe_to_mysql_file import read_data_with_spark





###################################################################################
# Tables to join: game_modes, type_of_game
# 
# Columns to select: game_mode_id, game_mode_name, type_of_game_name
#
#################################################################################



def get_all_game_modes(spark, jdbc_url, db_properties):
    
    query = f"""
        SELECT gm.game_mode_id, gm.game_mode_name, tog.type_of_game_name FROM game_modes gm JOIN type_of_game tog ON gm.type_of_game_id = tog.type_of_game_id
    """
    
    spark_df = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_df



   
   
####################################################################################
# Tables to join: positions_specifics_by_category, position_on_the_field
#
# Columns to select: specific_position_id, specific_position_name, position_id, position_name
#
####################################################################################
def get_all_positions_by_specific_position(spark, jdbc_url, db_properties):
    
    query = f"""
        SELECT 
            psc.specific_position_id, psc.specific_position_name, 
        
            GROUP_CONCAT(pof.position_name ORDER BY pof.position_name SEPARATOR ', ') AS grouped_positions,
            GROUP_CONCAT(pof.position_id ORDER BY pof.position_name SEPARATOR ', ') AS grouped_positions_id
        FROM positions_specifics_by_category psc
        LEFT JOIN position_on_the_field pof 
            ON psc.specific_position_id = pof.specific_position_id
        GROUP BY psc.specific_position_id, psc.specific_position_name
    """
    spark_df = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_df


####################################################################################
# Tables to join: basic_specific_positions_relation
#
# Columns to select: basic_position_id, specific_position_id
#
####################################################################################
def get_specific_basic_positions_id(spark, jdbc_url, db_properties):
    query = f"""
        SELECT bspr.basic_position_id AS stat_basic, bspr.specific_position_id AS stat_specific FROM basic_specific_positions_relation bspr
    """
    spark_df = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_df




#####################################################################################
# Tables to join: positions_specifics_by_category, game_modes
# Columns to select: specific_position_id, game_mode_id
#
#####################################################################################
def get_id_of_specific_and_game_id_when_not_exists(spark, jdbc_url, db_properties, type_of_not_exists_columns):
        NO_EXISTS = "no_existencia"
        
        if type_of_not_exists_columns == "specific_position_id":
            query = f"""
                SELECT specific_position_id FROM positions_specifics_by_category WHERE specific_position_name = '{NO_EXISTS}'
            """
        elif type_of_not_exists_columns == "game_mode_id":
            query = f"""
                SELECT game_mode_id FROM game_modes WHERE game_mode_name = '{NO_EXISTS}'
            """
       
        spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
        
        return spark_df
    
    
    

def query_to_select_all_positions_category(spark, jdbc_url, db_properties):

    query = "SELECT category_id, category_name FROM position_category"
    
    spark_positions = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_positions


def query_to_get_specific_position(spark, jdbc_url, db_properties, position):
    
    query = f"SELECT * FROM position_category_relation WHERE category_id = {position.category_id}"
    spark_df = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_df.collect()


def query_to_get_all_specific_positions(spark, jdbc_url, db_properties):
    
    query = f"""SELECT specific_position_id, specific_position_name FROM positions_specifics_by_category"""

    spark_df = read_data_with_spark(
        spark, jdbc_url, db_properties, query
    )
    return spark_df




