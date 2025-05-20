


def get_stats_to_offensive_player_and_tiki_taka_type_of_defense_laterales(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa laterales")
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
            
            
            
            ms.assists,
            ms.goals,
            
            ss.tackles,
            ss.interceptions,
            sda.clearances,
            sda.blocks,
            spts.crosses,
            spn.take_ons,
            spn.take_ons_won,
            sps.passes_completed,
            sps.passes_pct,
            
            sps.progressive_passes,
            smm.fouls,
            smm.fouled,
            smm.ball_recoveries,
            smm.aerials_won,
            sps.passes_completed_long,
            sps.assisted_shots,
            spn.touches
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN stats_miscellaneous_summary smm ON ms.player_id = smm.player_id AND ms.estadistica_id = smm.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season} 
        -- AND pp.position_id IN (34, 37, 41)
        -- AND pof.specific_position_id = (SELECT specific_position_id FROM positions_specifics_by_category WHERE specific_position_name = "{specific_position_id}")
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
        GROUP BY ms.player_id
    """
    return query

def get_stats_to_offensive_player_and_tiki_taka_type_of_defense_central_defenders(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa centrales")

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
            
            
            ms.assists,
            ms.goals,
            
            sda.tackles,
            sda.interceptions,
            sda.clearances,
            sda.blocks,
            sda.tackles_won,
            
            smm.aerials_won,
            smm.ball_recoveries,
            smm.fouls,
            smm.fouled,
            sda.errors,
            
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            
            sps.passes_completed_long,
            sda.challenge_tackles,
            
            sda.blocked_shots,
            spts.crosses
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN stats_miscellaneous_summary smm ON ms.player_id = smm.player_id AND ms.estadistica_id = smm.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season} 
        AND pof.specific_position_id = {specific_position_id}
        AND fm.match_id = {match_id}
        
        GROUP BY ms.player_id
    """
    return query


############################################################################
# MIDFIELDERS



def get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            
            -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,

            -- TOQUES
            psn.touches,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_live_ball,

            -- CARRIES
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,

            -- REGATES
            ss.take_ons,
            ss.take_ons_won,
            psn.take_ons_won_pct,

            -- ERRORES Y PÉRDIDAS
            psn.miscontrols,
            psn.dispossessed,

            -- RECEPCIÓN DE PASES
            psn.passes_received,
            psn.progressive_passes_received,

            -- DEFENSIVA
            sda.interceptions,
            sda.tackles,
            sda.tackles_won,
            sda.tackles_interceptions,
            sda.errors,
            sms.ball_recoveries
            
            
        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
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

    
def get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,

            -- RECEPCIÓN DE PASES
            psn.progressive_passes_received,
            psn.passes_received,

            -- CREACIÓN DE OCASIONES
            ss.xg_assist,
            sps.assisted_shots,
            ss.sca,
            ss.gca,

            -- TOQUES
            psn.touches,
            psn.touches_live_ball,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,

            -- CARRIES
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,

            -- REGATES Y POSESIÓN
            ss.take_ons,
            ss.take_ons_won,
            psn.take_ons_won_pct,
            psn.miscontrols,
            psn.dispossessed,

            -- DISCIPLINA
            sms.fouls,
            sms.fouled,

            -- DEFENSA
            sda.interceptions,
            sda.tackles,
            sda.tackles_won,
            sms.ball_recoveries,

            -- JUEGO AÉREO
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct
            
            
        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
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



def get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_creativo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            
           
            -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,

            -- CREACIÓN DE OCASIONES
            ss.xg_assist,
            sps.assisted_shots,
            ss.sca,
            ss.gca,


            -- CARRIES
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,

            -- TOQUES
            psn.touches,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.touches_live_ball,

            -- REGATES
            ss.take_ons,
            ss.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,

            -- RECUPERACIÓN Y DEFENSA
            sms.ball_recoveries,
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.interceptions,
            sda.tackles_interceptions,
            sms.fouls,
            sms.fouled,

            -- PÉRDIDAS DE BALÓN
            psn.miscontrols,
            psn.dispossessed,

            -- RECEPCIÓN DE PASES
            psn.progressive_passes_received,
            psn.passes_received
            
            
        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
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
    
    
def get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_lateral(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            
             -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.progressive_passes,

            -- REGATES Y POSESIÓN
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.miscontrols,
            psn.dispossessed,

            -- RECEPCIÓN DE PASES
            psn.progressive_passes_received,
            psn.passes_received,

            -- CREACIÓN DE OCASIONES
            ss.xg_assist,
            sps.assisted_shots,
            ss.sca,
            ss.gca,

            -- TOQUES
            psn.touches,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.touches_live_ball,

            -- DEFENSA
            sda.tackles,
            sda.tackles_won,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.interceptions,
            sda.tackles_interceptions,
            sms.ball_recoveries,
            sms.fouls,
            sms.fouled
            
            
            
        FROM match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
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


########################################################################
# FORWARDS

def get_stats_to_offensive_player_and_tiki_taka_type_of_delantero_centro(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            
            
            ms.goals,
            ms.assists,
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            ss.sca,
            ss.gca,
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.assisted_shots,
            spn.passes_received,
            spn.progressive_passes_received,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            spn.take_ons,
            spn.take_ons_won,
            spn.take_ons_tackled,
            spn.take_ons_tackled_pct,
            sms.aerials_won,
            sms.aerials_lost
        FROM

            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season}
        AND pof.specific_position_id = {specific_position_id}        
        AND fm.match_id = {match_id}
    """
    return query

def get_stats_to_offensive_player_and_tiki_taka_type_of_delantero_extremo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")


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
            ms.goals,
            ms.assists,
            ss.shots,
            ss.shots_on_target,
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            sps.passes_completed,
            sps.passes_pct,
            sps.progressive_passes,
            spn.carries,
            spn.progressive_carries,
            spn.take_ons,
            spn.take_ons_won,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.assisted_shots,
            spn.passes_received,
            spn.progressive_passes_received,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            spn.take_ons_tackled,
            spn.take_ons_tackled_pct,
            sms.aerials_won,
            sms.aerials_lost
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN position_on_the_field pof ON pp.position_id = pof.position_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        WHERE fm.Season = {season}
            AND pof.specific_position_id = {specific_position_id}
            AND fm.match_id = {match_id}
    """
    return query


