
# Estadísticas importantes para cada posicion del campo


def generate_query_for_forwards_players(match_id, season, basic_position_id):
    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pcr.category_id,
            t.team_id,  
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  
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
            sps.passes,
            sps.passes_pct,
            sps.progressive_passes,
            sps.passes_into_penalty_area,
            sps.assisted_shots,
            psn.take_ons,
            psn.take_ons_won,
            pt.crosses,
            psn.touches,
            psn.touches_att_3rd,
            psn.touches_att_pen_area
        FROM 
            match_statistics ms
        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_passTypes_summary pt ON ms.player_id = pt.player_id AND ms.estadistica_id = pt.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        LEFT JOIN position_category_relation pcr ON pp.position_id = pcr.position_id
        LEFT JOIN position_category pc ON pcr.category_id = pc.category_id
        
        WHERE fm.Season = {season}
            AND fm.match_id = {match_id}
            AND pp.position_id IN (
                SELECT position_id 
                FROM position_category_relation 
                WHERE category_id IN ({basic_position_id})
        )

        GROUP BY player_id
    """
    return query


def generate_query_for_midfielders_players(match_id, season, basic_position_id):
    # Convertir la lista de IDs a un formato de texto adecuado para SQL (ej: '40, 35, 46, 43')
    
    
    query = f"""
        SELECT  
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pcr.category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante

            ms.minutes,
        
            ss.sca,
            ss.gca,
            ss.interceptions,

            
            sps.passes_pct,
            pt.crosses,
            sps.progressive_passes,
            sps.passes_into_penalty_area,
            sps.passes_total_distance,
            sps.passes_progressive_distance,
            sps.passes_pct_short,
            sps.passes_pct_medium,
            sps.passes_pct_long,
            sps.passes_into_final_third,

            psn.touches,
            psn.take_ons_won_pct,
            psn.take_ons_tackled,
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.progressive_carries,
            psn.carries_into_final_third,
            psn.carries_into_penalty_area,
            psn.miscontrols,
            psn.dispossessed,
            psn.passes_received,
            psn.progressive_passes_received

        FROM 
            match_statistics ms

        LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id 
        LEFT JOIN stats_passTypes_summary pt ON ms.player_id = pt.player_id AND ms.estadistica_id = pt.stat_id
        LEFT JOIN position_category_relation pcr ON pp.position_id = pcr.position_id
        LEFT JOIN position_category pc ON pcr.category_id = pc.category_id
        
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        

        WHERE fm.Season = {season} 
            AND pp.position_id IN (
                SELECT pcr.position_id
                FROM position_category_relation pcr
                WHERE pcr.category_id IN ({basic_position_id})
            )
            AND fm.match_id = {match_id}
            
        group by player_id

    """
    return query


def generate_query_for_defenders_players(match_id, season, basic_position_id):

    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pcr.category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante

            ms.minutes,
            
            sps.passes_pct,

            
            psn.carries,
            psn.carries_distance,
            psn.carries_progressive_distance,
            psn.miscontrols,
            psn.dispossessed,
            psn.passes_received,

            sda.tackles,
            sda.tackles_won,
            sda.blocks,
            sda.blocked_shots,
            sda.blocked_passes,
            sda.interceptions,
            sda.clearances,
            sda.errors,
            sda.challenge_tackles_pct,
            sda.tackles_def_3rd,
            sda.tackles_mid_3rd,
            sda.tackles_att_3rd,
            sda.tackles_interceptions,
            
            -- Estadísticas de duelos aéreos
            sms.aerials_won_pct
            

        FROM 
            match_statistics ms

        LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
        LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id 
        LEFT JOIN stats_DefensiveActions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id  
        
        LEFT JOIN position_category_relation pcr ON pp.position_id = pcr.position_id
        LEFT JOIN position_category pc ON pcr.category_id = pc.category_id
        
        LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
        
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)
        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        

        WHERE fm.Season = {season} 
            AND pp.position_id IN (
                SELECT pcr.position_id
                FROM position_category_relation pcr
                WHERE pcr.category_id IN ({basic_position_id})
            )
            AND fm.match_id = {match_id}
            
        group by player_id
    """
    return query



def generate_query_for_goalkeepers_players(match_id, season, basic_position_id):

    query = f"""
        SELECT 
            ms.estadistica_id,
            ms.player_id,
            ms.match_id,
            pp.position_id,
            pcr.category_id,
            t.team_id,  -- Equipo del jugador en la temporada
            CASE 
                WHEN t.team_id = fm.Home THEN 'Home'
                WHEN t.team_id = fm.Away THEN 'Away'
                ELSE 'Unknown'
            END AS team_role,  -- Indica si es del equipo local o visitante
            ms.minutes,
            gk_shots_on_target_against,
            gk_goals_against,
            gk_save_pct,
            gk_psxg,
            gk_passes_pct_launched,
            gk_passes,
            gk_passes_throws,
            gk_pct_passes_launched,
            gk_goal_kicks,
            gk_crosses_stopped_pct,
            gk_def_actions_outside_pen_area,
            gk_avg_distance_def_actions

        FROM
            match_statistics ms
        LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id 
        
        LEFT JOIN stats_gk_summary sgs ON ms.player_id = sgs.player_id AND ms.estadistica_id = sgs.stat_id
        LEFT JOIN football_match fm ON ms.match_id = fm.match_id
            
        LEFT JOIN team_player tp ON ms.player_id = tp.player_id AND tp.team_id IN (fm.Home, fm.Away)

        LEFT JOIN team t ON tp.team_id = t.team_id AND fm.Season = t.tournament_team_id 
        LEFT JOIN position_category_relation pcr ON pp.position_id = pcr.position_id
        LEFT JOIN position_category pc ON pcr.category_id = pc.category_id
      
        WHERE fm.Season = {season} 
            AND pp.position_id IN (
                SELECT pcr.position_id
                FROM position_category_relation pcr
                WHERE pcr.category_id IN ({basic_position_id})
            )
            AND fm.match_id = {match_id}
            
        group by player_id
    """
    return query

        

dict_stats_position = {
    "forwards": generate_query_for_forwards_players,
    "midfielders": generate_query_for_midfielders_players,
    "defenders": generate_query_for_defenders_players,
    "goalkeepers": generate_query_for_goalkeepers_players
}