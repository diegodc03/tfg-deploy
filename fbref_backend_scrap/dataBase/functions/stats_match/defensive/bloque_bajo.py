####### Bloque Bajo


### DEFENSIVE STATS
def get_stats_to_defensive_player_and_bloque_bajo_type_of_defense_laterales(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa laterales")


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
            sda.interceptions,
            sda.blocks,
            sda.clearances,
            sda.errors,
            sda.tackles_def_3rd,
            sda.blocked_shots,
            sda.blocked_passes,
            sms.ball_recoveries,
            sms.aerials_won,
            spts.passes_blocked,
            sda.challenges,
            sda.challenge_tackles_pct,
            psn.passes_received
        FROM
            match_statistics ms
        LEFT JOIN stats_summary sm ON ms.player_id = sm.player_id AND ms.estadistica_id = sm.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
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
    
positions = [
        ['FB', 'LB', 'RB'],
        ['CB', 'CDM'],
        ['LW', 'RW', 'LM', 'RM'],
        ['CAM', 'CF'],
        ['ST'],
        ['GK']
    ]


            
# Specific positions for each type of player tiene una union con todas las posiciones de los jugadores
# y se le asigna un nombre a cada una de las posiciones para poder hacer la union con el resto de los jugadores    


def get_stats_to_defensive_player_and_bloque_bajo_type_of_defense_central_defenders(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa centrales")

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
       
            psn.take_ons_won_pct,
            sda.interceptions,
            sda.blocks,
            sda.clearances,
            sda.errors,
            sms.fouls,
            psn.touches_def_pen_area,
            sda.blocked_shots,
            sda.blocked_passes,
            sms.ball_recoveries,
            sps.passes_pct,
            sps.progressive_passes,
            sda.challenges,
            sda.challenge_tackles_pct,
            psn.touches_def_3rd,
            sms.offsides,
            psn.passes_received,
            spts.crosses
        FROM
            match_statistics ms
        LEFT JOIN stats_summary sm ON ms.player_id = sm.player_id AND ms.estadistica_id = sm.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sm.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
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



#### CENTROCAMPISTAS ####

def get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros defensivos\n")

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
            sds.challenge_tackles,
            sds.challenges,
            sds.challenge_tackles_pct,
            sds.challenged_lost,
            sds.blocks,
            sds.blocked_shots,
            sds.blocked_passes,
            sds.interceptions,
            sds.tackles_interceptions,
            sds.clearances,
            sds.errors,
            psn.miscontrols,
            psn.dispossessed,
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area
            
            FROM match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
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



def get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros ofensivos\n")

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
            sds.tackles_mid_3rd,
            sds.interceptions,
            sds.clearances,
            psn.touches,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.take_ons,
            psn.take_ons_won,
            psn.carries,
            psn.carries_progressive_distance,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_progressive_distance,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.xg_assists,
            sps.assisted_shots,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.progressive_passes

        FROM match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
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


def get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_creativo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y mediocentros creativo\n")

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
            sds.interceptions,
            sds.clearances,
            sms.ball_recoveries,
            sms.aerials_won_pct,
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.passes_progressive_distance,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_long,
            sps.passes_pct_long,
            sps.xg_assists,
            psn.take_ons,
            psn.take_ons_won,
            psn.progressive_passes_received,
            psn.touches_mid_3rd,
            psn.carries_into_final_third

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
    print(query)
    return query


def get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_lateral(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y  mediocentros lateral\n")

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
        sds.blocks,
        sds.interceptions,
        sds.clearances,
        psn.touches,
        psn.touches_def_3rd,
        psn.touches_mid_3rd,
        psn.touches_live_ball,
        psn.take_ons,
        psn.take_ons_won,
        psn.progressive_carries,
        psn.carries,
        psn.carries_into_final_third,
        sps.passes_completed,
        sps.passes_pct,
        sps.passes_into_final_third,
        sps.passes_completed_short,
        sps.passes_short,
        sps.progressive_passes,
        sps.xg_assists,
        sms.ball_recoveries,
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




#### DELANTEROS ####

def get_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_centro(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y delantero centro\n")

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

        sm.shots,
        sm.shots_on_target,
        sda.tackles,
        sda.tackles_won,
        sda.interceptions,
        sda.blocks,
        sm.xg,
        sm.npxg,
        sps.xg_assists,
        sm.sca,
        sm.gca,
        sps.passes_completed,
        sps.passes_pct,
        sps.progressive_passes,
        sps.passes_into_final_third,
        sps.passes_into_penalty_area,
        sps.crosses_into_penalty_area,
        sps.assisted_shots,
        psn.passes_received,
        psn.progressive_passes_received,
        sda.clearances,
        sms.fouls,
        sms.ball_recoveries

    FROM
        match_statistics ms
    	LEFT JOIN football_match fm ON ms.match_id = fm.match_id
    LEFT JOIN stats_summary sm ON ms.player_id = sm.player_id AND ms.estadistica_id = sm.stat_id
    LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
    LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
    LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
    LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
    LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
    LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id

    LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
    LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 

        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
    """

    return query








def get_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_extremo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y delantero extremo\n")

    
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
            sds.tackles,
            sds.tackles_won,
            sds.interceptions,
            sds.blocks,
            ss.xg,
            ss.npxg,
            sps.xg_assists,
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            pos.carries,
            pos.progressive_carries,
            pos.take_ons,
            pos.take_ons_won,
            pos.passes_received,
            pos.progressive_passes_received,
            pos.touches_def_pen_area,
            pos.touches_def_3rd,
            pos.touches_mid_3rd,
            pos.touches_att_3rd,
            pos.touches_live_ball,
            sms.fouls,
            sms.fouled,
            pos.dispossessed

        FROM
            match_statistics ms

        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_defensiveactions_summary sds ON ms.player_id = sds.player_id AND ms.estadistica_id = sds.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary pos ON ms.player_id = pos.player_id AND ms.estadistica_id = pos.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id
        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
    
    """
    return query