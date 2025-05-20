

# DEFENDERS

def get_avg_stats_to_offensive_player_and_presion_alta_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")
    query = f"""
        SELECT 
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- Defensive Actions
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
            
            -- Possession
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
            miscontrols,
            dispossessed,
            passes_received,
            progressive_passes_received,
            
            -- Passing
            passes_completed,
            passes,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_short,
            passes_completed_medium,
            passes_medium,
            passes_completed_long,
            passes_long,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,
            
            -- Miscellaneous
            fouls,
            fouled,
            cards_yellow,
            cards_red,
            offsides,
            aerials_won

        FROM 
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    
    return query





def get_avg_stats_to_offensive_player_and_presion_alta_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")


    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            -- Defensive Actions
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
            
            -- Passing
            passes_completed,
            passes_total_distance,
            passes_progressive_distance,
            passes_completed_short,
            passes_short,
            passes_completed_medium,
            passes_medium,
            passes_completed_long,
            passes_long,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,
            
            -- Miscellaneous
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            touches_live_ball,
            aerials_won,
            aerials_lost,
            ball_recoveries

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    return query


# MIDFIELDERS


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_defensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- DEFENSA
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
            offsides,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- REGATES Y POSESIÓN
            take_ons,
            take_ons_won,
            
            take_ons_won_pct,
            take_ons_tackled,
            miscontrols,
            dispossessed,

            -- PASES
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            progressive_passes_received,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_received,
            passes_blocked,
            passes_live,
            passes_dead,
            passes_free_kicks,
            through_balls,
            passes_switches,
            crosses

            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 




def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            
            -- Métricas de XG (Expected Goals)
            xg,
            npxg,
            xg_assist,
            sca,
            gca,

            -- PASES
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            
            passes_received,
            progressive_passes_received,

            -- TOQUES
            touches,
            touches_mid_3rd,
            touches_att_3rd,

            -- REGATES
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- PASES EN LARGO Y CORTO
            through_balls,
            passes_switches,
            passes_completed_short,
            passes_pct_short,
            passes_completed_medium,
            passes_pct_medium,
            passes_completed_long,
            passes_pct_long,

            -- ASISTENCIAS Y GOL
            assists,
            assisted_shots,

            -- OTRAS ESTADÍSTICAS DE PASES
            passes_offsides,
            passes_blocked,

           -- DEFENSA
            tackles_won,
            interceptions,
            clearances,
            fouls,
            fouled,

            -- CRUCES Y BALONES GANADOS
            crosses,
            ball_recoveries,
            aerials_won
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 



def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_creativo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            -- Métricas de XG (Expected Goals)
            xg,
            npxg,
            xg_assist,
            sca,
            gca,

            -- PASES
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_received,
            progressive_passes_received,

            -- TACKLES Y DEFENSA
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

            -- OTRAS ESTADÍSTICAS DE DEFENSA
            fouls,
            fouled,
            passes_offsides,
            passes_blocked,
            miscontrols,
            dispossessed,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- REGATES
            take_ons,
            take_ons_won,
            take_ons_won_pct,

            -- ESTADÍSTICAS DE PASES
            passes_switches,
            throw_ins,
 
            -- TACKLES ADICIONALES
            tackles,
            take_ons_tackled
            
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 
    
    
    

def get_avg_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_lateral(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
        
        -- TACKLES Y DEFENSA
        tackles,
        tackles_won,
        tackles_def_3rd,
        tackles_mid_3rd,
        tackles_att_3rd,
        interceptions,
        blocks,
        
        -- PASES
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
        
        -- TACKLES E INTERCEPCIONES
        tackles_interceptions,
        challenges,
        challenge_tackles_pct,
        challenged_lost,
        
        -- OTRAS ESTADÍSTICAS DEFENSIVAS
        clearances,
        errors,
        fouls,
        fouled,
        miscontrols,
        dispossessed,
        
        -- BALONES AÉREOS
        aerials_won,
        aerials_won_pct,
        aerials_lost,
        
        -- PASES DETALLADOS
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
        passes_pct_long
           
           
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 




# forwards


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            shots,
            shots_on_target,
            take_ons,
            take_ons_won,
            tackles,
            tackles_won,
            tackles_att_3rd,
            interceptions,
            blocks,
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            progressive_carries,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_received,
            progressive_passes_received,
            assisted_shots,
            xg_assist,
            gca,
            sca,
            xg,
            npxg,
            dispossessed,
            take_ons_won_pct,
            take_ons_tackled,
            passes_offsides,
            passes_blocked,
            crosses,
            tackles_interceptions,
            challenges,
            challenge_tackles,
            fouls,
            fouled,
            miscontrols,
            aerials_won,
            aerials_won_pct,
            own_goals,
            ball_recoveries,
            tackles_def_3rd,
            clearances,
            passes_short,
            passes_medium
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query 


def get_avg_stats_to_offensive_player_and_presion_alta_type_of_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            shots,
            shots_on_target,
            take_ons,
            take_ons_won,
            tackles,
            tackles_won,
            tackles_att_3rd,
            interceptions,
            blocks,
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            progressive_carries,
            passes_into_final_third,
            passes_into_penalty_area,  
            crosses_into_penalty_area,
            passes_received,
            progressive_passes_received,
            assisted_shots,
            xg_assist,
            gca,
            sca,
            xg,
            npxg,
            dispossessed,
            take_ons_won_pct,
            take_ons_tackled,
            passes_offsides,
            passes_blocked,
            crosses,
            tackles_interceptions,
            challenges,
            challenge_tackles,
            fouls,
            fouled,
            clearances,
            aerials_won,
            aerials_won_pct,
            own_goals,
            ball_recoveries,
            passes_medium
            
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query





