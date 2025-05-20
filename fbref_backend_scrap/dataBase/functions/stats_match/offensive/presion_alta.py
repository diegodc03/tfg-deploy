

# defenSE

def get_stats_to_offensive_player_and_presion_alta_type_of_defense_laterales(match_id, season, specific_position_id):
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
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,
            
            -- Possession
            spn.touches,
            spn.touches_def_pen_area,
            spn.touches_def_3rd,
            spn.touches_mid_3rd,
            spn.touches_att_3rd,
            spn.touches_live_ball,
            spn.take_ons_won,
            spn.carries,
            spn.carries_progressive_distance,
            spn.progressive_carries,
            spn.carries_into_final_third,
            spn.miscontrols,
            spn.dispossessed,
            spn.passes_received,
            spn.progressive_passes_received,
            
            -- Passing
            sps.passes_completed,
            sps.passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.progressive_passes,
            
            -- Miscellaneous
            smm.fouls,
            smm.fouled,
            smm.cards_yellow,
            smm.cards_red,
            smm.offsides,
            smm.aerials_won

        FROM 
            match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_miscellaneous_summary smm ON ms.player_id = smm.player_id AND ms.estadistica_id = smm.stat_id
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





def get_stats_to_offensive_player_and_presion_alta_type_of_defense_central_defenders(match_id, season, specific_position_id):
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
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.challenges,
            sda.challenge_tackles_pct,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,
            
            -- Passing
            sps.passes_completed,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.progressive_passes,
            
            -- Miscellaneous
            spn.touches,
            spn.touches_def_3rd,
            spn.touches_mid_3rd,
            spn.touches_att_3rd,
            spn.touches_live_ball,
            sms.aerials_won,
            sms.aerials_lost,
            sms.ball_recoveries

        FROM
            match_statistics ms
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
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



#####################################################################################
# MIDFIELDERS


def get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_defensivo(match_id, season, specific_position_id):
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
            
            -- DEFENSA
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
            
            
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- REGATES Y POSESIÓN
            ss.take_ons,
            ss.take_ons_won,
            
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.miscontrols,
            psn.dispossessed,

            -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            psn.progressive_passes_received,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            psn.passes_received,
            spts.passes_blocked,
            spts.passes_live,
            spts.passes_dead,
            spts.passes_free_kicks,
            spts.through_balls,
            spts.passes_switches,
            spts.crosses

            
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



def get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
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
            
            -- Métricas de XG (Expected Goals)
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            ss.sca,
            ss.gca,

            -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            
            psn.passes_received,
            psn.progressive_passes_received,

            -- TOQUES
            psn.touches,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,

            -- REGATES
            ss.take_ons,
            ss.take_ons_won,
            psn.take_ons_won_pct,

            -- PASES EN LARGO Y CORTO
            spts.through_balls,
            spts.passes_switches,
            sps.passes_completed_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_pct_long,

            -- ASISTENCIAS Y GOL
            ms.assists,
            sps.assisted_shots,

            -- OTRAS ESTADÍSTICAS DE PASES
            spts.passes_offsides,
            spts.passes_blocked,

            -- DEFENSA
            sda.tackles_won,
            sda.interceptions,
            sda.clearances,
            sms.fouls,
            sms.fouled,

            -- CRUCES Y BALONES GANADOS
            spts.crosses,
            sms.ball_recoveries,
            sms.aerials_won
            
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



def get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_creativo(match_id, season, specific_position_id):
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
            -- Métricas de XG (Expected Goals)
            ss.xg,
            ss.npxg,
            ss.xg_assist,
            ss.sca,
            ss.gca,

            -- PASES
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            psn.passes_received,
            psn.progressive_passes_received,

            -- TACKLES Y DEFENSA
            sda.tackles_won,
            sda.interceptions,
            sda.clearances,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.tackles_interceptions,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,

            -- OTRAS ESTADÍSTICAS DE DEFENSA
            sms.fouls,
            sms.fouled,
            spts.passes_offsides,
            spts.passes_blocked,
            psn.miscontrols,
            psn.dispossessed,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- REGATES
            ss.take_ons,
            ss.take_ons_won,
            psn.take_ons_won_pct,

            -- ESTADÍSTICAS DE PASES
            spts.passes_switches,
            spts.throw_ins,
 

            -- TACKLES ADICIONALES
            sda.tackles,
            psn.take_ons_tackled
            
            
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



def get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_lateral(match_id, season, specific_position_id):
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
        
        -- TACKLES Y DEFENSA
        sda.tackles,
        sda.tackles_won,
        sda.tackles_def_3rd,
        sda.tackles_mid_3rd,
        sda.tackles_att_3rd,
        sda.interceptions,
        sda.blocks,
        
        -- PASES
        sps.passes_completed,
        sps.passes,
        sps.passes_pct,
        sps.progressive_passes,
        psn.progressive_carries,
        
        ss.take_ons,
        ss.take_ons_won,
        psn.passes_received,
        psn.progressive_passes_received,
        sps.passes_into_final_third,
        sps.passes_into_penalty_area,
        sps.crosses_into_penalty_area,
        sps.assisted_shots,
        
        -- TACKLES E INTERCEPCIONES
        sda.tackles_interceptions,
        sda.challenges,
        sda.challenge_tackles_pct,
        sda.challenged_lost,
        
        -- OTRAS ESTADÍSTICAS DEFENSIVAS
        sda.clearances,
        sda.errors,
        sms.fouls,
        sms.fouled,
        psn.miscontrols,
        psn.dispossessed,
        
        -- BALONES AÉREOS
        sms.aerials_won,
        sms.aerials_won_pct,
        sms.aerials_lost,
        
        -- PASES DETALLADOS
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
        sps.passes_pct_long
           
           
            
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





#######################################################################################
# FORWARDS

def get_stats_to_offensive_player_and_presion_alta_type_of_delantero_centro(match_id, season, specific_position_id):
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
            ss.take_ons,
            ss.take_ons_won,
            sda.tackles,
            sda.tackles_won,
            sda.tackles_att_3rd,
            sda.interceptions,
            sda.blocks,
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            spn.progressive_carries,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            spn.passes_received,
            spn.progressive_passes_received,
            sps.assisted_shots,
            ss.xg_assist,
            ss.gca,
            ss.sca,
            ss.xg,
            ss.npxg,
            spn.dispossessed,
            spn.take_ons_won_pct,
            spn.take_ons_tackled,
            spts.passes_offsides,
            spts.passes_blocked,
            spts.crosses,
            sda.tackles_interceptions,
            sda.challenges,
            sda.challenge_tackles,
            sms.fouls,
            sms.fouled,
            spn.miscontrols,
            sms.aerials_won,
            sms.aerials_won_pct,
            sms.own_goals,
            sms.ball_recoveries,
            sda.tackles_def_3rd,
            sda.clearances,
            sps.passes_short,
            sps.passes_medium
            
        FROM
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_possession_summary spn ON ms.player_id = spn.player_id AND ms.estadistica_id = spn.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
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


def get_stats_to_offensive_player_and_presion_alta_type_of_delantero_extremo(match_id, season, specific_position_id):
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
            ss.take_ons,
            ss.take_ons_won,
            sda.tackles,
            sda.tackles_won,
            sda.tackles_att_3rd,
            sda.interceptions,
            sda.blocks,
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            spn.progressive_carries,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,  
            sps.crosses_into_penalty_area,
            spn.passes_received,
            spn.progressive_passes_received,
            sps.assisted_shots,
            ss.xg_assist,
            ss.gca,
            ss.sca,
            ss.xg,
            ss.npxg,
            spn.dispossessed,
            spn.take_ons_won_pct,
            spn.take_ons_tackled,
            spts.passes_offsides,
            spts.passes_blocked,
            spts.crosses,
            sda.tackles_interceptions,
            sda.challenges,
            sda.challenge_tackles,
            sms.fouls,
            sms.fouled,
            sda.clearances,
            sms.aerials_won,
            sms.aerials_won_pct,
            sms.own_goals,
            sms.ball_recoveries,
            sps.passes_medium
            
        FROM

            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
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




