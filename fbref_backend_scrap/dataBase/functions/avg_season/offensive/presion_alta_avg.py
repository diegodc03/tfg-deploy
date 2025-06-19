

# DEFENDERS

def get_avg_stats_to_offensive_player_and_presion_alta_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y defensa mediocentros defensivos")
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
            tackles_att_3rd,
            blocks,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            errors,
            touches,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,
            take_ons_won,
            carries,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            passes_received,
            progressive_passes_received

        FROM 
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    
    return query





def get_avg_stats_to_offensive_player_and_presion_alta_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y defensa mediocentros defensivos")


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
            challenges,
            challenge_tackles_pct,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            errors,
            passes_completed,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_completed_medium,
            passes_completed_long,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,
            touches,
            aerials_won,
            ball_recoveries

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    return query


# MIDFIELDERS


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y defensa mediocentros defensivos")

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
            tackles_att_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
            challenged_lost,
            blocks,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            errors,
            fouls,
            fouled,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            miscontrols

            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 




def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y defensa mediocentros ofensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            xg,
            npxg,
            xg_assist,
            sca,
            gca,
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_received,
            progressive_passes_received,
            touches,
            touches_mid_3rd,
            touches_att_3rd,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            through_balls,
            passes_switches,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 



def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y defensa mediocentros creativo")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            xg,
            npxg,
            xg_assist,
            sca,
            gca,
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_received,
            progressive_passes_received,
            tackles_won,
            interceptions,
            clearances,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            tackles_interceptions,
            blocks,
            blocked_shots,
            blocked_passes,
            fouls
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 
    
    
    

def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y  mediocentros lateral")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
        
        shots,
        tackles,
        tackles_won,
        tackles_def_3rd,
        tackles_mid_3rd,
        tackles_att_3rd,
        interceptions,
        blocks,
        passes_completed,
        passes,
        passes_pct,
        progressive_passes,
        progressive_carries,
        take_ons,
        take_ons_won,
        passes_received,
        progressive_passes_received,
        passes_into_final_third,
        passes_into_penalty_area,
        crosses_into_penalty_area,
        assisted_shots,
        tackles_interceptions,
        challenges,
        challenge_tackles_pct,
        clearances,
        aerials_won
           
           
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 




# forwards


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo presion alta y delantero centro")

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
            gca,
            sca,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            tackles,
            tackles_won,
            tackles_att_3rd,
            tackles_interceptions,
            interceptions,
            ball_recoveries,
            assisted_shots,
            passes_received,
            progressive_passes_received,
            progressive_carries,
            passes_into_penalty_area,
            passes_into_final_third,
            aerials_won,
            aerials_won_pct,
            fouls
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y delantero extremo")
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
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            tackles,
            tackles_won,
            tackles_att_3rd,
            tackles_interceptions,
            interceptions,
            ball_recoveries,
            fouls,
            fouled,
            assisted_shots,
            xg_assist,
            gca,
            sca,
            xg,
            npxg,
            progressive_carries,
            progressive_passes_received,
            passes_received,
            passes_into_penalty_area,
            crosses_into_penalty_area
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query





