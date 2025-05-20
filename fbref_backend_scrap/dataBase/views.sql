

/* Vistas para la posicion de delantero */
CREATE VIEW forward_stats_view_season_1 AS
SELECT 
    -- Genera un identificador único basado en player_id, match_id y statistic_id
    CONCAT(ms.player_id, '-', ms.match_id, '-', ms.estadistica_id) AS unique_id,

    ms.estadistica_id,
    ms.player_id,
    ms.match_id,
    pp.position_id,
    ms.minutes,
    ms.goals,
    ms.assists,
    ss.shots,
    ss.shots_on_target,
    ss.xg,
    ss.npxg,
    ss.xg_assist,
    ss.sca,
    ss.gca,
    -- Pases
    sps.passes_completed,
    sps.passes,
    sps.passes_pct,
    sps.progressive_passes,
    sps.passes_into_penalty_area,
    sps.assisted_shots,
    -- Regates
    psn.take_ons,
    psn.take_ons_won,
    pt.crosses,
    -- Posesión
    psn.touches,
    psn.touches_att_3rd,
    psn.touches_att_pen_area


FROM 
    match_statistics ms
-- Estadísticas ofensivas
LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
-- Estadísticas de pases
LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
-- Tipos de pases
LEFT JOIN stats_passTypes_summary pt ON ms.player_id = pt.player_id AND ms.estadistica_id = pt.stat_id
-- Estadísticas de posesión
LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
-- Posición de delantero
LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id  -- Asegura que estamos usando la posición correcta para el partido;
-- Asegura que estamos usando el partido correcto
LEFT JOIN football_match fm ON ms.match_id = fm.match_id

WHERE fm.Season = 128 AND pp.position_id IN (40, 35, 46, 43)   -- Asegura que estamos usando el partido correcto


-- Asegura que estamos usando el partido correcto
--pp.position_id IN (SELECT position_id FROM position_on_the_field WHERE position_name IN ('LW', 'RW', 'AM'))
--    AND ms.match_id = 726;  -- Asegura que estamos usando el partido correcto



















/* Vistas para la posicion de centrocampista */
CREATE VIEW midfielder_stats_view_season1 AS
SELECT 
    

    ms.estadistica_id,
    ms.player_id,
    ms.match_id,
    pp.position_id,
    ms.minutes,
    ms.goals,
    ms.assists,

    ss.shots,
    ss.shots_on_target,
    ss.xg,
    ss.npxg,
    ss.xg_assist,
    ss.sca,
    ss.gca,
    ss.interceptions,

    sps.passes_completed,
    sps.passes,
    sps.passes_pct,
    pt.crosses,
    sps.progressive_passes,
    sps.passes_into_penalty_area,
    sps.passes_total_distance,
    sps.passes_progressive_distance,
    sps.passes_completed_short,
    sps.passes_pct_short,
    sps.passes_completed_medium,
    sps.passes_pct_medium,
    sps.passes_completed_long,
    sps.passes_pct_long,
    sps.passes_into_final_third,

    psn.touches,
    psn.take_ons,
    psn.take_ons_won,
    psn.take_ons_won_pct,
    psn.take_ons_tackled,
    psn.carries,
    psn.carries_distance,
    psn.carries_progressive_distance,
    psn.progressive_carries,
    psn.carries_into_final_third,
    psn.carries_into_penalty_area,
    psn.miscontrols,
    psn.dispossessed,
    psn.passes_received,
    psn.progressive_passes_received

FROM 
    match_statistics ms
-- Estadísticas ofensivas
LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
-- Estadísticas de pases
LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
-- Tipos de pase
LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
--tipo de pases
LEFT JOIN stats_passTypes_summary pt ON ms.player_id = pt.player_id AND ms.estadistica_id = pt.stat_id
-- Posición de centrocampista
LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id  -- Asegura que estamos usando la posición correcta para el partido;
-- Asegura que estamos usando el partido correcto
LEFT JOIN football_match fm ON ms.match_id = fm.match_id

WHERE fm.Season = 128 AND pp.position_id IN (41, 42, 44, 45, 33)   -- Asegura que estamos usando el partido correcto







CREATE VIEW defense_stats_view_season AS
SELECT 
    ms.estadistica_id,
    ms.player_id,
    ms.match_id,
    pp.position_id,
    ms.minutes,
    ms.goals,
    ms.assists,

    ss.shots,
    ss.shots_on_target,
    ss.xg,
    ss.npxg,
    ss.xg_assist,
    ss.sca,
    ss.gca,

    sps.passes_completed,
    sps.passes,
    sps.passes_pct,

    
    psn.carries,
    psn.carries_distance,
    psn.carries_progressive_distance,
    psn.miscontrols,
    psn.dispossessed,
    psn.passes_received,

    sda.tackles,
    sda.tackles_won,
    sda.blocks,
    sda.blocked_shots,
    sda.blocked_passes,
    sda.interceptions,
    sda.clearances,
    sda.errors,
    sda.challenge_tackles,
    sda.challenges,
    sda.challenge_tackles_pct,
    sda.tackles_def_3rd,
    sda.tackles_mid_3rd,
    sda.tackles_att_3rd,
    sda.tackles_interceptions,
    
    -- Estadísticas de duelos aéreos
    sms.aerials_won,
    sms.aerials_won_pct,
    sms.aerials_lost

FROM 
    match_statistics ms
-- Estadísticas ofensivas
LEFT JOIN stats_summary ss ON ms.player_id = ss.player_id AND ms.estadistica_id = ss.stat_id
-- Estadísticas de pases
LEFT JOIN stats_passing_summary sps ON ms.player_id = sps.player_id AND ms.estadistica_id = sps.stat_id
-- Tipos de pase
LEFT JOIN stats_possession_summary psn ON ms.player_id = psn.player_id AND ms.estadistica_id = psn.stat_id
-- Posición de centrocampista
LEFT JOIN position_player pp ON ms.player_id = pp.player_id AND pp.match_id = ms.match_id  -- Asegura que estamos usando la posición correcta para el partido;
-- Asegura que estamos usando el partido correcto
LEFT JOIN stats_DefensiveActions_summary sda ON ms.player_id = sda.player_id AND ms.estadistica_id = sda.stat_id  -- Suponiendo que minutes es un identificador de la estadística
-- Estadísticas de duelos aéreos
LEFT JOIN stats_miscellaneous_summary sms ON ms.player_id = sms.player_id AND ms.estadistica_id = sms.stat_id 

LEFT JOIN football_match fm ON ms.match_id = fm.match_id

WHERE fm.Season = 128 AND pp.position_id IN (34, 41, 37, 45, 48)   -- Asegura que estamos usando el partido correcto


