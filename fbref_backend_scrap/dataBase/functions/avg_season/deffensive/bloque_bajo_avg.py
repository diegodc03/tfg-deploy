####### Bloque Bajo


### DEFENSIVE STATS
def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa laterales")


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
    return query



#### CENTROCAMPISTAS ####

def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

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

            -- Possession (psn)
            miscontrols,
            dispossessed,

            crosses_into_penalty_area,
            passes_into_final_third,
 

            -- Passing Summary (sps)
            passes_completed,
            passes,
            passes_pct,
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
            passes_into_penalty_area,
            pass_xa
            
            FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- Defensive Actions (sds)
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

            -- Possession (psn)
            touches,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,
            touches_live_ball,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            take_ons_tackled_pct,
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            miscontrols,
            dispossessed,
            passes_received,
            progressive_passes_received,

            -- Passing Summary (sps)
            passes_completed,
            passes,
            passes_pct,
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
            xg_assists,
            pass_xa,
            assisted_shots,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes
            

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query









def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- Defensive Actions (sda)
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
            challenged_lost,  -- Mapeado como tackled_lost
            blocks,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,

            -- Miscellaneous (sms)
            fouls,
            fouled,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- Passing Summary (sps)
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            passes_total_distance,
            passes_progressive_distance,
            passes_short,
            passes_pct_short,
            passes_medium,
            passes_pct_medium,
            passes_long,
            passes_pct_long,
            xg_assists,
            pass_xa,
            assisted_shots,
 
            -- Possession Summary (psn)
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            miscontrols,
            dispossessed,
            progressive_passes_received,
            touches,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,
            passes_received,
            progressive_carries,
            carries,
            carries_distance,
            carries_progressive_distance,
            carries_into_final_third,
            carries_into_penalty_area



        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query
    
    
    
def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    
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

        -- Possession Summary (psn)
        touches,
        touches_def_pen_area,
        touches_def_3rd,
        touches_mid_3rd,
        touches_att_3rd,
        touches_live_ball,
        take_ons,
        take_ons_won,
        take_ons_won_pct,
        take_ons_tackled,
        take_ons_tackled_pct,
        progressive_carries,
        carries,
        carries_distance,
        carries_progressive_distance,
        carries_into_final_third,
        carries_into_penalty_area,

        -- Passing Summary (sps)
        passes_completed,
        passes,
        passes_pct,
        passes_into_final_third,
        passes_into_penalty_area,
        passes_completed_short,
        passes_short,
        passes_pct_short,
        passes_completed_medium,
        passes_medium,
        passes_pct_medium,
        passes_completed_long,
        passes_long,
        passes_pct_long,
        passes_progressive_distance,
        progressive_passes,
        xg_assists,
        pass_xa,
        assisted_shots,
        crosses_into_penalty_area,

        -- Miscellaneous (sms)
        fouls,
        fouled,
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
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            interceptions,
            blocks,
            xg,
            npxg,
            xg_assists AS xg_assist,
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
            offsides,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,
            pens_won,
            pens_conceded,
            own_goals

    FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """

    return query





def get_avg_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")

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
            xg_assists AS xg_assist,

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
            dispossessed,
            crosses,
            throw_ins,
            corner_kicks,
            corner_kicks_in,
            corner_kicks_out,
            corner_kicks_straight,
            passes_live,
            passes_dead
            
        
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query