
# Estadisticas importantes para todas las posiciones
stats_importants = [
    "goals",
    "assists",
    "shots",
    "shots_on_target",
    "xg",
    "npxg",
    "xg_assist"
    "passes_pct",
]



# Estadísticas importantes para cada posicion del campo


def get_avg_stats_for_forwards(league_id, query_to_search_category_id):
    query = f"""
        SELECT 
            league_id,
            position_player,
            starter_status,
            type_of_stat,
            goals,
            assists,
            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            sca,
            gca,

            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_penalty_area,
            assisted_shots,

            take_ons,
            take_ons_won,
            crosses,
            touches,
            touches_att_3rd,
            touches_att_pen_area
        FROM 
            avg_player_stats_by_basic_positions av
        WHERE av.league_id = {league_id} AND av.position_player = ({query_to_search_category_id}) 
    """
    return query


def get_avg_stats_for_midfielders(league_id, query_to_search_category_id):

    query = f"""
        SELECT  
            league_id,
            position_player,
            starter_status,
            type_of_stat,

            sca,
            gca,
            interceptions,

            passes_pct,
            crosses,
            progressive_passes,
            passes_into_penalty_area,
            passes_total_distance,
            passes_progressive_distance,
            passes_pct_short,
            passes_pct_medium,
            passes_pct_long,
            passes_into_final_third,
            touches,
            take_ons_won_pct,
            take_ons_tackled,
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            miscontrols,
            dispossessed,
            passes_received,
            progressive_passes_received

        FROM 
            avg_player_stats_by_basic_positions av
            WHERE av.league_id = {league_id} AND av.position_player = ({query_to_search_category_id})
    """
    return query


def get_avg_stats_for_defenders(league_id, query_to_search_category_id):

    query = f"""
        SELECT 
            league_id,
            position_player,
            starter_status,
            type_of_stat,

            passes_pct,

            
            carries,
            carries_distance,
            carries_progressive_distance,
            miscontrols,
            dispossessed,
            passes_received,

            tackles,
            tackles_won,
            blocks,
            blocked_shots,
            blocked_passes,
            interceptions,
            clearances,
            errors,
            challenge_tackles_pct,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            tackles_interceptions,
            
            -- Estadísticas de duelos aéreos
            aerials_won_pct

        FROM 
            avg_player_stats_by_basic_positions av
            WHERE av.league_id = {league_id} AND av.position_player = ({query_to_search_category_id})
    """
    return query



def get_avg_stats_for_goalkeepers(league_id, query_to_search_category_id):

    query = f"""
        SELECT 
            league_id,
            position_player,
            starter_status,
            type_of_stat,

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
            avg_player_stats_by_basic_positions av
            WHERE av.league_id = {league_id} AND av.position_player = ({query_to_search_category_id})
    """
    return query

        

dict_positions_avg = {
    "forwards": get_avg_stats_for_forwards,
    "midfielders": get_avg_stats_for_midfielders,
    "defenders": get_avg_stats_for_defenders,
    "goalkeepers": get_avg_stats_for_goalkeepers
}