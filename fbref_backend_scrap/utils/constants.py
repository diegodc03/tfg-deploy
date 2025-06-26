

required_football_match_columns = [
    'Home', 'Away', 'Wk', 'Day', 'Date',
    'Score', 'Season'
]


football_match_league_columns = ['Wk', 'Day', 'Date', 'Home', 'Away', 'Score', 'Attendance', 'Venue', 'Referee']
football_match_cup_columns = ['Round', 'Day', 'Date', 'Home', 'Away', 'Score', 'Attendance', 'Venue', 'Referee']


############################################################################################################

stats_summary_player = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes",
    "goals", "assists", "pens_made", "pens_att", "shots", "shots_on_target", 
    "cards_yellow", "cards_red", "touches", "tackles", "interceptions", 
    "blocks", "xg", "npxg", "xg_assist", "sca", "gca", 
    "passes_completed", "passes", "passes_pct", "progressive_passes", "carries", 
    "progressive_carries", "take_ons", "take_ons_won"
]

stats_passing_summary = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes", "passes_completed", "passes", "passes_pct", "passes_total_distance", "passes_progressive_distance",
    "passes_completed_short", "passes_short", "passes_pct_short",
    "passes_completed_medium", "passes_medium", "passes_pct_medium",
    "passes_completed_long", "passes_long", "passes_pct_long",
    "assists", "xg_assists", "pass_xa", "assisted_shots", 
    "passes_into_final_third", "passes_into_penalty_area", 
    "crosses_into_penalty_area", "progressive_passes",
]

stats_passTypes_summary = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes", 
    "passes", "passes_live", "passes_dead", "passes_free_kicks", "through_balls", "passes_switches",
    "crosses", "throw_ins", "corner_kicks", "corner_kicks_in", "corner_kicks_out", "corner_kicks_straight",
    "passes_completed", "passes_offsides", "passes_blocked"
]

stats_DefensiveActions_summary = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes", 
    "tackles", "tackles_won", "tackles_def_3rd", "tackles_mid_3rd", "tackles_att_3rd", "challenge_tackles", 
    "challenges", "challenge_tackles_pct", "challenged_lost", "blocks", "blocked_shots", "blocked_passes",
    "interceptions", "tackles_interceptions", "clearances", "errors"
]

stats_Possession_summary = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes", 
    "touches", "touches_def_pen_area", "touches_def_3rd", "touches_mid_3rd", "touches_att_3rd", "touches_att_pen_area", 
    "touches_live_ball", "take_ons", "take_ons_won", "take_ons_won_pct", "take_ons_tackled", "take_ons_tackled_pct",
    "carries", "carries_distance", "carries_progressive_distance", "progressive_carries", "carries_into_final_third", "carries_into_penalty_area", 
    "miscontrols", "dispossessed", "passes_received", "progressive_passes_received"
]

stats_miscellaneous_summary = [
    "player", "shirt_number", "nacionality", "position", "age", "minutes", 
    "cards_yellow", "cards_red", "cards_yellow_red", "fouls", "fouled", "offsides", 
    "tackles_interceptions", "interceptions", "tackles_won", "pens_won", "pens_conceded", "own_goals", 
    "ball_recoveries","aerials_won", "aerials_lost", "aerials_won_pct"
]

stats_goalkeeper_summary = [
    "player", "nacionality", "age", "minutes", "gk_shots_on_target_against", "gk_goals_against", 
    "gk_saves", "gk_save_pct", "gk_psxg", "gk_passes_completed_launched", "gk_passes_launched", "gk_passes_pct_launched",
    "gk_passes", "gk_passes_throws", "gk_pct_passes_launched", "gk_passes_length_avg", "gk_goal_kicks", "gk_pct_goal_kicks_launched",
    "gk_goal_kick_length_avg", "gk_crosses", "gk_crosses_stopped", "gk_crosses_stopped_pct", "gk_def_actions_outside_pen_area", "gk_avg_distance_def_actions"
]





############################################################################################################
dic_stats = {
    1: stats_summary_player,
    2: stats_passing_summary,
    3: stats_passTypes_summary,
    4: stats_DefensiveActions_summary,
    5: stats_Possession_summary,
    6: stats_miscellaneous_summary
}


table_dic_to_insert = {
    0: "stats_gk_summary",
    1: "stats_summary",
    2: "stats_passing_summary",
    3: "stats_passTypes_summary",
    4: "stats_DefensiveActions_summary",
    5: "stats_Possession_summary",
    6: "stats_miscellaneous_summary"
}




basic_elements_of_player = ["player", "shirt_number", "nacionality", "position", "age", "minutes", "goals", "assists"]
basic_elements_of_gk = ["player", "nacionality", "age", "minutes"]

match_statisctics_of_player = ["minutes", "goals", "assists"]
match_statisctics_of_gk = ["minutes"]


############################################################################################################




var_integers = [
    "minutes", "goals", "assists", "passes_completed", "passes", "passes_completed_short", 
    "passes_short", "passes_completed_medium", "passes_medium", "passes_completed_long", "passes_long", "assisted_shots",
    "passes_into_final_third", "passes_into_penalty_area", "crosses_into_penalty_area", "progressive_passes", "tackles", "tackles_won",
    "tackles_def_3rd", "tackles_mid_3rd", "tackles_att_3rd", "challenge_tackles", "challenges", "challenged_lost",
    "blocks", "blocked_shots", "blocked_passes", "interceptions", "tackles_interceptions", "clearances",
    "errors", "touches", "touches_def_pen_area", "touches_def_3rd", "touches_mid_3rd", "touches_att_3rd",
    "touches_att_pen_area", "touches_live_ball", "take_ons", "take_ons_won", "take_ons_tackled", "carries",
    "progressive_carries", "carries_into_final_third", "carries_into_penalty_area", "miscontrols", "dispossessed", "passes_received",
    "progressive_passes_received", "cards_yellow", "cards_red", "cards_yellow_red", "fouls", "fouled",
    "offsides", "pens_won", "pens_conceded", "own_goals", "ball_recoveries","aerials_won",
    "aerials_lost", "pens_made", "pens_att", "shots", "shots_on_target", "sca",
    "gca", "passes_live", "passes_dead", "passes_free_kicks", "through_balls", "passes_switches",
    "throw_ins", "corner_kicks", "corner_kicks_in", "corner_kicks_out", "corner_kicks_straight", "passes_offsides",
    "passes_blocked", "crosses", "passes_total_distance", "passes_progressive_distance", "carries_distance", "carries_progressive_distance",
    "Attendance", "gk_shots_on_target_against", "gk_goals_against", "gk_saves", "gk_passes_completed_launched", "gk_passes_launched", 
    "gk_passes", "gk_passes_throws", "gk_goal_kicks", "gk_crosses", "gk_crosses_stopped", "gk_def_actions_outside_pen_area",
    "shirt_number"

    ]

var_floats = [
    
    "xg_assists", "pass_xa", "xg", "npxg", "xa", "xg_assist",
    "goals_pens_per90", "xG", "xG.1", "Wk", "gk_psxg",
    "gk_passes_length_avg", "gk_goal_kick_length_avg", "gk_avg_distance_def_actions"
  ]

var_pct = [
    "passes_pct", "passes_pct_short", "passes_pct_medium", "passes_pct_long", "challenge_tackles_pct", "take_ons_won_pct",
    "take_ons_tackled_pct", "aerials_won_pct", "gk_save_pct", "gk_passes_pct_launched", "gk_pct_passes_launched", "gk_pct_goal_kicks_launched", 
    "gk_crosses_stopped_pct"
]

var_strings = [
    "player", "nacionality", "position", "Day", "Date", "Time", 
    "Home", "Away", "Score", "season", "Venue", "Referee", 
    "player_id"
]





# Constants for different tables introducie

# Table Type_shots
type_shots = ["Pass (Dead)", "Pass (Live)", "Tackle", "Shot", "Fouled", "Take-On"]
# Table body_part
body_parts = ["Right Foot", "Left Foot", "Head", "Other"]
# Table outcome_stats
outcomes = ["Goal", "Saved", "Off Target", "Post", "Blocked", "Wayward", "Own Goal", "Penalty Saved", "Penalty Missed", "Woodwork", "Other"]
# Table position_on_the_field
type_positions = ["GK", "DF", "MF", "FW", "FB", "LB", "RB", "CB", "DM", "CM", "LM", "RM", "WM", "LW", "RW", "AM"]
# Tabla categorias básicas de juego
basic_positions = ["goalkeepers", "defenders", "midfielders", "forwards"]


# Table Type_of_game
type_of_game = ["deffensive", "offensive", "No_existencia_de_tipo_de_juego"]
# Table type_of_games
game_modes = ["no_existencia", "bloque_bajo", "bloque_medio", "contraataque", "tiki_taka", "presion_alta", "juego_por_bandas"]
   
   
# Posiciones
# Basic Positions
basic_positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
# Specific Positions
specific_positions = [
    "center_midfielder", "central_defender", "defensive_midfielder", "forward", "fullback",
    "goalkeeper", "lateral_midfielder", "no_existencia", "offensive_midfielder", "winger"
]


