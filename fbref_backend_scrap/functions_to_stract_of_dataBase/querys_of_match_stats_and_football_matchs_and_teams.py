   
from w_read_dataframe_to_mysql_file import read_data_with_spark
from pyspark.sql.functions import col
    
def get_rows_of_match_statistics(spark, jdbc_url, db_properties, match_id):
    
    query = f"""
        SELECT ms.estadistica_id, ms.player_id  FROM match_statistics ms WHERE ms.match_id = {match_id}
    """
    spark_df = read_data_with_spark(spark, jdbc_url, db_properties, query)
    return spark_df
    
    
    
    
def select_football_match(spark, jdbc_url, db_properties, match_id):
    
    query = f"""
        SELECT fm.Score, fm.Home, fm.Away FROM football_match fm WHERE match_id = {match_id}
    """
    spark_df = read_data_with_spark(
            spark, 
            jdbc_url, 
            db_properties, 
            query
    )
    
    if spark_df.count() > 0:
        return spark_df.collect()[0]
    else:
        return None
    
    


def get_all_matchs_ids_of_league_id(spark, jdbc_url, db_properties, league_id):
    query = f"""
        SELECT match_id FROM football_match WHERE league_id = {league_id}
    """
    return spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as match_ids",
        properties=db_properties
    )
    
    
    
    
def check_if_match_id_score_exists(spark, jdbc_url, db_properties, match_id):
    query = f"""
        SELECT COUNT(*) as count FROM match_statistics WHERE match_id = {match_id}
    """
    result_df = spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) as match_stats",
        properties=db_properties
    )
    
    

def check_season_exists(season_year, spark, jdbc_url, db_properties):
    # Leer la tabla 'season' desde MySQL usando JDBC
    season_df = spark.read.jdbc(url=jdbc_url, table="season", properties=db_properties)

    # Filtrar por el 'season_year' deseado
    filtered_df = season_df.filter(season_df["season_year"] == season_year)

    # Contar las filas que coinciden con la temporada
    count = filtered_df.count()

    # Si el contador es mayor que 0, la temporada ya existe
    return count > 0


def check_tournament_exists(nombre_liga, season_tournament_id, spark, jdbc_url, db_properties):

    tournament_df = spark.read.jdbc(url=jdbc_url, table="tournament", properties=db_properties)

    filtered_df = tournament_df.filter((tournament_df["nombre_liga"] == nombre_liga) & 
                                       (tournament_df["season_tournament_id"] == season_tournament_id))

    count = filtered_df.count()
    return count > 0




def get_match_id_by_teams_and_tournament(local_team_id, visitor_team_id, season, spark, jdbc_url, db_properties):

    query = f"""
    SELECT match_id FROM football_match
    WHERE Home = {local_team_id}
      AND Away = {visitor_team_id}
      AND Season = {season}
    """

    match_df = spark.read.jdbc(
        url=jdbc_url, 
        table="football_match", 
        properties=db_properties
    ).select("match_id").filter((col("Home") == local_team_id) & (col("Away") == visitor_team_id) & (col("Season") == season))
    
    match = match_df.first()
    if not match:
        return -1
    else:
        return match['match_id']
    
    
    

def get_result_of_match(spark, jdbc_url, db_properties, match_id):
    
    query = f"""
        SELECT 
            fm.Score, 
            home_team.team_name AS Home_Team_Name, 
            fm.Home AS Home_Team_ID,
            fm.Away AS Away_Team_ID,
            away_team.team_name AS Away_Team_Name
        FROM football_match fm
        JOIN team home_team ON fm.Home = home_team.team_id
        JOIN team away_team ON fm.Away = away_team.team_id
        WHERE fm.match_id = {match_id};
    """
    
    return read_data_with_spark(spark, jdbc_url, db_properties, query)
    
    

def get_match_of_tournaments(spark, jdbc_url, db_properties):
    # Leer todas las ligas posibles de la base de datos
    tournaments = spark.read.jdbc(url=jdbc_url, table="tournament", properties=db_properties)
    
    # Leer la tabla de temporadas para obtener los season_year
    seasons = spark.read.jdbc(url=jdbc_url, table="season", properties=db_properties)
    
    # Hacer un join entre 'tournaments' y 'seasons' basándonos en 'season_tournament_id' y 'season_id'
    tournaments_with_season = tournaments.join(seasons, tournaments['season_tournament_id'] == seasons['season_id'], 'left') \
                                         .select(tournaments['*'], seasons['season_year'])

    return tournaments_with_season





"""
    Get teams in competition.
"""
def get_teams_in_competition(spark, jdbc_url, db_properties, tournament_id):
    
    query = f"""
         SELECT DISTINCT t.team_id, t.team_name FROM team t  WHERE t.tournament_team_id = {tournament_id}

    """
    return read_data_with_spark(spark, jdbc_url, db_properties, query)





