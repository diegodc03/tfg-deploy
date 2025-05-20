CREATE TABLE `season` (
  `season_id` integer PRIMARY KEY AUTO_INCREMENT,
  `season_year` varchar(255)
);


CREATE TABLE `tournament` (
  `tournament_id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre_liga` varchar(255),
  `season_tournament_id` integer,
  `type_of_competition` varchar(255),
  `tournament_fbref_id` varchar(255)
);

ALTER TABLE `tournament` ADD FOREIGN KEY (`season_tournament_id`) REFERENCES `season` (`season_id`) ON DELETE CASCADE ON UPDATE CASCADE;



CREATE TABLE `team` (
  `team_id` integer PRIMARY KEY AUTO_INCREMENT,
  `team_name` varchar(255),
  `tournament_team_id` integer
);

ALTER TABLE `team` ADD FOREIGN KEY (`tournament_team_id`) REFERENCES `tournament` (`tournament_id`) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE `jugador` (
  `player_id` integer PRIMARY KEY AUTO_INCREMENT,
  `player` varchar(255),
  `shirt_number` integer,
  `nacionality` varchar(255),
  `position` varchar(255),
  `age` integer
);

CREATE TABLE `team_player` (
  `team_id` integer,
  `player_id` integer,
  PRIMARY KEY (`team_id`, `jugador_team_id`)
);

ALTER TABLE `team_player` ADD FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `team_player` ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE;





CREATE TABLE football_match (
    match_id INT PRIMARY KEY AUTO_INCREMENT,
    Home INT,
    Away INT,
    Wk FLOAT,
    Day VARCHAR(255),
    Date DATE,
    Score VARCHAR(255),
    Attendance INT,
    Venue VARCHAR(255),
    Referee VARCHAR(255),
    Season INT,
    FOREIGN KEY (Home) REFERENCES team(team_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Away) REFERENCES team(team_id) ON DELETE CASCADE ON UPDATE CASCADE
);




CREATE TABLE `estadisticas_partido_gen` (
  `estadistica_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `local_possession` FLOAT,
  `visitor_possession` FLOAT,
  `local_passing_accuracy` FLOAT,
  `visitor_passing_accuracy` FLOAT,
  `local_shots_on_target` FLOAT,
  `visitor_shots_on_target` FLOAT,
  `local_saves` FLOAT,
  `visitor_saves` FLOAT,
  `local_cards` FLOAT,
  `visitor_cards` FLOAT,
  `local_fouls` FLOAT,
  `visitor_fouls` FLOAT,
  `local_corners` FLOAT,
  `visitor_corners` FLOAT,
  `local_crosses` FLOAT,
  `visitor_crosses` FLOAT,
  `local_touches` FLOAT,
  `visitor_touches` FLOAT,
  `local_tackles` FLOAT,
  `visitor_tackles` FLOAT,
  `local_interceptions` FLOAT,
  `visitor_interceptions` FLOAT,
  `local_aerials_won` FLOAT,
  `visitor_aerials_won` FLOAT,
  `local_clearances` FLOAT,
  `visitor_clearances` FLOAT,
  `local_offsides` FLOAT,
  `visitor_offsides` FLOAT,
  `local_goal_kicks` FLOAT,
  `visitor_goal_kicks` FLOAT,
  `local_throw_ins` FLOAT,
  `visitor_throw_ins` FLOAT,
  `local_long_balls` FLOAT,
  `visitor_long_balls` FLOAT,
  `match_id` integer
);




CREATE TABLE `roles` (
  `rol_id` integer PRIMARY KEY AUTO_INCREMENT,
  `tipo_rol` varchar(255),
  `descripcion_rol` text
);

CREATE TABLE `puntuacion_partido` (
  `puntuacion_id` integer PRIMARY KEY AUTO_INCREMENT,
  `jugador_id` integer,
  `partido_id` integer,
  `rol_id` integer,
  `puntuacion` integer
);

CREATE TABLE `match_statistics` (
  `estadistica_id` integer PRIMARY KEY AUTO_INCREMENT,
  `match_id` integer,
  `player_id` integer,
  `minutes` integer,
  `goals` integer,
  `assists` integer
);

CREATE TABLE `stats_summary` (
  `estatistic_id` int PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `pens_made` int,
  `pens_att` int,
  `shots` int,
  `shots_on_target` int,
  `cards_yellow` int,
  `cards_red` int,
  `touches` int,
  `tackles` int,
  `interceptions` int,
  `blocks` int,
  `xg` float,
  `npxg` float,
  `xg_assist` float,
  `sca` int,
  `gca` int,
  `passes_completed` int,
  `passes` int,
  `passes_pct` float,
  `progressive_passes` int,
  `carries` int,
  `progressive_carries` int,
  `take_ons` int,
  `take_ons_won` int
);

CREATE TABLE `stats_passing_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `passes_completed` integer,
  `passes` integer,
  `passes_pct` double,
  `passes_total_distance` double,
  `passes_progressive_distance` double,
  `passes_completed_short` integer,
  `passes_short` integer,
  `passes_pct_short` double,
  `passes_completed_medium` integer,
  `passes_medium` integer,
  `passes_pct_medium` double,
  `passes_completed_long` integer,
  `passes_long` integer,
  `passes_pct_long` double,
  `assists` integer,
  `xg_assists` double,
  `pass_xa` double,
  `assisted_shots` integer,
  `passes_into_final_third` integer,
  `passes_into_penalty_area` integer,
  `crosses_into_penalty_area` integer,
  `progressive_passes` integer
);

CREATE TABLE `stats_DefensiveActions_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `tackles` integer,
  `tackles_won` integer,
  `tackles_def_3rd` integer,
  `tackles_mid_3rd` integer,
  `tackles_att_3rd` integer,
  `challenge_tackles` integer,
  `challenges` integer,
  `challenge_tackles_pct` double,
  `challenged_lost` integer,
  `blocks` integer,
  `blocked_shots` integer,
  `blocked_passes` integer,
  `interceptions` integer,
  `tackles_interceptions` integer,
  `clearances` integer,
  `errors` integer
);

CREATE TABLE `stats_Possession_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `touches` integer,
  `touches_def_pen_area` integer,
  `touches_def_3rd` integer,
  `touches_mid_3rd` integer,
  `touches_att_3rd` integer,
  `touches_att_pen_area` integer,
  `touches_live_ball` integer,
  `take_ons` integer,
  `take_ons_won` integer,
  `take_ons_won_pct` double,
  `take_ons_tackled` integer,
  `take_ons_tackled_pct` double,
  `carries` integer,
  `carries_distance` double,
  `carries_progressive_distance` double,
  `progressive_carries` integer,
  `carries_into_final_third` integer,
  `carries_into_penalty_area` integer,
  `miscontrols` integer,
  `dispossessed` integer,
  `passes_received` integer,
  `progressive_passes_received` integer
);

CREATE TABLE `stats_miscellaneous_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `cards_yellow` integer,
  `cards_red` integer,
  `cards_yellow_red` integer,
  `fouls` integer,
  `fouled` integer,
  `offsides` integer,
  `crosses` integer,
  `interceptions` integer,
  `tackles_won` integer,
  `pens_won` integer,
  `pens_conceded` integer,
  `own_goals` integer,
  `ball_recoveries` integer,
  `aerials_won` integer,
  `aerials_lost` integer,
  `aerials_won_pct` double,
  `pens_made` integer,
  `pens_att` integer,
  `shots` integer,
  `shots_on_target` integer,
  `tackles` integer,
  `goals_pens_per90` double,
  `xg` double,
  `npxg` double,
  `xa` double,
  `xg_assist` double,
  `sca` integer,
  `gca` integer
);

CREATE TABLE `stats_passTypes_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `passes` integer,
  `passes_live` integer,
  `passes_dead` integer,
  `passes_free_kicks` integer,
  `through_balls` integer,
  `passes_switches` integer,
  `crosses` integer,
  `throw_ins` integer,
  `corner_kicks` integer,
  `corner_kicks_in` integer,
  `corner_kicks_out` integer,
  `corner_kicks_straight` integer,
  `passes_completed` integer,
  `passes_offsides` integer,
  `passes_blocked` integer
);

CREATE TABLE `stats_gk_summary` (
  `estatistic_id` integer PRIMARY KEY AUTO_INCREMENT,
  `stat_id` integer,
  `player_id` integer,
  `gk_shots_on_target_against` integer,
  `gk_goals_against` integer,
  `gk_saves` integer,
  `gk_save_pct` double,
  `gk_psxg` double,
  `gk_passes_completed_launched` integer,
  `gk_passes_launched` integer,
  `gk_passes_pct_launched` double,
  `gk_passes` integer,
  `gk_passes_throws` integer,
  `gk_pct_passes_launched` double,
  `gk_passes_length_avg` double,
  `gk_goal_kicks` integer,
  `gk_pct_goal_kicks_launched` double,
  `gk_goal_kick_length_avg` double,
  `gk_crosses` integer,
  `gk_crosses_stopped` integer,
  `gk_crosses_stopped_pct` double,
  `gk_def_actions_outside_pen_area` integer,
  `gk_avg_distance_def_actions` double
);	


CREATE TABLE `stats_shots_summary` (
  `estatistic_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `match_id` INTEGER,
  `shot_minute` INTEGER,
  `player_shot` INTEGER,
  `team_shot` INTEGER,
  `xg` DOUBLE,
  `psxg` DOUBLE,
  `outcome` INTEGER,
  `distance` DOUBLE,
  `body_part` INTEGER,
  `notes` VARCHAR(255),
  `player_assisted_1` INTEGER,
  `event_type` INTEGER,
  `player_assisted_2` INTEGER,
  `event_type_2` INTEGER,
  CONSTRAINT `fk_stat_id` FOREIGN KEY (`match_id`) REFERENCES `football_match` (`match_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_player_shot` FOREIGN KEY (`player_shot`) REFERENCES `jugador` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_team_shot` FOREIGN KEY (`team_shot`) REFERENCES `team` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_outcome` FOREIGN KEY (`outcome`) REFERENCES `outcome_stats` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_body_part` FOREIGN KEY (`body_part`) REFERENCES `body_part` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_event_type` FOREIGN KEY (`event_type`) REFERENCES `event_shots` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_event_type_2` FOREIGN KEY (`event_type_2`) REFERENCES `event_shots` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_player_assisted_1` FOREIGN KEY (`player_assisted_1`) REFERENCES `jugador` (`player_id`)  ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_player_assisted_2` FOREIGN KEY (`player_assisted_2`) REFERENCES `jugador` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE event_shots(
    id integer PRIMARY KEY AUTO_INCREMENT,
    event_shot_name varchar(255)
);

CREATE TABLE body_part(
    id integer PRIMARY KEY AUTO_INCREMENT,
    body_part_name varchar(255)
)

CREATE TABLE outcome_stats(
    id integer PRIMARY KEY AUTO_INCREMENT,
    outcome_name varchar(255)
)


CREATE TABLE `nacionality` (
  `nacionality_id` integer PRIMARY KEY AUTO_INCREMENT,
  `nacionality` varchar(255)
);

CREATE TABLE `position` (
  `position_id` integer PRIMARY KEY AUTO_INCREMENT,
  `position` varchar(255)
);

CREATE TABLE `age` (
  `age_id` integer PRIMARY KEY AUTO_INCREMENT,
  `age` integer
);

CREATE TABLE `shirt_number` (
  `shirt_number_id` integer PRIMARY KEY AUTO_INCREMENT,
  `shirt_number` integer
);

CREATE TABLE `position_on_the_field` (
  `position_id` integer PRIMARY KEY AUTO_INCREMENT,
  `position_name` varchar(255)
);

CREATE TABLE `position_player` (
  `position_id` integer,
  `match_id` integer,
  `player_id` integer,
  PRIMARY KEY (`position_id`, `player_id`, `match_id`)
);
ALTER TABLE `position_player` ADD FOREIGN KEY (`match_id`) REFERENCES `football_match` (`match_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `position_player` ADD FOREIGN KEY (`position_id`) REFERENCES `position_on_the_field` (`position_id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `position_player` ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE position_category (
    position_id INT PRIMARY KEY,
    category_name VARCHAR(20) NOT NULL,
    FOREIGN KEY (position_id) REFERENCES position_on_the_field(position_id)
);

CREATE TABLE position_category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE position_category_relation (
    position_id INT,
    category_id INT,
    PRIMARY KEY (position_id, category_id),
    FOREIGN KEY (position_id) REFERENCES position_on_the_field(position_id),
    FOREIGN KEY (category_id) REFERENCES position_category(category_id)
);


INSERT INTO position_category (category_name)
VALUES ('goalkeepers'), ('defenders'), ('midfielders'), ('forwards');


-- Goalkeepers (Porteros)
INSERT INTO position_category_relation (position_id, category_id)
SELECT position_id, (SELECT category_id FROM position_category WHERE category_name = 'goalkeepers')
FROM position_on_the_field WHERE position_name = 'GK';

-- Defenders (Defensas)
INSERT INTO position_category_relation (position_id, category_id)
SELECT position_id, (SELECT category_id FROM position_category WHERE category_name = 'defenders')
FROM position_on_the_field WHERE position_name IN ('DF', 'FB', 'LB', 'RB', 'CB');

-- Midfielders (Centrocampistas)
INSERT INTO position_category_relation (position_id, category_id)
SELECT position_id, (SELECT category_id FROM position_category WHERE category_name = 'midfielders')
FROM position_on_the_field WHERE position_name IN ('MF', 'DM', 'CM', 'LM', 'RM', 'WM');

-- Forwards (Delanteros)
INSERT INTO position_category_relation (position_id, category_id)
SELECT position_id, (SELECT category_id FROM position_category WHERE category_name = 'forwards')
FROM position_on_the_field WHERE position_name IN ('FW', 'LW', 'RW', 'AM');


ALTER TABLE `puntuacion_partido` ADD FOREIGN KEY (`jugador_id`) REFERENCES `jugador` (`jugador_id`);

ALTER TABLE `puntuacion_partido` ADD FOREIGN KEY (`partido_id`) REFERENCES `football_match` (`match_id`);

ALTER TABLE `puntuacion_partido` ADD FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`);




    
    
CREATE TABLE match_players_score (
    match_player_scores_id INT AUTO_INCREMENT,
    match_player_id INT NOT NULL,
    specific_position_id INT,
    basic_position_id INT,
    score FLOAT NOT NULL,
    PRIMARY KEY (match_player_score_id),
    FOREIGN KEY (match_player_id) REFERENCES match_players(match_player_id),
    FOREIGN KEY (specific_position_id) REFERENCES positions_specifics_by_category(specific_position_id),
    FOREIGN KEY (basic_position_id) REFERENCES position_category(category_id));
    
    


CREATE TABLE basic_specific_positions_relation(
    basic_position_id INT,
    specific_position_id INT,
    PRIMARY KEY (basic_position_id, specific_position_id),
    FOREIGN KEY (basic_position_id) REFERENCES position_category(category_id),
    FOREIGN KEY (specific_position_id) REFERENCES positions_specifics_by_category(specific_position_id)

)


INSERT INTO basic_specific_positions_relation (specific_position_id, basic_position_id) VALUES 
(1, 1), -- Goalkeeper
(2, 2), -- Fullback
(3, 2), -- Central Defender
(4, 3), -- Center Midfielder
(5, 3), -- Lateral Midfielder
(6, 3), -- Defensive Midfielder
(7, 3), -- Offensive Midfielder
(8, 4), -- Winger
(9, 4); -- Forward









/*************************************************************************/

ALTER TABLE `stats_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_passing_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_DefensiveActions_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_Possession_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_miscellaneous_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_passTypes_summary` 
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_gk_summary`
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_shots_summary`
ADD FOREIGN KEY (`stat_id`) REFERENCES `match_statistics` (`estadistica_id`)
ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE `stats_summary` 
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_passing_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_DefensiveActions_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_Possession_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_miscellaneous_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_passTypes_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_gk_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stats_shots_summary`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;


/*************************************************************************/
/*************************************************************************/

ALTER TABLE `match_statistics`
ADD FOREIGN KEY (`player_id`) REFERENCES `jugador` (`player_id`)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `match_statistics`
ADD FOREIGN KEY (`match_id`) REFERENCES `football_match` (`match_id`)
ON DELETE CASCADE ON UPDATE CASCADE;


/*************************************************************************/
/*************************************************************************/


ALTER TABLE `estadisticas_partido_gen` ADD FOREIGN KEY (`match_id`) REFERENCES `football_match` (`match_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*************************************************************************/
/*************************************************************************/


CREATE TABLE avg_player_stats (
    id int PRIMARY KEY AUTO_INCREMENT,
    league_id INT,
    gk_shots_on_target_against FLOAT,
    gk_goals_against FLOAT,
    gk_saves FLOAT,
    gk_save_pct FLOAT,
    gk_psxg FLOAT,
    gk_passes_completed_launched FLOAT,
    gk_passes_launched FLOAT,
    gk_passes_pct_launched FLOAT,
    gk_passes FLOAT,
    gk_passes_throws FLOAT,
    gk_pct_passes_launched FLOAT,
    gk_passes_length_avg FLOAT,
    gk_goal_kicks FLOAT,
    gk_pct_goal_kicks_launched FLOAT,
    gk_goal_kick_length_avg FLOAT,
    gk_crosses FLOAT,
    gk_crosses_stopped FLOAT,
    gk_crosses_stopped_pct FLOAT,
    gk_def_actions_outside_pen_area FLOAT,
    gk_avg_distance_def_actions FLOAT,
    pens_made FLOAT,
    pens_att FLOAT,
    shots FLOAT,
    shots_on_target FLOAT,
    cards_yellow FLOAT,
    cards_red FLOAT,
    touches FLOAT,
    tackles FLOAT,
    interceptions FLOAT,
    blocks FLOAT,
    xg FLOAT,
    npxg FLOAT,
    xg_assist FLOAT,
    sca FLOAT,
    gca FLOAT,
    passes_completed FLOAT,
    passes FLOAT,
    passes_pct FLOAT,
    progressive_passes FLOAT,
    carries FLOAT,
    progressive_carries FLOAT,
    take_ons FLOAT,
    take_ons_won FLOAT,
    passes_total_distance FLOAT,
    passes_progressive_distance FLOAT,
    passes_completed_short FLOAT,
    passes_short FLOAT,
    passes_pct_short FLOAT,
    passes_completed_medium FLOAT,
    passes_medium FLOAT,
    passes_pct_medium FLOAT,
    passes_completed_long FLOAT,
    passes_long FLOAT,
    passes_pct_long FLOAT,
    xg_assists FLOAT,
    pass_xa FLOAT,
    assisted_shots FLOAT,
    passes_into_final_third FLOAT,
    passes_into_penalty_area FLOAT,
    crosses_into_penalty_area FLOAT,
    passes_live FLOAT,
    passes_dead FLOAT,
    passes_free_kicks FLOAT,
    through_balls FLOAT,
    passes_switches FLOAT,
    crosses FLOAT,
    throw_ins FLOAT,
    corner_kicks FLOAT,
    corner_kicks_in FLOAT,
    corner_kicks_out FLOAT,
    corner_kicks_straight FLOAT,
    passes_offsides FLOAT,
    passes_blocked FLOAT,
    tackles_won FLOAT,
    tackles_def_3rd FLOAT,
    tackles_mid_3rd FLOAT,
    tackles_att_3rd FLOAT,
    challenge_tackles FLOAT,
    challenges FLOAT,
    challenge_tackles_pct FLOAT,
    challenged_lost FLOAT,
    blocked_shots FLOAT,
    blocked_passes FLOAT,
    tackles_interceptions FLOAT,
    clearances FLOAT,
    errors FLOAT,
    touches_def_pen_area FLOAT,
    touches_def_3rd FLOAT,
    touches_mid_3rd FLOAT,
    touches_att_3rd FLOAT,
    touches_att_pen_area FLOAT,
    touches_live_ball FLOAT,
    take_ons_won_pct FLOAT,
    take_ons_tackled FLOAT,
    take_ons_tackled_pct FLOAT,
    carries_distance FLOAT,
    carries_progressive_distance FLOAT,
    carries_into_final_third FLOAT,
    carries_into_penalty_area FLOAT,
    miscontrols FLOAT,
    dispossessed FLOAT,
    passes_received FLOAT,
    progressive_passes_received FLOAT,
    cards_yellow_red FLOAT,
    fouls FLOAT,
    fouled FLOAT,
    offsides FLOAT,
    pens_won FLOAT,
    pens_conceded FLOAT,
    own_goals FLOAT,
    ball_recoveries FLOAT,
    aerials_won FLOAT,
    aerials_lost FLOAT,
    aerials_won_pct FLOAT
);

ALTER TABLE player_stats ADD FOREIGN KEY (league_id) REFERENCES tournament(tournament_id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE avg_player_stats_by_basic_positions ADD FOREIGN KEY (position_player) REFERENCES position_category(category_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE avg_player_stats_by_specific_positions ADD FOREIGN KEY (position_player) REFERENCES position_on_the_field(position_id) ON DELETE CASCADE ON UPDATE CASCADE;




CREATE TABLE positions_specifics_by_category (
    specific_position_id INT PRIMARY KEY AUTO_INCREMENT,
    specific_position_name VARCHAR(255) NOT NULL,
);

INSERT INTO `positions_specifics_by_category` (`specific_position_id`, `specific_position_name`) VALUES (NULL, 'goalkeeper'), (NULL, 'fullback'), (NULL, 'central_defender'), (NULL, 'center_midfielder'), (NULL, 'lateral_midfielder'), (NULL, 'defensive_midfielder'), (NULL, 'offensive_midfielder'), (NULL, 'winger'), (NULL, 'forward');


ALTER TABLE players ADD CONSTRAINT fk_players_positions_new
FOREIGN KEY (position_id) REFERENCES positions_new(id)
ON DELETE CASCADE;



CREATE TABLE type_of_game (
    type_of_game_id INT PRIMARY KEY AUTO_INCREMENT,
    type_of_game_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE game_modes (
    game_mode_id INT PRIMARY KEY AUTO_INCREMENT,
    game_mode_name VARCHAR(255) NOT NULL,
    type_of_game_id INT NOT NULL,
    FOREIGN KEY (type_of_game_id) REFERENCES type_of_game(type_of_game_id)
);


INSERT INTO type_of_game (type_of_game_name) VALUES
('defensive'),
('offensive');

INSERT INTO game_modes (game_mode_name, type_of_game_id)
VALUES
('bloque_bajo', 1),
('bloque_medio', 1),
('contraataque', 1),
('tiki_taka', 2),
('presion_alta', 2),
('juego_por_bandas', 2);






CREATE TABLE query_mappings (
    game_mode_id INT NOT NULL,
    position_player_id INT NOT NULL,
    function_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (game_mode_id, position_player_id),
    FOREIGN KEY (game_mode_id) REFERENCES game_modes(game_mode_id),
    FOREIGN KEY (position_player_id) REFERENCES positions_specifics_by_category(specific_position_id)
);


INSERT INTO query_mappings (game_mode_id, position_player_id, function_name)
VALUES 
(1, 2, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_defense_laterales'),
(1, 3, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_defense_central_defenders'),
(1, 4, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_creativo'),
(1, 5, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_lateral'),
(1, 6, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_defensivo'),
(1, 7, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_centrocampista_ofensivo'),
(1, 8, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_extremo'),
(1, 9, 'get_stats_to_defensive_player_and_bloque_bajo_type_of_forward_delantero_centro'),

(2, 2, 'get_stats_to_defensive_player_and_bloque_medio_type_of_defense_laterales'),
(2, 3, 'get_stats_to_defensive_player_and_bloque_medio_type_of_defense_central_defenders'),
(2, 4, 'get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_creativo'),
(2, 5, 'get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_lateral'),
(2, 6, 'get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_defensivo'),
(2, 7, 'get_stats_to_defensive_player_and_bloque_medio_type_of_centrocampista_ofensivo'),
(2, 8, 'get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_extremo'),
(2, 9, 'get_stats_to_defensive_player_and_bloque_medio_type_of_forward_delantero_centro'),


(3, 2, 'get_stats_to_defensive_player_and_contraataque_type_of_defense_laterales'),
(3, 3, 'get_stats_to_defensive_player_and_contraataque_type_of_defense_central_defenders'),
(3, 4, 'get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_creativo'),
(3, 5, 'get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_lateral'),
(3, 6, 'get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_defensivo'),
(3, 7, 'get_stats_to_defensive_player_and_contraataque_type_of_centrocampista_ofensivo'),
(3, 8, 'get_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_extremo'),
(3, 9, 'get_stats_to_defensive_player_and_contraataque_type_of_forward_delantero_centro'),


(4, 2, 'get_stats_to_offensive_player_and_tiki_taka_type_of_defense_laterales'),
(4, 3, 'get_stats_to_offensive_player_and_tiki_taka_type_of_defense_central_defenders'),
(4, 4, 'get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_creativo'),
(4, 5, 'get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_lateral'),
(4, 6, 'get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_defensivo'),
(4, 7, 'get_stats_to_offensive_player_and_tiki_taka_type_of_centrocampista_ofensivo'),
(4, 8, 'get_stats_to_offensive_player_and_tiki_taka_type_of_delantero_extremo'),
(4, 9, 'get_stats_to_offensive_player_and_tiki_taka_type_of_delantero_centro'),


(5, 2, 'get_stats_to_offensive_player_and_presion_alta_type_of_defense_laterales'),
(5, 3, 'get_stats_to_offensive_player_and_presion_alta_type_of_defense_central_defenders'),
(5, 4, 'get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_creativo'),
(5, 5, 'get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_lateral'),
(5, 6, 'get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_defensivo'),
(5, 7, 'get_stats_to_offensive_player_and_presion_alta_type_of_centrocampista_ofensivo'),
(5, 8, 'get_stats_to_offensive_player_and_presion_alta_type_of_delantero_extremo'),
(5, 9, 'get_stats_to_offensive_player_and_presion_alta_type_of_delantero_centro'),


(6, 2, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_laterales'),
(6, 3, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_defense_central_defenders'),
(6, 4, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_creativo'),
(6, 5, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_lateral'),
(6, 6, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_defensivo'),
(6, 7, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_centrocampista_ofensivo'),
(6, 8, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_extremo')
(6, 9, 'get_stats_to_offensive_player_and_juego_por_bandas_type_of_delantero_centro'),

-- Agregar más combinaciones según sea necesario
-- Asegúrate de que los nombres de las funciones sean correctos y existan en tu base de datos
-- Puedes usar un script para insertar múltiples filas si tienes muchas combinaciones


/*************************************************************************/
/*************************************************************************/





UPDATE position_on_the_field p
JOIN positions_specifics_by_category spc 
    ON (
        (spc.specific_position_name = 'goalkeeper' AND p.position_name = 'GK') OR
        (spc.specific_position_name = 'fullback' AND p.position_name IN ('LB', 'RB', 'FB')) OR
        (spc.specific_position_name = 'central_defender' AND p.position_name IN ('CB', 'DF')) OR
        (spc.specific_position_name = 'center_midfielder' AND p.position_name = 'CM') OR
        (spc.specific_position_name = 'lateral_midfielder' AND p.position_name IN ('LM', 'RM')) OR
        (spc.specific_position_name = 'defensive_midfielder' AND p.position_name = 'DM') OR
        (spc.specific_position_name = 'offensive_midfielder' AND p.position_name = 'AM') OR
        (spc.specific_position_name = 'winger' AND p.position_name IN ('LW', 'RW')) OR
        (spc.specific_position_name = 'forward' AND p.position_name = 'FW')
    )
SET p.specific_position_id = spc.specific_position_id;



DELETE FROM `tfg_1_base_datos_partido`.`stats_sumary`
DELETE FROM `tfg_1_base_datos_partido`.`stats_passing_summary`
DELETE FROM `tfg_1_base_datos_partido`.`stats_DefensiveActions_summary`
DELETE FROM `tfg_1_base_datos_partido`.`stats_Possession_summary`
DELETE FROM `tfg_1_base_datos_partido`.`stats_miscellaneous_summary`
DELETE FROM `tfg_1_base_datos_partido`.`stats_passTypes_summary`


ALTER TABLE `stats_sumary`
DROP FOREIGN KEY `stats_sumary_ibfk_1`;  -- Asume que el nombre de la restricción es 'stats_sumary_ibfk_1'

ALTER TABLE `stats_passing_summary`
DROP FOREIGN KEY `stats_passing_summary_ibfk_1`;  -- Asegúrate de usar el nombre correcto de la restricción

ALTER TABLE `stats_DefensiveActions_summary`
DROP FOREIGN KEY `stats_DefensiveActions_summary_ibfk_1`;  -- Lo mismo aquí

ALTER TABLE `stats_Possession_summary`
DROP FOREIGN KEY `stats_Possession_summary_ibfk_1`;  -- Y aquí

ALTER TABLE `stats_miscellaneous_summary`
DROP FOREIGN KEY `stats_miscellaneous_summary_ibfk_1`;  -- Igualmente aquí

ALTER TABLE `stats_passTypes_summary`
DROP FOREIGN KEY `stats_passTypes_summary_ibfk_1`;  -- Igualmente aquí




ALTER TABLE `stats_sumary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;

ALTER TABLE `stats_passing_summary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;

ALTER TABLE `stats_DefensiveActions_summary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;

ALTER TABLE `stats_Possession_summary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;

ALTER TABLE `stats_miscellaneous_summary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;

ALTER TABLE `stats_passTypes_summary`
CHANGE COLUMN `statistic_id` `stat_id` INTEGER;



/* modifica un auto increment con alter table */
ALTER TABLE `stats_sumary`
MODIFY COLUMN `estatistic_id` INTEGER AUTO_INCREMENT;