
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, ArrayType, FloatType, DoubleType


def get_football_match_schema():
    schema = StructType([
        StructField("Wk", FloatType(), True),
        StructField("Day", StringType(), True),
        StructField("Date", DateType(), True), 
        StructField("Home",IntegerType(), True),  
        StructField("Away", IntegerType(), True), 
        StructField("Score", StringType(), True),
        StructField("Attendance", IntegerType(), True),
        StructField("Venue", StringType(), True),
        StructField("Referee", StringType(), True),
        StructField("match_link", StringType(), True),  # Cambié a StringType si es un string
        StructField("Season", IntegerType(), True)  # Cambié a StringType si es un string
    ])
    return schema


def get_team_player_schema():
    schema = StructType([
        StructField("team_id", IntegerType(), True),
        StructField("player_id", IntegerType(), True)
    ])
    return schema

def get_player_schema():
    schema = StructType([
        StructField("player", StringType(), True),
        StructField("shirt_number", IntegerType(), True),
        StructField("nacionality", StringType(), True),
        StructField("position", StringType(), True),
        StructField("age", IntegerType(), True)
    ])
    return schema

def get_gk_schema():
    schema = StructType([
        StructField("player", StringType(), True),
        StructField("nacionality", StringType(), True),
        StructField("age", IntegerType(), True)
    ])
    return schema

def get_team_jug_schema():
    schema = StructType([
        StructField("team_id", StringType(), True),
        StructField("player_id", StringType(), True)
    ])
    return schema


def get_schema_by_index(index):

    schema_dict = {
        0: get_stats_goalkeeper_summary_schema(),
        1: get_stats_summary_player_schema(),
        2: get_stats_passing_summary_schema(),
        3: get_stats_passTypes_summary_schema(),
        4: get_stats_DefensiveActions_summary_schema(),
        5: get_stats_Possession_summary_schema(),
        6: get_stats_miscellaneous_summary_schema()
    }

    return schema_dict.get(index, None)  # Retorna None si el índice no es válido



def get_match_stats_gen_schema():
    schema = StructType([
        StructField("local_aerials_won", FloatType(), True),
        StructField("visitor_aerials_won", FloatType(), True),
        StructField("local_cards", FloatType(), True),
        StructField("visitor_cards", FloatType(), True),
        StructField("local_clearances", FloatType(), True),
        StructField("visitor_clearances", FloatType(), True),
        StructField("local_corners", FloatType(), True),
        StructField("visitor_corners", FloatType(), True),
        StructField("local_crosses", FloatType(), True),
        StructField("visitor_crosses", FloatType(), True),
        StructField("local_fouls", FloatType(), True),
        StructField("visitor_fouls", FloatType(), True),
        StructField("local_goal_kicks", FloatType(), True),
        StructField("visitor_goal_kicks", FloatType(), True),
        StructField("local_interceptions", FloatType(), True),
        StructField("visitor_interceptions", FloatType(), True),
        StructField("local_long_balls", FloatType(), True),
        StructField("visitor_long_balls", FloatType(), True),
        StructField("local_offsides", FloatType(), True),
        StructField("visitor_offsides", FloatType(), True),
        StructField("local_passing_accuracy", FloatType(), True),
        StructField("visitor_passing_accuracy", FloatType(), True),
        StructField("local_possession", FloatType(), True),
        StructField("visitor_possession", FloatType(), True),
        StructField("local_saves", FloatType(), True),
        StructField("visitor_saves", FloatType(), True),
        StructField("local_shots_on_target", FloatType(), True),
        StructField("visitor_shots_on_target", FloatType(), True),
        StructField("local_tackles", FloatType(), True),
        StructField("visitor_tackles", FloatType(), True),
        StructField("local_throw_ins", FloatType(), True),
        StructField("visitor_throw_ins", FloatType(), True),
        StructField("local_touches", FloatType(), True),
        StructField("visitor_touches", FloatType(), True),
        StructField("match_id", IntegerType(), True)
    ])
    return schema



def get_stats_summary_player_schema():
    schema = StructType([
        StructField("pens_made", IntegerType(), True),
        StructField("pens_att", IntegerType(), True),
        StructField("shots", IntegerType(), True),
        StructField("shots_on_target", IntegerType(), True),
        StructField("cards_yellow", IntegerType(), True),
        StructField("cards_red", IntegerType(), True),
        StructField("touches", IntegerType(), True),
        StructField("tackles", IntegerType(), True),
        StructField("interceptions", IntegerType(), True),
        StructField("blocks", IntegerType(), True),
        StructField("xg", FloatType(), True),
        StructField("npxg", FloatType(), True),
        StructField("xg_assist", FloatType(), True),
        StructField("sca", IntegerType(), True),
        StructField("gca", IntegerType(), True),
        StructField("passes_completed", IntegerType(), True),
        StructField("passes", IntegerType(), True),
        StructField("passes_pct", FloatType(), True),
        StructField("progressive_passes", IntegerType(), True),
        StructField("carries", IntegerType(), True),
        StructField("progressive_carries", IntegerType(), True),
        StructField("take_ons", IntegerType(), True),
        StructField("take_ons_won", IntegerType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema



def get_stats_passing_summary_schema():
    schema = StructType([
        StructField("passes_completed", IntegerType(), True),
        StructField("passes", IntegerType(), True),
        StructField("passes_pct", DoubleType(), True),
        StructField("passes_total_distance", IntegerType(), True),
        StructField("passes_progressive_distance", IntegerType(), True),
        StructField("passes_completed_short", IntegerType(), True),
        StructField("passes_short", IntegerType(), True),
        StructField("passes_pct_short", DoubleType(), True),
        StructField("passes_completed_medium", IntegerType(), True),
        StructField("passes_medium", IntegerType(), True),
        StructField("passes_pct_medium", DoubleType(), True),
        StructField("passes_completed_long", IntegerType(), True),
        StructField("passes_long", IntegerType(), True),
        StructField("passes_pct_long", DoubleType(), True),
        StructField("xg_assists", DoubleType(), True),
        StructField("pass_xa", DoubleType(), True),
        StructField("assisted_shots", IntegerType(), True),
        StructField("passes_into_final_third", IntegerType(), True),
        StructField("passes_into_penalty_area", IntegerType(), True),   
        StructField("crosses_into_penalty_area", IntegerType(), True),
        StructField("progressive_passes", IntegerType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema


def get_stats_passTypes_summary_schema():
    schema = StructType([
        StructField("passes", IntegerType(), True),
        StructField("passes_live", IntegerType(), True),
        StructField("passes_dead", IntegerType(), True),
        StructField("passes_free_kicks", IntegerType(), True),
        StructField("through_balls", IntegerType(), True),
        StructField("passes_switches", IntegerType(), True),
        StructField("crosses", IntegerType(), True),
        StructField("throw_ins", IntegerType(), True),
        StructField("corner_kicks", IntegerType(), True),
        StructField("corner_kicks_in", IntegerType(), True),
        StructField("corner_kicks_out", IntegerType(), True),
        StructField("corner_kicks_straight", IntegerType(), True),
        StructField("passes_completed", IntegerType(), True),
        StructField("passes_offsides", IntegerType(), True),
        StructField("passes_blocked", IntegerType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema



def get_stats_DefensiveActions_summary_schema():
    schema = StructType([
        StructField("tackles", IntegerType(), True),
        StructField("tackles_won", IntegerType(), True),
        StructField("tackles_def_3rd", IntegerType(), True),
        StructField("tackles_mid_3rd", IntegerType(), True),
        StructField("tackles_att_3rd", IntegerType(), True),
        StructField("challenge_tackles", IntegerType(), True),
        StructField("challenges", IntegerType(), True),
        StructField("challenge_tackles_pct", DoubleType(), True),
        StructField("challenged_lost", IntegerType(), True),
        StructField("blocks", IntegerType(), True),
        StructField("blocked_shots", IntegerType(), True),
        StructField("blocked_passes", IntegerType(), True),
        StructField("interceptions", IntegerType(), True),
        StructField("tackles_interceptions", IntegerType(), True),
        StructField("clearances", IntegerType(), True),
        StructField("errors", IntegerType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema



def get_stats_Possession_summary_schema():
    schema = StructType([
        StructField("touches", IntegerType(), True),
        StructField("touches_def_pen_area", IntegerType(), True),
        StructField("touches_def_3rd", IntegerType(), True),
        StructField("touches_mid_3rd", IntegerType(), True),
        StructField("touches_att_3rd", IntegerType(), True),
        StructField("touches_att_pen_area", IntegerType(), True),
        StructField("touches_live_ball", IntegerType(), True),
        StructField("take_ons", IntegerType(), True),
        StructField("take_ons_won", IntegerType(), True),
        StructField("take_ons_won_pct", DoubleType(), True),
        StructField("take_ons_tackled", IntegerType(), True),
        StructField("take_ons_tackled_pct", DoubleType(), True),
        StructField("carries", IntegerType(), True),
        StructField("carries_distance", IntegerType(), True),
        StructField("carries_progressive_distance", IntegerType(), True),
        StructField("progressive_carries", IntegerType(), True),
        StructField("carries_into_final_third", IntegerType(), True),
        StructField("carries_into_penalty_area", IntegerType(), True),
        StructField("miscontrols", IntegerType(), True),
        StructField("dispossessed", IntegerType(), True),
        StructField("passes_received", IntegerType(), True),
        StructField("progressive_passes_received", IntegerType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema



def get_stats_miscellaneous_summary_schema():
    schema = StructType([
        StructField("cards_yellow", IntegerType(), True),
        StructField("cards_red", IntegerType(), True),
        StructField("cards_yellow_red", IntegerType(), True),
        StructField("fouls", IntegerType(), True),
        StructField("fouled", IntegerType(), True),
        StructField("offsides", IntegerType(), True),
        StructField("crosses", IntegerType(), True),
        StructField("interceptions", IntegerType(), True),
        StructField("tackles_won", IntegerType(), True),
        StructField("pens_won", IntegerType(), True),
        StructField("pens_conceded", IntegerType(), True),
        StructField("own_goals", IntegerType(), True),
        StructField("ball_recoveries", IntegerType(), True),
        StructField("aerials_won", IntegerType(), True),
        StructField("aerials_lost", IntegerType(), True),
        StructField("aerials_won_pct", DoubleType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema





def get_stats_goalkeeper_summary_schema():
    schema = StructType([
        StructField("gk_shots_on_target_against", IntegerType(), True),
        StructField("gk_goals_against", IntegerType(), True),
        StructField("gk_saves", IntegerType(), True),
        StructField("gk_save_pct", DoubleType(), True),
        StructField("gk_psxg", DoubleType(), True),
        StructField("gk_passes_completed_launched", IntegerType(), True),
        StructField("gk_passes_launched", IntegerType(), True),
        StructField("gk_passes_pct_launched", DoubleType(), True),
        StructField("gk_passes", IntegerType(), True),
        StructField("gk_passes_throws", IntegerType(), True),
        StructField("gk_pct_passes_launched", DoubleType(), True),
        StructField("gk_passes_length_avg", DoubleType(), True),
        StructField("gk_goal_kicks", IntegerType(), True),
        StructField("gk_pct_goal_kicks_launched", DoubleType(), True),
        StructField("gk_goal_kick_length_avg", DoubleType(), True),
        StructField("gk_crosses", IntegerType(), True),
        StructField("gk_crosses_stopped", IntegerType(), True),
        StructField("gk_crosses_stopped_pct", DoubleType(), True),
        StructField("gk_def_actions_outside_pen_area", IntegerType(), True),
        StructField("gk_avg_distance_def_actions", DoubleType(), True),
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True)
    ])
    return schema


def get_shots_stats_schema():
    schema = StructType([
        StructField("shot_minute", StringType(), True),
        StructField("player_shot", IntegerType(), True),
        StructField("team_shot", IntegerType(), True),
        StructField("xg", DoubleType(), True),
        StructField("psxg", DoubleType(), True),
        StructField("outcome", IntegerType(), True),
        StructField("distance", DoubleType(), True),
        StructField("body_part", IntegerType(), True),
        StructField("player_assisted_1", IntegerType(), True),
        StructField("event_type", IntegerType(), True),
        StructField("player_assisted_2", IntegerType(), True),
        StructField("event_type_2", IntegerType(), True),
        StructField("match_id", IntegerType(), True)
    ])
    return schema



def get_match_stats_schema():
    schema = StructType([
        StructField("minutes", IntegerType(), True),
        StructField("goals", IntegerType(), True),
        StructField("assists", IntegerType(), True),
        StructField("match_id", IntegerType(), True),
        StructField("player_id", IntegerType(), True), 
    ])
    return schema

def possible_leagues_schema():
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("id", IntegerType(), True),
        StructField("slug", StringType(), True),
        StructField("seasons", ArrayType(StringType()), True),
        StructField("type", StringType(), True)
    ])
    return schema


def get_season_schema():
    schema = StructType([
        StructField("season_year", StringType(), True)
    ])
    return schema

def get_team_schema():
    schema = StructType([
        StructField("team_name", StringType(), True),
        StructField("tournament_team_id", IntegerType(), True)
    ])
    return schema

def get_tournament_schema():
    schema = StructType([
        StructField("tournament_id", IntegerType(), True),
        StructField("nombre_liga", StringType(), True),
        StructField("season_tournament_id", IntegerType(), True),
        StructField("type_of_competition", StringType(), True),
        StructField("tournament_fbref_id", IntegerType(), True)
    ])
    return schema
    

def get_event_shots_schema():
    schema = StructType([
        StructField("event_shot_name", StringType(), True),
    ])
    return schema

def get_body_part_schema():
    schema = StructType([
        StructField("body_part_name", StringType(), True),
    ])
    return schema

def get_outcome_schema():
    schema = StructType([
        StructField("outcome_name", StringType(), True),
    ])
    return schema


def get_type_position_schema():
    schema = StructType([
        StructField("position_name", StringType(), True),
    ])
    return schema

def get_basic_positions_schema():
    print("esquema")

def get_position_player_schema():
    schema = StructType([
        StructField("position_id", IntegerType(), True),
        StructField("match_id", IntegerType(), True),
        StructField("player_id", IntegerType(), True)
    ])
    return schema





def get_all_stats_schema():
    schema = StructType([
        StructField("player_id", IntegerType(), True),
        StructField("stat_id", IntegerType(), True),
        StructField("minutes", IntegerType(), True),
        StructField("goals", IntegerType(), True),
        StructField("assists", IntegerType(), True),
        StructField("shots", IntegerType(), True),
        StructField("shots_on_target", IntegerType(), True),
        StructField("xg", FloatType(), True),
        StructField("npxg", FloatType(), True)
    ])
    return schema
