
#### DEFENSIVE BLOCK ####

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensas laterales")
    

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            challenge_tackles,
            challenge_tackles_pct,
            blocks,
            interceptions,
            tackles_interceptions,
            clearances,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,
            passes_received,
            progressive_passes_received,
            passes_completed,
            passes_pct,
            passes_completed_short,
            passes_completed_medium,
            passes_completed_long,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area



        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa centrales")


    query = f"""
        SELECT

            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            challenge_tackles,
            challenge_tackles_pct,
            blocks,
            interceptions,
            tackles_interceptions,
            clearances,
            errors,
            touches_def_pen_area,
            touches_def_3rd,
            passes_received,
            progressive_passes_received,
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            ball_recoveries,
            aerials_won,
            aerials_won_pct

        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query




# MIDFIELDERS DEFENSIVE BLOCK

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y  mediocentros defensivos\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
            blocks,
            interceptions,
            tackles_interceptions,
            clearances,
            errors,
            touches_def_pen_area,
            touches_def_3rd,
            passes_received,
            progressive_passes_received,
            passes_completed,
            passes_pct,
            passes_short,
            passes_pct_short,
            passes_medium,
            passes_pct_medium,
            progressive_passes,
            ball_recoveries,
            aerials_won,
            aerials_won_pct

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa mediocentros ofensivos\n")

    query = f"""
        SELECT    
        apssp.league_id,
        apssp.position_player,
        apssp.starter_status,
        apssp.type_of_stat,
    
        passes_completed,
        passes_pct,
        passes_progressive_distance,
        progressive_passes,
        passes_into_final_third,
        passes_into_penalty_area,
        pass_xa,
        take_ons,
        take_ons_won_pct,
        carries_progressive_distance,
        progressive_carries,
        carries_into_final_third,
        passes_received,
        progressive_passes_received,
        shots,
        shots_on_target,
        xg,
        npxg,
        gca,
        touches_att_3rd,
        touches_att_pen_area,
        fouled,
        interceptions,
        tackles_won,
        ball_recoveries,
        aerials_won_pct

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa mediocentros creativo\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            challenge_tackles,
            challenge_tackles_pct,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            fouls,
            ball_recoveries,
            aerials_won,
            aerials_won_pct,
            progressive_carries,
            carries,
            carries_progressive_distance,
            touches,
            touches_mid_3rd,
            take_ons,
            take_ons_won_pct,
            passes_received,
            progressive_passes_received,
            progressive_passes,
            passes_completed,
            passes_pct,
            passes_into_final_third

    
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query
    


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa mediocentros lateral\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            challenge_tackles,
            challenge_tackles_pct,
            blocks,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            ball_recoveries,
            aerials_won,
            aerials_won_pct,
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_live_ball,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            passes_completed_short,
            passes_short,
            passes_pct_short,
            passes_into_final_third,
            gca
    
    
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




# FORWARD DEFENSIVE BLOCK

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y delanteros centros \n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            sca,
            tackles_att_3rd,
            tackles_mid_3rd,
            tackles_won,
            challenge_tackles,
            challenge_tackles_pct,
            blocks,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            touches_att_3rd,
            touches_live_ball,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            carries,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            passes_received,
            progressive_passes_received,
            passes_into_final_third,
            passes_into_penalty_area,
            passes_completed_short,
            passes_pct_short
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    return query


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque medio y defensa mediocentros defensivos\n")

    
    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            sca,
            tackles_att_3rd,
            tackles_mid_3rd,
            tackles_won,
            interceptions,
            blocks,
            blocked_passes,
            tackles_interceptions,
            challenge_tackles,
            challenge_tackles_pct,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            passes_received,
            progressive_passes_received,
            touches_att_3rd,
            touches_att_pen_area,
            touches_live_ball,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            pass_xa,
            passes_completed_short,
            passes_pct_short,
            ball_recoveries,
            aerials_won,
            offsides

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query