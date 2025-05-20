
from pyspark.sql.functions import col







def get_player(name, spark, jdbc_url, db_properties):
    
    query = f"""
        SELECT player_id FROM jugador
        WHERE player = '{name}'
    """

    player_df = spark.read.jdbc(
        url=jdbc_url, 
        table="jugador", 
        properties=db_properties
    ).select("player_id").filter(col("player") == name)
    
    player = player_df.first()
    if player:
        return player['player_id']
    else:
        query = f"""
            SELECT player_id FROM jugador
            WHERE player = 'Desconocido'
        """
        player_df = spark.read.jdbc(url=jdbc_url, table="jugador", properties=db_properties).select("player_id").filter(col("player") == 'Desconocido')
        player = player_df.first()
        return player['player_id'] if player else -1


def get_event_shots(event, spark, jdbc_url, db_properties):

    query = f"""
        SELECT id FROM event_shots
        WHERE event_shot_name = '{event}'
    """

    event_df = spark.read.jdbc(
        url=jdbc_url, 
        table="event_shots", properties=db_properties
    ).select("id").filter(col("event_shot_name") == event)
    event = event_df.first()
    
    if event:
        return event['id']
    else:
        query = f"""
            SELECT id FROM event_shots
            WHERE event_shot_name = 'Other'
        """
        event_df = spark.read.jdbc(
            url=jdbc_url, 
            table="event_shots",
            properties=db_properties
        ).select("id").filter(col("event_shot_name") == 'Other')
        
        event = event_df.first()
        return event['id'] if event else -1


def get_body_part(body_part, spark, jdbc_url, db_properties):
    

    body_part_df = spark.read.jdbc(
        url=jdbc_url, 
        table="body_part", 
        properties=db_properties
    ).select("id").filter(col("body_part_name") == body_part)
   
    body_part = body_part_df.first()

    if body_part:
        return body_part['id']
    else:
        query = f"""
            SELECT id FROM body_part
            WHERE body_part_name = 'Other'
        """
        body_part_df = spark.read.jdbc(
            url=jdbc_url, 
            table="body_part", 
            properties=db_properties
        ).select("id").filter(col("body_part_name") == 'Other')

        body_part = body_part_df.first()
        
        return body_part['id'] if body_part else -1



def get_outcome(outcome, spark, jdbc_url, db_properties):


    outcome_df = spark.read.jdbc(
        url=jdbc_url, 
        table="outcome_stats", 
        properties=db_properties
        ).select("id").filter(col("outcome_name") == outcome)

    outcome = outcome_df.first()
    return outcome['id'] if outcome else -1


def get_team_id_by_name_andleague_id(team_name, league_id, spark, jdbc_url, db_properties):

    team_df = spark.read.jdbc(
        url=jdbc_url, 
        table="team",  # Reemplaza "team_table_name" con el nombre de la tabla
        properties=db_properties
    ).select("team_id").filter((col("team_name") == team_name) & (col("tournament_team_id") == league_id))


    team = team_df.first()
    return team['team_id'] if team else -1






