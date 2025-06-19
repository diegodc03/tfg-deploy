



def get_stats_to_defensive_player_and_contraataque_type_of_defense_laterales(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y defensa mediocentros defensivos")


    query = f"""
        SELECT

            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            
            ms.minutes,
            sps.passes_completed,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.progressive_passes,
            psn.carries,
            psn.progressive_carries,
            spts.crosses,
            sps.crosses_into_penalty_area,
            ss.shots,
            ss.shots_on_target,
            psn.touches,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            spts.through_balls,
            ss.take_ons,
            ss.take_ons_won,
            psn.carries_distance,
            sps.passes_pct,
            psn.progressive_passes_received
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT join stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
    """
    return query
            


def get_stats_to_defensive_player_and_contraataque_type_of_defense_central_defenders(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y defensa mediocentros defensivos")


    query = f"""
        SELECT
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            
            ms.minutes,
            sps.passes_completed,
            sps.passes_total_distance,
            sps.passes_progressive_distance, 
            sps.progressive_passes,
            psn.carries,
            psn.progressive_carries,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            spts.through_balls,
            sda.clearances,
            sda.interceptions,
            sda.tackles,
            psn.progressive_passes_received,
            psn.touches,
            psn.take_ons,
            psn.take_ons_won,
            sps.passes_pct,
            sps.passes_completed_long,
            psn.carries_distance
            
        FROM
            match_statistics ms
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
    """
    return query












#######################################################################################
# MIDFIELDERS

def get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y defensa mediocentros defensivos\n")
    
    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
            
            sds.tackles,
            sds.tackles_won,
            sds.tackles_def_3rd,
            sds.tackles_mid_3rd,
            sds.tackles_interceptions,
            sds.interceptions,
            sds.clearances,
            sds.blocks,
            sds.blocked_passes,
            sds.errors,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_won_pct,
            sps.progressive_passes,
            sps.passes_completed_long,
            sps.passes_pct_long,
            sps.passes_progressive_distance,
            sps.passes_into_final_third,
            psn.progressive_carries,
            psn.carries_distance,
            psn.miscontrols,
            psn.dispossessed,
            psn.passes_received,
            psn.progressive_passes_received,
            sms.fouls
        
        FROM 
            match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
            
            WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
        """
    return query
    
    

def get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y  mediocentros ofensivos\n")

    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,

            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.assisted_shots,
            sps.pass_xa,
            ms.assists,
            ss.xg_assist,
            ss.sca,
            ss.gca,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            sms.fouled,
            sms.ball_recoveries
        
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
        
        WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
        """
    return query






def get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_creativo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y  mediocentros creativa\n")

    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
  
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            spts.through_balls,
            sps.passes_completed_long,
            sps.passes_pct_long,
            sps.passes_completed_medium,
            sps.passes_pct_medium,
            ss.xg_assist,
            ss.sca,
            ss.gca,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,
            sms.ball_recoveries,
            sds.interceptions,
            sds.tackles,
            sds.tackles_won,
            sds.tackles_interceptions,
            sds.blocks
            
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
            
            WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
        """
    return query




def get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_lateral(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y  mediocentros lateral\n")
    
    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
            
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.assisted_shots,
            sps.pass_xa,
            ms.assists,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.carries,
            psn.progressive_carries,
            psn.carries_progressive_distance,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            sds.tackles_att_3rd,
            sds.challenge_tackles,
            sds.challenges,
            sds.interceptions,
            sms.ball_recoveries,
            psn.dispossessed
        
        FROM 
            match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
            
            WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
        """
    return query







########################################################################################
# FORWARD

def get_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_centro(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y defensa mediocentros defensivos\n")
    
    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
            
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            ss.sca,
            ss.gca,
            ss.pens_made,
            ss.pens_att,
            sps.assisted_shots,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct
        FROM
            match_statistics ms
            LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
            LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
            LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
            LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
            LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
            LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
            LEFT JOIN football_match fm ON ms.match_id = fm.match_id
            
            LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
            LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
            
            WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
        """
    return query

def get_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_extremo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo contraataque y defensa mediocentros defensivos \n")

    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pof.specific_position_id AS category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
            
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            sps.assisted_shots,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.passes_completed,
            sps.passes_pct,
            psn.carries,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.passes_received,
            psn.progressive_passes_received,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,
            sms.fouled
        
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
    
    """
    return query