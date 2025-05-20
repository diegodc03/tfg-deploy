
#### DEFENSIVE BLOCK ####

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_defense_laterales(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")
    

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,
            
            Tackles_def_3rd,
            tackles_mid_3rd,
            tackles_att_3rd,
            challenge_tackles,
            challenges,
            challenge_tackles_pct,
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
            touches_att_pen_area,
            touches_live_ball,
            miscontrols,
            dispossessed,
            passes_received,
            progressive_passes_received,
            passes_completed,
            passes,
            passes_pct,
            passes_short,
            passes_medium,
            passes_long,
            passes_completed_short,
            passes_completed_medium,
            passes_completed_long,
            xg_assists,
            pass_xa,
            assisted_shots,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            progressive_passes,
            passes_live,
            passes_dead,
            passes_free_kicks,
            through_balls,
            passes_switches,
            crosses,
            throw_ins,
            corner_kicks,
            corner_kicks_in,
            corner_kicks_out,
            corner_kicks_straight,
            passes_offsides,
            passes_blocked,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_defense_central_defenders(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos")


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
            miscontrols,
            dispossessed,
            passes_received,
            progressive_passes_received,
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
            xg_assists,
            pass_xa,
            passes_into_final_third,
            passes_into_penalty_area,
            crosses_into_penalty_area,
            passes_offsides,

            passes_blocked,
            fouls,
            fouled,
            offsides,
            own_goals,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            take_ons_tackled_pct
        
        FROM
            avg_player_stats_by_specific_positions apssp
            WHERE apssp.league_id = {season} 
            AND apssp.position_player = ({specific_position_id})
    """
    return query




# MIDFIELDERS DEFENSIVE BLOCK

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_defensivo(season, specific_position_id):
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
            take_ons_won,
            take_ons_tackled,
            take_ons_tackled_pct,
            passes_received,
            progressive_passes_received,

            -- Passing Summary (sps)
            passes_into_final_third,
            passes_into_penalty_area,
            passes_completed,
            passes_pct,
            passes_short,
            passes_pct_short,
            passes_medium,
            passes_pct_medium,
            passes_long,
            passes_pct_long,
            progressive_passes,
            passes_total_distance,
            passes_progressive_distance,

            -- Pass Types Summary (spts)
            passes_offsides,
            passes_blocked,

            -- Miscellaneous Summary (sms)
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,
            fouls,
            fouled,
            pens_conceded,
            own_goals

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_ofensivo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego defensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT    
        apssp.league_id,
        apssp.position_player,
        apssp.starter_status,
        apssp.type_of_stat,
    
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

        pass_xa,
        assisted_shots,

        take_ons,
        take_ons_won,
        take_ons_won_pct,

        carries,
        carries_distance,
        carries_progressive_distance,
        progressive_carries,
        carries_into_final_third,
        carries_into_penalty_area,

        passes_received,
        progressive_passes_received,

        shots,
        xg_assist,
        shots_on_target,
        pens_made,
        pens_att,
        xg,
        npxg,
        sca,
        gca,

        touches,
        touches_mid_3rd,
        touches_att_3rd,
        touches_att_pen_area,
        touches_live_ball,

        fouled,

        interceptions,
        tackles,
        tackles_won,
        blocks,
        ball_recoveries,
        miscontrols,
        dispossessed,

        aerials_won,
        aerials_lost,
        aerials_won_pct
        
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_creativo(season, specific_position_id):
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
            challenges,
            challenge_tackles,
            challenge_tackles_pct,
            blocked_shots,
            blocked_passes,
            interceptions,
            tackles_interceptions,
            clearances,
            
            
            -- Miscellaneous (sms)
            fouls,
            fouled,
            offsides,
            pens_won,
            pens_conceded,
            own_goals,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- Possession
            
            progressive_carries,
            carries,
            carries_distance,
            carries_progressive_distance,
            touches,
            touches_def_3rd,
            touches_mid_3rd,
            touches_att_3rd,
            take_ons,
            take_ons_won,
            take_ons_won_pct,
            take_ons_tackled,
            take_ons_tackled_pct,
            passes_received,
            progressive_passes_received,

            -- Passing
            progressive_passes,
            passes_completed,
            passes,
            passes_pct,
            passes_short,
            passes_pct_short,
            passes_medium,
            passes_pct_medium,
            passes_long,
            passes_pct_long,
            passes_into_final_third,
            passes_into_penalty_area

    
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query
    


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_lateral(season, specific_position_id):
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
            fouls,
            fouled,
            offsides,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct,

            -- Possession & touches
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
            miscontrols,
            dispossessed,

            -- Passing
            passes_completed,
            passes,
            passes_pct,
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
            progressive_passes,
            passes_total_distance,
            passes_progressive_distance,



            -- Goal creation
            gca
    
    
        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query




# FORWARD DEFENSIVE BLOCK

def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_centro(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")

    query = f"""
        SELECT
            apssp.league_id,
            apssp.position_player,
            apssp.starter_status,
            apssp.type_of_stat,

            -- Defensive Actions (d)
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

            -- Possession (pos)
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
            carries,
            carries_distance,
            carries_progressive_distance,
            progressive_carries,
            carries_into_final_third,
            carries_into_penalty_area,
            dispossessed,
            passes_received,
            progressive_passes_received, 
            
            -- Passing (ps)
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
            passes_into_penalty_area

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})

    """
    return query


def get_avg_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_extremo(season, specific_position_id):
    print("Comienzo con la adición de puntuación de stats de los jugadores por tipo de juego ofensivo y defensa mediocentros defensivos\n")

    
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

            -- Possession (pos)
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
            passes_received,
            progressive_passes_received,

            -- Passing (ps)
            passes_completed,
            passes,
            passes_pct,
            progressive_passes,
            crosses_into_penalty_area,
            xg_assists,
            pass_xa,
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

            -- Miscellaneous (m)
            fouls,
            fouled,
            offsides,
            pens_won,
            pens_conceded,
            own_goals,
            ball_recoveries,
            aerials_won,
            aerials_lost,
            aerials_won_pct

        FROM
            avg_player_stats_by_specific_positions apssp
        WHERE apssp.league_id = {season} 
        AND apssp.position_player = ({specific_position_id})
    
    """
    return query