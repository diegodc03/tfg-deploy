

# DEFENDERS


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa laterales")
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
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa centrales")

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
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,

            -- TOQUES
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,

            -- CARRIES
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,

            -- REGATES
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- ERRORES Y PÉRDIDAS
            miscontrols,
            dispossessed,

            -- RECEPCIÓN DE PASES
            passes_received,
            progressive_passes_received,

            -- DEFENSIVA
            interceptions,
            tackles,
            tackles_won,
            tackles_interceptions,
            errors,
            ball_recoveries
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""

        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
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
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,

            -- RECEPCIÓN DE PASES
            progressive_passes_received,
            passes_received,

            -- CREACIÓN DE OCASIONES
            xg_assist,
            assisted_shots,
            sca,
            gca,

            -- TOQUES
            touches,
            touches_live_ball,
            touches_mid_3rd,
            touches_att_3rd,

            -- CARRIES
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,

            -- REGATES Y POSESIÓN
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            miscontrols,
            dispossessed,

            -- DISCIPLINA
            fouls,
            fouled,

            -- DEFENSA
            interceptions,
            tackles,
            tackles_won,
            ball_recoveries,

            -- JUEGO AÉREO
            aerials_won,
            aerials_lost,
            aerials_won_pct
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query



def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_creativo(season, specific_position_id):
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
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,

            -- CREACIÓN DE OCASIONES
            xg_assist,
            assisted_shots,
            sca,
            gca,


            -- CARRIES
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,

            -- TOQUES
            touches,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,
            touches_live_ball,

            -- REGATES
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            take_ons_tackled_pct,

            -- RECUPERACIÓN Y DEFENSA
            ball_recoveries,
            tackles,
            tackles_won,
            tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            interceptions,
            tackles_interceptions,
            fouls,
            fouled,

            -- PÉRDIDAS DE BALÓN
            miscontrols,
            dispossessed,

            -- RECEPCIÓN DE PASES
            progressive_passes_received,
            passes_received
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query
    


def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_lateral(season, specific_position_id):
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
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,

            -- REGATES Y POSESIÓN
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            miscontrols,
            dispossessed,

            -- RECEPCIÓN DE PASES
            progressive_passes_received,
            passes_received,

            -- CREACIÓN DE OCASIONES
            xg_assist,
            assisted_shots,
            sca,
            gca,

            -- TOQUES
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_att_pen_area,
            touches_live_ball,

            -- DEFENSA
            tackles,
            tackles_won,
            tackles_mid_3rd,
            tackles_att_3rd,
            interceptions,
            tackles_interceptions,
            ball_recoveries,
            fouls,
            fouled
            
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query





# FORWARDS

def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_delantero_centro(season, specific_position_id):
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
            aerials_lost
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query

def get_avg_stats_to_offensive_player_and_tiki_taka_type_of_delantero_extremo(season, specific_position_id):
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
            aerials_lost
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


