



def get_avg_stats_to_defensive_player_and_contraataque_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")


    query = f"""
        SELECT

            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            passes_completed,
            passes_total_distance,
            passes_progressive_distance,
            progressive_passes,
            carries,
            progressive_carries,
            crosses,
            crosses_into_penalty_area,
            shots,
            shots_on_target,
            touches,
            passes_into_final_third,
            passes_into_penalty_area,
            through_balls,
            take_ons,
            take_ons_won,
            carries_distance,
            passes_pct,
            progressive_passes_received
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query
            


def get_avg_stats_to_defensive_player_and_contraataque_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")


    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            passes_completed,
            passes_total_distance,
            passes_progressive_distance, 
            progressive_passes,
            carries,
            progressive_carries,
            passes_into_final_third,
            passes_into_penalty_area,
            through_balls,
            clearances,
            interceptions,
            tackles,
            progressive_passes_received,
            touches,
            take_ons,
            take_ons_won,
            passes_pct,
            passes_completed_long,
            carries_distance
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query



# MIDFIELDERS

def get_avg_stats_to_defensive_player_and_contraataque_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles
            tackles_won
            tackles_def_3rd
            tackles_mid_3rd
            tackles_interceptions
            interceptions
            clearances
            blocks
            blocked_passes
            errors
            ball_recoveries
            aerials_won
            aerials_won_pct
            progressive_passes
            passes_completed_long
            passes_pct_long
            passes_progressive_distance
            passes_into_final_third
            progressive_carries
            carries_distance
            miscontrols
            dispossessed
            passes_received
            progressive_passes_received
            fouls
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
        """
    return query



def get_avg_stats_to_defensive_player_and_contraataque_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            progressive_passes
            passes_into_final_third
            passes_into_penalty_area
            assisted_shots
            pass_xa
            assists
            xg_assist
            sca
            gca
            take_ons
            take_ons_won
            take_ons_won_pct
            progressive_carries
            carries_into_final_third
            carries_into_penalty_area
            passes_received
            progressive_passes_received
            shots
            shots_on_target
            xg
            npxg
            touches_att_3rd
            touches_att_pen_area
            fouled
            ball_recoveries
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
        """
    return query



def get_avg_stats_to_defensive_player_and_contraataque_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            progressive_passes
            passes_into_final_third
            passes_into_penalty_area
            through_balls
            passes_completed_long
            passes_pct_long
            passes_completed_medium
            passes_pct_medium
            xg_assist
            sca
            gca
            take_ons
            take_ons_won
            take_ons_won_pct
            progressive_carries
            carries_into_final_third
            carries_into_penalty_area
            passes_received
            progressive_passes_received
            ball_recoveries
            interceptions
            tackles
            tackles_won
            tackles_interceptions
            blocks
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
        """
    return query


def get_avg_stats_to_defensive_player_and_contraataque_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")
    
    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            progressive_passes
            passes_into_final_third
            passes_into_penalty_area
            crosses_into_penalty_area
            assisted_shots
            pass_xa
            assists
            take_ons
            take_ons_won
            take_ons_won_pct
            carries
            progressive_carries
            carries_progressive_distance
            carries_into_final_third
            carries_into_penalty_area
            passes_received
            progressive_passes_received
            touches_att_3rd
            touches_att_pen_area
            tackles_att_3rd
            challenge_tackles
            challenges
            interceptions
            ball_recoveries
            dispossessed
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
        """
    return query
    
# FORWARD

def get_avg_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            shots
            shots_on_target
            xg
            npxg
            xg_assist
            sca
            gca
            pens_made
            pens_att
            assisted_shots
            progressive_passes
            passes_into_final_third
            passes_into_penalty_area
            passes_completed
            passes_pct
            passes_completed_short
            passes_short
            passes_pct_short
            take_ons
            take_ons_won
            take_ons_tackled
            take_ons_tackled_pct
            aerials_won
            aerials_lost
            aerials_won_pct
        
       FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
        """
    return query


def get_avg_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos \n")

    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            shots
            shots_on_target
            xg
            npxg
            xg_assist
            assisted_shots
            progressive_passes
            passes_into_final_third
            passes_into_penalty_area
            crosses_into_penalty_area
            passes_completed
            passes_pct
            carries
            progressive_carries
            carries_into_final_third
            take_ons
            take_ons_won
            take_ons_tackled
            take_ons_tackled_pct
            passes_received
            progressive_passes_received
            aerials_won
            aerials_lost
            aerials_won_pct
            fouled
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    
    """
    return query
