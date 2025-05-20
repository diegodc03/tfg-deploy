



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
            
            -- Defensive
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            tackles_interceptions,
            interceptions,
            blocks,
            blocked_shots,
            blocked_passes,
            clearances,
            errors,
            
            
            fouls,
            fouled,
            aerials_won,
            aerials_lost,
            aerials_won_pct,
            ball_recoveries,
    
            -- Passing
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_completed_long,
            passes_long,
            passes_pct_long,
            passes_completed_medium,
            passes_medium,
            passes_pct_medium,
            passes_total_distance,
            passes_progressive_distance,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,


            -- Possession
            take_ons,
            take_ons_won,
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

            -- Receiving
            passes_received,
            progressive_passes_received,

            -- Creation
            sca,
            gca,
            xg_assist
        
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
            
            -- Pase
            passes_completed,
            passes,
            passes_pct,
            passes_progressive_distance,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_completed_long,
            passes_pct_long,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assists,
            xg_assist,
            pass_xa,
            assisted_shots,

            -- Regates
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- Carreras y progresión
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,

            -- Recibos
            passes_received,
            progressive_passes_received,

            -- Tiros y goles
            shots,
            shots_on_target,
            goals,
            pens_made,
            pens_att,
            xg,
            npxg,
            sca,
            gca,

            -- Toques
            touches,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,
            touches_live_ball,

            -- Faltas
            fouled,

            -- Defensa
            interceptions,
            tackles,

            blocks,
            ball_recoveries,
            miscontrols,
            dispossessed,

            -- Aéreos
            aerials_won,
            aerials_lost,
            aerials_won_pct
        
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
            
            -- Pases
            passes_completed,
            passes,
            passes_pct,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_completed_long,
            passes_pct_long,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            through_balls,

            -- Regates
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- Carreras y progresión
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            -- Recibos
            passes_received,
            progressive_passes_received,

            -- Creación de gol
            sca,
            gca,

 
            xg_assist,

            -- Defensa
            tackles,
            tackles_won,
            interceptions,
            blocks,
            tackles_interceptions,
            ball_recoveries,
            clearances,
            errors,

       
            fouls,
            fouled,
            offsides,

            -- Aéreos
            aerials_won,
            aerials_lost,
            aerials_won_pct
            
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
            
            -- Pases
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_short,
            passes_pct_short,
            passes_completed_medium,
            passes_medium,
            passes_pct_medium,
            passes_completed_long,
            passes_long,
            passes_pct_long,
            assists,
            pass_xa,
            assisted_shots,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,

            -- Toques
            touches,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,

            -- Regates
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- Carreras
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,

            -- Errores y pérdidas
            miscontrols,
            dispossessed,

            -- Recibos
            passes_received,
            progressive_passes_received,

            -- Defensa
            tackles,
            tackles_won,
            tackles_mid_3rd,
            tackles_att_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
            interceptions,
            tackles_interceptions,
            clearances,
            ball_recoveries,

            -- Faltas y tarjetas
            fouls,
            fouled,
            offsides
        
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
            
            pens_made,
            pens_att,
            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,
            sca,
            gca,

            -- Passing Summary (sps)
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assisted_shots,
            passes_completed_short,
            passes_short,
            passes_pct_short,
            passes_completed_medium,
            passes_medium,
            passes_pct_medium,

            -- Possession (psn)
            take_ons,
            take_ons_won,
            take_ons_tackled,
            take_ons_tackled_pct,

            -- Miscellaneous (sms)
            aerials_won,
            aerials_lost
        
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
            
            shots,
            shots_on_target,
            xg,
            npxg,
            xg_assist,

            -- Passing Summary (ps)
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assisted_shots,
            passes_completed_short,
            passes_short,
            passes_pct_short,

            -- Possession (pos)
            carries,
            progressive_carries,
            take_ons,
            take_ons_won,
            take_ons_tackled,
            take_ons_tackled_pct,
            passes_received,
            progressive_passes_received,

            -- Miscellaneous (sms)
            aerials_won,
            aerials_lost
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    
    """
    return query
