
#### DEFENSIVE BLOCK ####

def get_stats_to_defensive_player_and_bloque_medio_type_of_defense_laterales(match_id, season, specific_position_id):
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
            sda.tackles,
            sda.tackles_won,
            sda.Tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.challenge_tackles,
            sda.challenges,
            sda.challenge_tackles_pct,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,
            psn.touches,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.touches_live_ball,
            psn.miscontrols,
            psn.dispossessed,
            psn.passes_received,
            psn.progressive_passes_received,
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.passes_short,
            sps.passes_medium,
            sps.passes_long,
            sps.passes_completed_short,
            sps.passes_completed_medium,
            sps.passes_completed_long,
            sps.xg_assists,
            sps.pass_xa,
            sps.assisted_shots,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            sps.progressive_passes,
            spts.passes_live,
            spts.passes_dead,
            spts.passes_free_kicks,
            spts.through_balls,
            spts.passes_switches,
            spts.crosses,
            spts.throw_ins,
            spts.corner_kicks,
            spts.corner_kicks_in,
            spts.corner_kicks_out,
            spts.corner_kicks_straight,
            spts.passes_offsides,
            spts.passes_blocked,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct
        FROM

            match_statistics ms
        LEFT JOIN stats_summary sm ON ms.player_id = sm.player_id AND ms.estadistica_id = sm.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
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
            ms.goals,
            ms.assists,
            sda.tackles,
            sda.tackles_won,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.challenge_tackles,
            sda.challenges,
            sda.challenge_tackles_pct,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.tackles_interceptions,
            sda.clearances,
            sda.errors,
            psn.touches,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_live_ball,
            psn.miscontrols,
            psn.dispossessed,
            psn.passes_received,
            psn.progressive_passes_received,
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
            sps.xg_assists,
            sps.pass_xa,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            spts.passes_offsides,

            spts.passes_blocked,
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.own_goals,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct
        FROM

            match_statistics ms
        LEFT JOIN stats_summary sm ON ms.player_id = sm.player_id AND ms.estadistica_id = sm.stat_id
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN stats_defensiveactions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary spts ON ms.player_id = spts.player_id AND ms.estadistica_id = spts.stat_id
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
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")
    
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
            sds.tackles_att_3rd,
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



            -- Possession Summary (psn)
            psn.touches,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.take_ons_won,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.passes_received,
            psn.progressive_passes_received,

            -- Passing Summary (sps)
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.passes_completed,
            sps.passes_pct,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_long,
            sps.passes_pct_long,
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,

            -- Pass Types Summary (spts)
            spts.passes_offsides,
            spts.passes_blocked,

            -- Miscellaneous Summary (sms)
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,
            sms.fouls,
            sms.fouled,
            sms.pens_conceded,
            sms.own_goals

        FROM match_statistics ms
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
    
    
    
def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_ofensivo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")
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
            -- Pase
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.passes_progressive_distance,
            sps.passes_completed_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_pct_long,
            sps.progressive_passes,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.crosses_into_penalty_area,
            
         
            sps.pass_xa,
            sps.assisted_shots,

            -- Regates
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,

            -- Carreras y progresión
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,

            -- Recibos
            psn.passes_received,
            psn.progressive_passes_received,

            -- Tiros y goles
            ss.shots,
        	
            
            ss.xg_assist,
            ss.shots_on_target,
           
            ss.pens_made,
            ss.pens_att,
            ss.xg,
            ss.npxg,
            ss.sca,
            ss.gca,

            -- Toques
            psn.touches,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.touches_live_ball,

            -- Faltas
            sms.fouled,

            -- Defensa
            sms.interceptions,
            sds.tackles,
            sds.tackles_won,
            sds.blocks,
            sms.ball_recoveries,
            psn.miscontrols,
            psn.dispossessed,

            -- Aéreos
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct
        
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





def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_creativo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")
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
            sds.tackles_att_3rd,
            sds.challenges,
            sds.challenge_tackles,
            sds.challenge_tackles_pct,
            sds.blocked_shots,
            sds.blocked_passes,
            sds.interceptions,
            sds.tackles_interceptions,
            sds.clearances,
            
            
            -- Miscellaneous (sms)
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.pens_won,
            sms.pens_conceded,
            sms.own_goals,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- Possession
            
            psn.progressive_carries,
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.touches,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.passes_received,
            psn.progressive_passes_received,

            -- Passing
            sps.progressive_passes,
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_long,
            sps.passes_pct_long,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area

    
        FROM match_statistics ms
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



def get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_lateral(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

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
            sds.tackles_att_3rd,
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
            
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct,

            -- Possession & touches
            psn.touches,
            psn.touches_def_pen_area,
            psn.touches_def_3rd,
            psn.touches_mid_3rd,
            psn.touches_att_3rd,
            psn.touches_att_pen_area,
            psn.touches_live_ball,
            psn.take_ons,
            psn.take_ons_won,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.take_ons_tackled_pct,
            psn.miscontrols,
            psn.dispossessed,

            -- Passing
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
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
            sps.progressive_passes,
            sps.passes_total_distance,
            sps.passes_progressive_distance,



            -- Goal creation
            ss.gca
    
    
        FROM match_statistics ms
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





#################################################################################
# FORWARD DEFENSIVE BLOCK

def get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_centro(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")


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

            -- Defensive Actions (d)
            sds.tackles,
            sds.tackles_won,
            sds.tackles_def_3rd,
            sds.tackles_mid_3rd,
            sds.tackles_att_3rd,
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

            -- Possession (pos)
            pos.touches,
            pos.touches_def_pen_area,
            pos.touches_def_3rd,
            pos.touches_mid_3rd,
            pos.touches_att_3rd,
            pos.touches_live_ball,
            pos.take_ons,
            pos.take_ons_won,
            pos.take_ons_won_pct,
            pos.take_ons_tackled,
            pos.take_ons_tackled_pct,
            pos.carries,
            pos.carries_distance,
            pos.carries_progressive_distance,
            pos.progressive_carries,
            pos.carries_into_final_third,
            pos.carries_into_penalty_area,
            pos.dispossessed,
            pos.passes_received,
            pos.progressive_passes_received,

            -- Passing (ps)
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
            sps.passes_into_penalty_area

        FROM match_statistics ms
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




def get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_extremo(match_id, season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")

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
            sds.tackles_att_3rd,
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

            -- Possession (pos)
            pos.touches,
            pos.touches_def_pen_area,
            pos.touches_def_3rd,
            pos.touches_mid_3rd,
            pos.touches_att_3rd,
            pos.touches_att_pen_area,
            pos.touches_live_ball,
            pos.take_ons,
            pos.take_ons_won,
            pos.take_ons_won_pct,
            pos.take_ons_tackled,
            pos.take_ons_tackled_pct,
            pos.passes_received,
            pos.progressive_passes_received,

            -- Passing (ps)
            sps.passes_completed,
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.crosses_into_penalty_area,
            sps.xg_assists,
            sps.pass_xa,
            sps.passes_into_final_third,
            sps.passes_into_penalty_area,
            sps.passes_completed_short,
            sps.passes_short,
            sps.passes_pct_short,
            sps.passes_completed_medium,
            sps.passes_medium,
            sps.passes_pct_medium,
            sps.passes_completed_long,
            sps.passes_long,
            sps.passes_pct_long,

            -- Miscellaneous (m)
            sms.fouls,
            sms.fouled,
            sms.offsides,
            sms.pens_won,
            sms.pens_conceded,
            sms.own_goals,
            sms.ball_recoveries,
            sms.aerials_won,
            sms.aerials_lost,
            sms.aerials_won_pct

        FROM match_statistics ms
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