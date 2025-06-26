


from pyspark.sql import functions as F
from pyspark.sql.functions import col, sum
import numpy as np
from fbref_backend_scrap.utils.read_dataframe_to_mysql_file import read_data_with_spark


valid_type_of_stat_values = ['avg', 'max', 'min', 'desv', 'mode', 'sum']
status_starter_player = ['starter', 'substitute']
UMBRAL_DISPERSION = 4





def query_to_get_stats(spark, jdbc_url, db_properties, league_id, table_name, position_name):
    
    # Base query con los joins
    base_query = f"""
        SELECT { "ms.goals, ms.assists," if table_name == "stats_summary" else "" } 
               tn.*, 
               CASE WHEN ms.minutes > 70 THEN 'more' ELSE 'less' END AS minutes_category
        FROM {table_name} tn 
        JOIN match_statistics ms ON tn.stat_id = ms.estadistica_id 
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN position_player pp ON ms.player_id = pp.player_id AND ms.match_id = pp.match_id
        JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        WHERE fm.Season = {league_id}
    """

    # Filtro según la posición
    if position_name == "GK":
        query = base_query + " AND pof.position_name = 'GK'"
    elif position_name == "Field":
        query = base_query + " AND pof.position_name != 'GK'"
    else:
        raise ValueError("position_name debe ser 'GK' o 'Field'")

    spark_df = spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as {table_name}",
        properties=db_properties
    )

    df_more_than_70 = spark_df.filter(col("minutes_category") == "more").drop("minutes_category", "estatistic_id", "stat_id", "player_id")
    df_less_than_70 = spark_df.filter(col("minutes_category") == "less").drop("minutes_category", "estatistic_id", "stat_id", "player_id")

    return df_more_than_70, df_less_than_70





def check_if_avg_stats_of_league_exists(spark, jdbc_url, db_properties, league_id):
    query = f"SELECT * FROM avg_player_stats WHERE league_id = {league_id}"
    spark_df = spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as avg_player_stats",
        properties=db_properties
    )
    return True if spark_df.count() > 0 else False


def check_if_avg_teams_stats_of_league_exists(spark, jdbc_url, db_properties, league_id, team_id):
    query = f"SELECT * FROM avg_teams_stats WHERE league_id = {league_id} and team_id = {team_id}"
    spark_df = spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as avg_teams_stats",
        properties=db_properties
    )
    return True if spark_df.count() > 0 else False


def loop_throgh_all_columns_avg(spark_df, number_of_rows):
    dict_val_columns_average_stats = {}
    for column in spark_df.columns:
        if (column == 'player_id' or column == 'estatistic_id' or column == 'stat_id') or (spark_df.filter(col(column).isNull()).count() > 0):
            continue
        
        sum_column = spark_df.select(sum(column)).collect()[0][0]
        average_column = sum_column / number_of_rows
        
        dict_val_columns_average_stats[column] = average_column
        
    return dict_val_columns_average_stats


def query_to_get_stats_by_position(spark, jdbc_url, db_properties, league_id, positions, table_name):
    
    position_list_sql = ", ".join(f"'{row['position_id']}'" for row in positions)
    
    query = f"""
        SELECT { "ms.goals, ms.assists," if table_name == "stats_summary" else "" }
                tn.*,
                CASE WHEN ms.minutes > 70 THEN 'more' ELSE 'less' END AS minutes_category
        FROM {table_name} tn
        JOIN match_statistics ms ON tn.stat_id = ms.estadistica_id
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN position_player pp ON tn.player_id = pp.player_id AND fm.match_id = pp.match_id
        JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        WHERE fm.Season = {league_id} AND pof.position_id IN ({position_list_sql}) 
    """

    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    df_more_than_70 = spark_df.filter(col("minutes_category") == "more").drop("minutes_category", "estatistic_id", "stat_id", "player_id")
    df_less_than_70 = spark_df.filter(col("minutes_category") == "less").drop("minutes_category", "estatistic_id", "stat_id", "player_id")

    return df_more_than_70, df_less_than_70


def query_to_get_basic_positions_stats_with_teams(spark, jdbc_url, db_properties, league_id, positions, table_name, team_id):
    
    position_list_sql = ", ".join(f"'{row['position_id']}'" for row in positions)
    
    query = f"""
        SELECT { "ms.goals, ms.assists," if table_name == "stats_summary" else "" }
                tn.*,
                CASE WHEN ms.minutes > 70 THEN 'more' ELSE 'less' END AS minutes_category
        FROM {table_name} tn
        JOIN match_statistics ms ON tn.stat_id = ms.estadistica_id
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN position_player pp ON tn.player_id = pp.player_id AND fm.match_id = pp.match_id
        JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
        WHERE fm.Season = {league_id} AND pof.position_id IN ({position_list_sql}) and t.team_id = {team_id}
    """

    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    df_more_than_70 = spark_df.filter(col("minutes_category") == "more").drop("minutes_category", "estatistic_id", "stat_id", "player_id")
    df_less_than_70 = spark_df.filter(col("minutes_category") == "less").drop("minutes_category", "estatistic_id", "stat_id", "player_id")

    return df_more_than_70, df_less_than_70




def query_to_get_stats_with_team(spark, jdbc_url, db_properties, league_id, table_name, position_name, team_id):
    # Base query con los joins    
    base_query = f"""
        SELECT { "ms.goals, ms.assists," if table_name == "stats_summary" else "" } 
               tn.*, 
               CASE WHEN ms.minutes > 70 THEN 'more' ELSE 'less' END AS minutes_category
        FROM {table_name} tn 
        JOIN match_statistics ms ON tn.stat_id = ms.estadistica_id
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN position_player pp ON ms.player_id = pp.player_id AND ms.match_id = pp.match_id
        JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
        
        WHERE fm.Season = {league_id} AND t.team_id = {team_id}
    """

    # Filtro según la posición
    if position_name == "GK":
        query = base_query + " AND pof.position_name = 'GK'"
    elif position_name == "Field":
        query = base_query + " AND pof.position_name != 'GK'"
    else:
        raise ValueError("position_name debe ser 'GK' o 'Field'")

    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)

    df_more_than_70 = spark_df.filter(col("minutes_category") == "more").drop("minutes_category", "estatistic_id", "stat_id", "player_id")
    df_less_than_70 = spark_df.filter(col("minutes_category") == "less").drop("minutes_category", "estatistic_id", "stat_id", "player_id")

    return df_more_than_70, df_less_than_70




def get_valid_type_of_stat(stat_type):
    if stat_type in valid_type_of_stat_values:
        return stat_type
    else:
        raise ValueError(f"Invalid value for type_of_stat: {stat_type}")

def get_valid_starter_status(starter_status):
    if starter_status in status_starter_player:
        return starter_status
    else:
        raise ValueError(f"Invalid value for starter_status: {starter_status}")


def create_stat_dict(league_id, position, stat_type, starter_status):
    return {
        "league_id": league_id,
        "position_player": position,
        "type_of_stat": get_valid_type_of_stat(stat_type),
        "starter_status": get_valid_starter_status(starter_status)
    }

def init_dicts_basic(league_id, position_category, tipo):
    return (
        create_stat_dict(league_id, position_category, "avg", tipo),
        create_stat_dict(league_id, position_category, "desv", tipo),
        create_stat_dict(league_id, position_category, "mode", tipo),
    )


def init_dicts_specific(league_id, pos_id, tipo):
    return (
        create_stat_dict_specific(league_id, pos_id, "avg", tipo),
        create_stat_dict_specific(league_id, pos_id, "desv", tipo),
        create_stat_dict_specific(league_id, pos_id, "mode", tipo),
    )
    
def create_stat_dict_specific(league_id, position, stat_type, starter_status):
    return {
        "league_id": league_id,
        "position_player": position,
        "type_of_stat": get_valid_type_of_stat(stat_type),
        "starter_status": get_valid_starter_status(starter_status)
    }


def init_dicts_specific_teams(league_id, pos_id, tipo, team_id):
    return (
        create_stat_dict_specific_teams(league_id, pos_id, "avg", tipo, team_id),
        create_stat_dict_specific_teams(league_id, pos_id, "desv", tipo, team_id),
        create_stat_dict_specific_teams(league_id, pos_id, "mode", tipo, team_id),
    )
    
def create_stat_dict_specific_teams(league_id, position, stat_type, starter_status, team_id):
    return {
        "league_id": league_id,
        "team_id": team_id,
        "position_player": position,
        "type_of_stat": get_valid_type_of_stat(stat_type),
        "starter_status": get_valid_starter_status(starter_status)
    }


def value_setting(value, avg, desv):
    
    if avg is None or desv is None or avg == 0:
        return 0.0  # o simplemente `return value`, depende de tu lógica

    if desv > UMBRAL_DISPERSION * avg:
        return np.log1p(value)

    return value


def loop_throgh_all_columns_basic_positions(spark_df, number_of_rows):
    dict_val_columns = {}
    dict_val_desv_columns = {}
    dict_val_mode_columns = {}
 
    
    for column in spark_df.columns:
        if column == 'player_id' or column == 'estatistic_id' or column == 'stat_id':
            continue
                
        # Rellenar nulos con 0 SOLO para esta columna
        df_col_filled = spark_df.withColumn(column, F.when(F.col(column).isNull(), F.lit(0)).otherwise(F.col(column)))
            
        # Calcular métricas sobre la columna sin nulos
        desv_val_column = df_col_filled.select(F.stddev(column)).collect()[0][0]
        sum_column = df_col_filled.select(F.sum(column)).collect()[0][0]

        try:
            mode_val = spark_df.groupBy(column).count().orderBy(F.desc("count")).first()
            mode_value = float(mode_val[column])
        except Exception:
            mode_value = 0.0  # por si falla el cálculo de la moda
        
        average_column = (sum_column / number_of_rows) if sum_column is not None and number_of_rows != 0 else 0.0
        #value_setting(sum_column, average_column, desv_val_column)

        dict_val_columns[column] = average_column
        dict_val_desv_columns[column] = float(desv_val_column) if desv_val_column is not None else 0.0
        dict_val_mode_columns[column] = float(mode_value)
                

    return dict_val_columns, dict_val_desv_columns, dict_val_mode_columns





def query_to_get_stats_by_specific_position(spark, jdbc_url, db_properties, league_id, position, table_name):
    
    query = f"""
        SELECT { "ms.goals, ms.assists," if table_name == "stats_summary" else "" }
                tn.*,
                CASE WHEN ms.minutes > 70 THEN 'more' ELSE 'less' END AS minutes_category
        FROM {table_name} tn
        JOIN match_statistics ms ON tn.stat_id = ms.estadistica_id
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN position_player pp ON tn.player_id = pp.player_id AND fm.match_id = pp.match_id
        JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        WHERE fm.Season = {league_id} AND pof.position_id IN ({",".join(map(str, position))})
    """

    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)

    df_more_than_70 = spark_df.filter(col("minutes_category") == "more").drop("minutes_category", "estatistic_id", "stat_id", "player_id")
    df_less_than_70 = spark_df.filter(col("minutes_category") == "less").drop("minutes_category", "estatistic_id", "stat_id", "player_id")

    return df_more_than_70, df_less_than_70
    
    
def check_if_avg_stats_of_league_exists_by_basic_position(spark, jdbc_url, db_properties, league_id, position):
    query = f"SELECT apsp.id FROM avg_player_stats_by_basic_positions apsp WHERE league_id = {league_id} AND position_player = {position}"
    
    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    return True if spark_df.count() > 0 else False

def check_if_avg_stats_of_league_exists_by_specific_position(spark, jdbc_url, db_properties, league_id, position):
    query = f"SELECT apssp.id FROM avg_player_stats_by_specific_positions apssp WHERE league_id = {league_id} AND position_player = {position}"
    print(f"Query: {query}")
    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    return True if spark_df.count() > 0 else False



def check_if_avg_teams_stats_of_league_exists_by_basic_position(spark, jdbc_url, db_properties, league_id, position, team_id):
    query = f"SELECT ats.id FROM avg_teams_stats_by_basic_positions ats WHERE league_id = {league_id} AND position_player = {position} AND team_id = {team_id}"
    
    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    return True if spark_df.count() > 0 else False




