####### Bloque Bajo


### DEFENSIVE STATS
def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa laterales")


    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
        
            interceptions,
            blocks,
            clearances,
            errors,
            tackles_def_3rd,
            blocked_shots,
            blocked_passes,
            ball_recoveries,
            aerials_won,
            passes_blocked,
            challenges,
            challenge_tackles_pct,
            passes_received
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
        
        
    """
    print("Query para laterales:", query)
    return query
    
positions = [
        ['FB', 'LB', 'RB'],
        ['CB', 'CDM'],
        ['LW', 'RW', 'LM', 'RM'],
        ['CAM', 'CF'],
        ['ST'],
        ['GK']
    ]


            
# Specific positions for each type of player tiene una union con todas las posiciones de los jugadores
# y se le asigna un nombre a cada una de las posiciones para poder hacer la union con el resto de los jugadores    


def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa centrales")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            take_ons_won_pct,
            interceptions,
            blocks,
            clearances,
            errors,
            fouls,
            touches_def_pen_area,
            blocked_shots,
            blocked_passes,
            ball_recoveries,
            passes_pct,
            progressive_passes,
            challenges,
            challenge_tackles_pct,
            touches_def_3rd,
            offsides,
            passes_received,
            crosses
    FROM
        avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    print("Query para defensas centrales:", query)
    return query



#### CENTROCAMPISTAS ####

def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros defensivos\n")

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
            miscontrols,
            dispossessed,
            passes_completed,
            passes,
            passes_pct,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_short,
            passes_pct_short,
            passes_into_final_third,
            passes_into_penalty_area
            
            FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    print("Query para mediocentros defensivos:", query)
    return query




def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros ofensivos\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_mid_3rd,
            interceptions,
            clearances,
            touches,
            touches_att_3rd,
            touches_att_pen_area,
            take_ons,
            take_ons_won,
            carries,
            carries_progressive_distance,
            carries_into_final_third,
            carries_into_penalty_area,
            passes_received,
            progressive_passes_received,
            passes_completed,
            passes_pct,
            passes_progressive_distance,
            passes_completed_medium,
            passes_medium,
            xg_assists,
            assisted_shots,
            passes_into_final_third,
            passes_into_penalty_area,
            progressive_passes


        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    print("Query para mediocentros ofensivos:", query)
    return query









def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros creativo\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            tackles,
            tackles_won,
            tackles_def_3rd,
            interceptions,
            clearances,
            ball_recoveries,
            aerials_won_pct,
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            passes_progressive_distance,
            passes_short,
            passes_pct_short,
            passes_medium,
            passes_pct_medium,
            passes_long,
            passes_pct_long,
            xg_assists,
            take_ons,
            take_ons_won,
            progressive_passes_received,
            touches_mid_3rd,
            carries_into_final_third



        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    print("Query para mediocentros creativos:", query)
    return query
    
    
    
def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y defensa mediocentros lateral\n")

    
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
        blocks,
        interceptions,
        clearances,
        touches,
        touches_def_3rd,
        touches_mid_3rd,
        touches_live_ball,
        take_ons,
        take_ons_won,
        progressive_carries,
        carries,
        carries_into_final_third,
        passes_completed,
        passes_pct,
        passes_into_final_third,
        passes_completed_short,
        passes_short,
        progressive_passes,
        xg_assists,
        ball_recoveries,
        aerials_won_pct

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




#### DELANTEROS ####

def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y delantero centro\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            shots,
            shots_on_target,
            tackles,
            tackles_won,
            interceptions,
            blocks,
            xg,
            npxg,
            xg_assists,
            sca,
            gca,
            passes_completed,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assisted_shots,
            passes_received,
            progressive_passes_received,
            clearances,
            fouls,
            ball_recoveries

    FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """

    return query





def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo bloque bajo y delantero extremo\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            shots,
            shots_on_target,
            tackles,
            tackles_won,
            interceptions,
            blocks,
            xg,
            npxg,
            xg_assists,
            passes_completed,
            passes_pct,
            progressive_passes,
            carries,
            progressive_carries,
            take_ons,
            take_ons_won,
            passes_received,
            progressive_passes_received,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,
            fouls,
            fouled,
            dispossessed
            
        
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query