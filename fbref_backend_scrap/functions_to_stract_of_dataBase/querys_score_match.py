
from w_read_dataframe_to_mysql_file import read_data_with_spark
from pyspark.sql.functions import col

def get_scores_by_type_of_game_mode(spark, jdbc_url, db_properties, match_id, game_mode_id, league_id):
    """
    Get scores by type of game mode.
    """
    
    query = f"""
        SELECT 
            j.player,
            ms.minutes,
            mps.score,
            psc.specific_position_name,
            pc.category_name
            t.team_name AS team_name,
        FROM match_statistics ms
        JOIN match_players_score mps ON ms.estadistica_id = mps.match_player_id
        JOIN jugador j ON ms.player_id = j.player_id
        JOIN positions_specifics_by_category psc ON mps.specific_position_id = psc.specific_position_id
        JOIN game_modes gm ON mps.game_mode_id = gm.game_mode_id
        JOIN position_category pc ON pc.category_id = mps.basic_position_id 
        JOIN football_match fm ON ms.match_id = fm.match_id
        JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
        WHERE ms.match_id = {match_id} AND gm.game_mode_id = {game_mode_id} AND fm.Season = {league_id}
    """
    
    read_data_with_spark(spark, jdbc_url, db_properties, query)



def get_season_tournament_id(season_year, spark, jdbc_url, db_properties):
    # Consulta SQL para obtener el `season_tournament_id` basado en `nombre_liga` y `season_year`
    query = f"""
    SELECT season_id
    FROM season
    WHERE season_year = '{season_year}'
    """
    
    # Ejecutar la consulta
    season_tournament_df = read_data_with_spark(spark, jdbc_url, db_properties, query).select("season_id").filter(col("season_year") == season_year)
    
    if season_tournament_df.count() > 0:
        return season_tournament_df.collect()[0]['season_id']
    else:
        return None  # Si no se encuentra, devolver None
    
    
    
    
    
def get_number_of_scores_by_type_of_game_mode_and_specific_position_id(spark, jdbc_url, db_properties, match_id, game_mode_id, specific_position_id):
    """
    Get number of scores by type of game mode and specific position id.
    """
    
    query = f"""
        SELECT COUNT(*) FROM match_players_score mps JOIN match_statistics ms ON mps.match_player_id = ms.estadistica_id 
        WHERE ms.match_id = {match_id} AND mps.game_mode_id = {game_mode_id} AND mps.specific_position_id = {specific_position_id}
    """
    
    print("La query es", query)
    
    number_of_rows = read_data_with_spark(spark, jdbc_url, db_properties, query)
    return number_of_rows.collect()[0][0] if number_of_rows.count() > 0 else 0
    
    
    
def get_number_of_scores_by_type_of_game_mode_and_basic_position_id(spark, jdbc_url, db_properties, match_id):
    """
    Get number of scores by type of game mode and specific position id.
    """
    
    query = f"""
        SELECT COUNT(*) FROM match_players_score mps JOIN match_statistics ms ON mps.match_player_id = ms.estadistica_id 
        WHERE ms.match_id = {match_id} AND mps.game_mode_id = 0
    """
    print("La query es", query)
    number_of_rows = read_data_with_spark(spark, jdbc_url, db_properties, query)
    return number_of_rows.collect()[0][0] if number_of_rows.count() > 0 else 0