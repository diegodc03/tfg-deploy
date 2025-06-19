
#### DEFENSIVE BLOCK ####

def get_stats_to_defensive_player_and_bloque_medio_type_of_defense_laterales(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa laterales")
    

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
            
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.challenge_tackles,
            sda.challenge_tackles_pct,
            sda.blocks,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_completed_short,
            sps.passes_completed_medium,
            sps.passes_completed_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area

        FROM

            match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
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


def get_stats_to_defensive_player_and_bloque_medio_type_of_defense_central_defenders(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa  defensivos")


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
            
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.challenge_tackles,
            sda.challenge_tackles_pct,
            sda.blocks,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_pct_medium,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_won_pct

        FROM

            match_statistics ms
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
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



##############################################################################
# MIDFIELDERS DEFENSIVE BLOCK

def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa mediocentros defensivos\n")
    
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
            sds.challenge_tackles,
            sds.challenges,
            sds.challenge_tackles_pct,
            sds.blocks,
            sds.interceptions,
            sds.tackles_interceptions,
            sds.clearances,
            sds.errors,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.progressive_passes,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_won_pct

        FROM match_statistics ms
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
    
    
    
def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y mediocentros ofensivos\n")
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
            sps.passes_pct,
            sps.passes_progressive_distance,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.pass_xa,
            psn.take_ons,
            psn.take_ons_won_pct,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.passes_received,
            psn.progressive_passes_received,
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            ss.gca,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            sms.fouled,
            sms.interceptions,
            sds.tackles_won,
            sms.ball_recoveries,
            sms.aerials_won_pct
        
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
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





def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_creativo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y mediocentros creativo\n")
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
            sds.challenge_tackles,
            sds.challenge_tackles_pct,
            sds.blocked_passes,
            sds.interceptions,
            sds.tackles_interceptions,
            sds.clearances,
            sms.fouls,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_won_pct,
            psn.progressive_carries,
            psn.carries,
            psn.carries_progressive_distance,
            psn.touches,
            psn.touches_mid_3rd,
            psn.take_ons,
            psn.take_ons_won_pct,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.progressive_passes,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_into_final_third

    
        FROM match_statistics ms
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



def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_lateral(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y mediocentro lateral\n")

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
            sds.challenge_tackles,
            sds.challenge_tackles_pct,
            sds.blocks,
            sds.blocked_passes,
            sds.interceptions,
            sds.tackles_interceptions,
            sds.clearances,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_won_pct,
            psn.touches,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_live_ball,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_into_final_third,
            ss.gca
    
    
        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
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





#################################################################################
# FORWARD DEFENSIVE BLOCK

def get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_centro(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y delanteros centros\n")


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
            sds.tackles_att_3rd,
            sds.tackles_mid_3rd,
            sds.tackles_won,
            sds.challenge_tackles,
            sds.challenge_tackles_pct,
            sds.blocks,
            sds.blocked_passes,
            sds.interceptions,
            sds.tackles_interceptions,
            pos.touches_att_3rd,
            pos.touches_live_ball,
            pos.take_ons,
            pos.take_ons_won,
            pos.take_ons_won_pct,
            pos.carries,
            pos.carries_progressive_distance,
            pos.progressive_carries,
            pos.carries_into_final_third,
            pos.carries_into_penalty_area,
            pos.passes_received,
            pos.progressive_passes_received,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.passes_completed_short,
            sps.passes_pct_short

        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary pos ON ms.player_id = pos.player_id AND ms.estadistica_id = pos.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
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




def get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_extremo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y delanteros extremo\n")

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
            sds.tackles_att_3rd,
            sds.tackles_mid_3rd,
            sds.tackles_won,
            sds.interceptions,
            sds.blocks,
            sds.blocked_passes,
            sds.tackles_interceptions,
            sds.challenge_tackles,
            sds.challenge_tackles_pct,
            pos.take_ons,
            pos.take_ons_won,
            pos.take_ons_won_pct,
            pos.passes_received,
            pos.progressive_passes_received,
            pos.touches_att_3rd,
            pos.touches_att_pen_area,
            pos.touches_live_ball,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.pass_xa,
            sps.passes_completed_short,
            sps.passes_pct_short,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.offsides

        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary pos ON ms.player_id = pos.player_id AND ms.estadistica_id = pos.stat_id
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