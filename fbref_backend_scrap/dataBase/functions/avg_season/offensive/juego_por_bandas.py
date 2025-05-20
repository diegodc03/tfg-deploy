

# DEFENDERS



def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            -- Defensive Actions
            passes_completed,
            passes_total_distance,
            passes_progressive_distance,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses,
            crosses_into_penalty_area,
            carries,
            progressive_carries,
            carries_into_final_third,
            touches_att_3rd,
            touches_att_pen_area,
            take_ons,
            take_ons_won,
            passes_switches,
            through_balls, 
            progressive_passes_received,
            passes_pct
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query





def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")
    

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- Defensive Actions
            passes_completed,
            passes_total_distance,
            passes_progressive_distance,
            progressive_passes,
            passes_completed_long,
            passes_into_final_third,
            passes_into_penalty_area,
            through_balls,
            progressive_passes_received,
            carries,
            progressive_carries,
            carries_distance,
            touches_mid_3rd,
            clearances,
            interceptions,
            tackles,
            blocks,
            passes_pct,
            take_ons,
            take_ons_won
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query



# MIDFIELDERS

def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- DEFENSIVA
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

            -- PASES
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            crosses,
            
            passes,
            passes_completed,
            passes_pct,
            passes_short,
            passes_medium,
            passes_long,
            progressive_passes,

            -- RECEPCIÓN
            passes_received,
            progressive_passes_received,

            -- REGATES / POSESIÓN
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

            -- TOQUES
            touches,
            touches_def_pen_area,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,

            -- ERRORES y DUELLOS
            miscontrols,
            dispossessed,
            fouls,
            fouled,
            offsides,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- CREACIÓN
            gca,
            sca,
            assists
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
           
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,
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
            pass_xa,
            assisted_shots,
            through_balls,
            passes_switches,
            crosses,
            
            -- DEFENSIVA
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            blocks,
            interceptions,
            tackles_interceptions,
            challenges,
            challenge_tackles_pct AS challenges_pct,

            -- RECEPCIÓN Y POSESIÓN
            passes_received,
            progressive_passes_received,
            miscontrols,
            dispossessed,
            fouls,
            fouled,
            ball_recoveries,
            
            -- DUELOS AÉREOS
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- REGATES
            take_ons,
            take_ons_won,
            take_ons_won_pct
                
           
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query




def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- OFENSIVA
            shots,
            shots_on_target,
            xg_assist,
            assisted_shots,

            -- DISTRIBUCIÓN
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_completed_long,
            passes_pct_long,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            crosses,
            passes_live,
            through_balls,
            passes_switches,
            throw_ins,

      

            -- REGATES Y POSESIÓN
            take_ons,
            take_ons_won,
            progressive_carries,
            passes_received,
            progressive_passes_received,
            dispossessed,

            -- DEFENSIVA
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            fouls,
            fouled,
            aerials_won,
            aerials_lost,
            aerials_won_pct
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query






def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- PASES
            passes_completed,
            passes,
            passes_pct,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
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
            assisted_shots,
            xg_assist,
            
            crosses,
            throw_ins,
            through_balls,
            passes_switches,

            -- DEFENSA
            tackles,
            tackles_won,
            tackles_mid_3rd,
            tackles_att_3rd,
            tackles_def_3rd,
            interceptions,
            tackles_interceptions,
            blocks,
            blocked_shots,
            blocked_passes,
            clearances,
            challenges,
            challenge_tackles,
            challenge_tackles_pct,

            -- REGATES Y CONTROL
            touches,
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
            passes_received,
            progressive_passes_received,
            dispossessed,
            miscontrols,

            -- FALTAS Y JUEGO AÉREO
            fouls,
            fouled,
            offsides,
            aerials_won,
            aerials_lost
           
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query



# FORWARDERS

def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")



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
            passes_completed_short,
            passes_short,
            passes_pct_short,
            passes_completed_medium,
            passes_medium,
            passes_pct_medium,
            take_ons,
            take_ons_won,
            take_ons_tackled,
            take_ons_tackled_pct,
            aerials_won,
            aerials_lost,
            touches,
            touches_att_3rd,
            touches_att_pen_area,
            take_ons_won_pct,
            miscontrols,
            dispossessed,
            crosses,
            fouls,
            fouled
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query






def get_avg_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

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
            passes_completed,
            passes_pct,
            progressive_passes,
            carries,
            progressive_carries,
            take_ons,
            take_ons_won,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            assisted_shots,
            passes_received,
            progressive_passes_received,
            passes_completed_short,
            passes_short,
            passes_pct_short,
            take_ons_tackled,
            take_ons_tackled_pct,
            aerials_won,
            aerials_lost,
            touches,
            touches_att_3rd,
            touches_att_pen_area,
            take_ons_won_pct,
            miscontrols,
            dispossessed,
            crosses,
            fouls,
            fouled
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    """
    return query


