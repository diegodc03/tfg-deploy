

# DEFENDERS


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y defensa laterales")
    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            apssp.tackles,
            apssp.interceptions,
            apssp.clearances,
            apssp.blocks,
            apssp.crosses,
            apssp.take_ons,
            apssp.take_ons_won,
            apssp.passes_completed,
            apssp.passes_pct,
            
            apssp.progressive_passes,
            apssp.fouls,
            apssp.fouled,
            apssp.ball_recoveries,
            apssp.aerials_won,
            apssp.passes_completed_long,
            apssp.assisted_shots,
            apssp.touches
            
        FROM 
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query



def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y defensa centrales")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            interceptions,
            clearances,
            blocks,
            tackles_won,
            aerials_won,
            ball_recoveries,
            fouls,
            fouled,
            errors,
            
            passes_completed,
            passes_pct,
            progressive_passes,
            
            passes_completed_long,
            challenge_tackles,
            blocked_shots,
            crosses
        FROM 
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query



# MIDFIELDERS



def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo tiki taka y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            passes_completed,
            passes_pct,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            progressive_passes,
            passes_into_final_third,
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_live_ball,
            carries,
            carries_progressive_distance,
            progressive_carries,
            passes_received,
            interceptions,
            tackles,
            tackles_won,
            tackles_interceptions,
            ball_recoveries,
            dispossessed,
            miscontrols,
            take_ons,
            take_ons_won
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y  mediocentros ofensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            xg_assist,
            assisted_shots,
            sca,
            gca,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            passes_received,
            progressive_passes_received,
            touches_att_3rd,
            touches_att_pen_area,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            ball_recoveries,
            tackles_att_3rd
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query



def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y  mediocentros creativos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
           
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes_received,
            passes_received,
            xg_assist,
            assisted_shots,
            sca,
            gca,
            touches,
            touches_mid_3rd,
            touches_att_3rd,
            progressive_carries,
            carries_into_final_third,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            interceptions,
            ball_recoveries
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query
    


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y  mediocentros laterales")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            passes_completed,
            passes_pct,
            passes_progressive_distance,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_into_final_third,
            progressive_passes,
            crosses_into_penalty_area,
            take_ons,
            take_ons_won,
            progressive_carries,
            carries_into_final_third,
            passes_received,
            progressive_passes_received,
            xg_assist,
            assisted_shots,
            sca,
            gca
            
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query





# FORWARDS

def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y  delanteros centro")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            goals,
            assists,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            sca,
            gca,
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            assisted_shots,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_received,
            progressive_passes_received,
            aerials_won,
            take_ons_won
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query

def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego  ofensivo tiki taka y  delanteros extremos")


    query = f"""
        SELECT

            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            goals,
            assists,
            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assisted_shots,
            passes_completed_short,
            passes_pct_short,
            carries,
            progressive_carries,
            take_ons,
            take_ons_won,
            passes_received,
            progressive_passes_received,
            take_ons_tackled_pct
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


