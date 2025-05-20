



# DEFENSE



def get_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_laterales(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")

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

            -- Defensive Actions
            ss.passes_completed,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            spts.crosses,
            sps.crosses_into_penalty_area,
            spn.carries,
            spn.progressive_carries,
            spn.carries_into_final_third,
            spn.touches_att_3rd,
            spn.touches_att_pen_area,
            spn.take_ons,
            spn.take_ons_won,
            spts.passes_switches,
            spts.through_balls, 
            spn.progressive_passes_received,
            sps.passes_pct
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
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





def get_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_central_defenders(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")
    

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
            
            -- Defensive Actions
            sps.passes_completed,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.progressive_passes,
            sps.passes_completed_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            spts.through_balls,
            spn.progressive_passes_received,
            spn.carries,
            spn.progressive_carries,
            spn.carries_distance,
            spn.touches_mid_3rd,
            sda.clearances,
            sda.interceptions,
            sda.tackles,
            sda.blocks,
            sps.passes_pct,
            spn.take_ons,
            spn.take_ons_won
        FROM
            match_statistics ms
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
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


################################################################
# MIDFIELDERS

def get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
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
            
            -- DEFENSIVA
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.challenge_tackles,
            sda.challenges,
            sda.challenge_tackles_pct,
            sda.challenged_lost,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,

            -- PASES
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            spts.crosses,
            
            sps.passes,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_short,
            sps.passes_medium,
            sps.passes_long,
            sps.progressive_passes,

            -- RECEPCIÓN
            psn.passes_received,
            psn.progressive_passes_received,

            -- REGATES / POSESIÓN
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,

            -- TOQUES
            psn.touches,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_live_ball,

            -- ERRORES y DUELLOS
            psn.miscontrols,
            psn.dispossessed,
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- CREACIÓN
            ss.gca,
            ss.sca,
            ms.assists
            
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
    
    
def get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
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
            
           
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.progressive_passes,
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
            sps.pass_xa,
            sps.assisted_shots,
            spts.through_balls,
            spts.passes_switches,
            spts.crosses,

            -- DEFENSIVA
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.blocks,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.challenges,
            sda.challenge_tackles_pct AS challenges_pct,

            -- RECEPCIÓN Y POSESIÓN
            psn.passes_received,
            psn.progressive_passes_received,
            psn.miscontrols,
            psn.dispossessed,
            sms.fouls,
            sms.fouled,
            sms.ball_recoveries,
            
            -- DUELOS AÉREOS
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- REGATES
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct
                
           
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



def get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_creativo(match_id, season, specific_position_id):
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
            
            -- OFENSIVA
            ss.shots,
            ss.shots_on_target,
            ss.xg_assist,
            sps.assisted_shots,

            -- DISTRIBUCIÓN
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            spts.crosses,
            spts.passes_live,
            spts.through_balls,
            spts.passes_switches,
            spts.throw_ins,

      

            -- REGATES Y POSESIÓN
            psn.take_ons,
            psn.take_ons_won,
            psn.progressive_carries,
            psn.passes_received,
            psn.progressive_passes_received,
            psn.dispossessed,

            -- DEFENSIVA
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.challenge_tackles,
            sda.challenges,
            sda.challenge_tackles_pct,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sms.fouls,
            sms.fouled,
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



def get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_lateral(match_id, season, specific_position_id):
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
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
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
            sps.assisted_shots,
            ss.xg_assist,
            
            spts.crosses,
            spts.throw_ins,
            spts.through_balls,
            spts.passes_switches,

            -- DEFENSA
            sda.tackles,
            sda.tackles_won,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.tackles_def_3rd,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.clearances,
            sda.challenges,
            sda.challenge_tackles,
            sda.challenge_tackles_pct,

            -- REGATES Y CONTROL
            psn.touches,
            psn.touches_live_ball,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,
            psn.dispossessed,
            psn.miscontrols,

            -- FALTAS Y JUEGO AÉREO
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.aerials_won,
            sms.aerials_lost
           
            
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



# FORWARDERS

def get_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_centro(match_id, season, specific_position_id):
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
            sms.aerials_lost,
            spn.touches,
            spn.touches_att_3rd,
            spn.touches_att_pen_area,
            spn.take_ons_won_pct,
            spn.miscontrols,
            spn.dispossessed,
            spts.crosses,
            sms.fouls,
            sms.fouled
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
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






def get_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_extremo(match_id, season, specific_position_id):
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
            sms.aerials_lost,
            spn.touches,
            spn.touches_att_3rd,
            spn.touches_att_pen_area,
            spn.take_ons_won_pct,
            spn.miscontrols,
            spn.dispossessed,
            spts.crosses,
            sms.fouls,
            sms.fouled
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
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


