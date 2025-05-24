


from ..models import FootballMatch
from ..models import MatchPlayerScore
from ..models import MatchStatistics
from ..models import StatsDefenseSummary
from ..models import StatsGoalkeeperSummary
from ..models import StatsMiscellaneousSummary
from ..models import StatsPassingSummary
from ..models import StatsPassTypesSummary
from ..models import StatsPossessionSummary
from ..models import StatsSummary


from ..serializers_dto.tables_serializers import StatsSummarySerializer
from ..serializers_dto.tables_serializers import StatsDefensiveActionsSerializer
from ..serializers_dto.tables_serializers import StatsGKSerializer
from ..serializers_dto.tables_serializers import StatsMiscellaneousSerializer
from ..serializers_dto.tables_serializers import StatsPassingSerializer
from ..serializers_dto.tables_serializers import StatsPassTypesSerializer
from ..serializers_dto.tables_serializers import StatsPossessionSerializer
# Estadísticas a mostrar en el endPoint de datos
# Se van a distribuir segun el tipo de tabla para así mostrarse en el frontal mas ordenado


stats_columns = {
    "stats_summary": ["touches", "shots", "xg", "passes_completed", "passes", "passes_pct", "progressive_passes", "carries", "take_ons"],
    "stats_possession_summary": ["touches", "touches_def_pen_area", "touches_def_3rd", "touches_mid_3rd", "touches_att_3rd", "touches_att_pen_area", "touches_live_ball", "take_ons", "take_ons_won_pct", "carries", "carries_distance", "carries_progressive_distance", "progressive_distance", "miscontrols", "dispossessed", "passes_received", "progressive_passes_received"],
    "stats_passTypes_summary": ["passes", "passes_live", "passes_dead", "passes_free_kicks", "through_balls", "passes_switches", "crosses", "throw_ins", "passes_completed", "passes_offsides"],
    "stats_passing_summary": ["passes_completed", "passes", "passes_pct", "passes_total_distance", "passes_progressive_distance", "passes_completed_short", "passes_short", "passes_pct_short", "passes_completed_medium", "passes_medium", "passes_pct_medium", "passes_completed_long", "passes_long", "passes_pct_long", "xg_assists", "assisted_shots", "passes_into_final_third", "passes_into_penalty_area", "crosses_into_penalty_area", "progressive_passes"],
    "stats_miscellaneous_summary": ["fouls", "fouled", "cards_yellow", "cards_red", "offsides", "crosses", "interceptions", "tackles_won", "ball_recoveries", "aerials_won", "aerials_lost", "aerials_won_pct"],
    "stats_defensiveactions_summary": ["tackles", "tackles_won", "tackles_def_3rd", "tackles_mid_3rd", "tackles_att_3rd", "challenges_tackles", "challenges", "challenges_tackles_pct", "challenged_lost", "blocks", "blocked_shots", "interceptions", "tacles_interceptions", "clearences", "errors"],
    "stats_gk_summary": ["gk_shots_on_target_against", "gk_goals_against", "gk_saves", "gk_save_pct", "gk_psxg", "gk_passes_completed_launched", "gk_passes_launched", "gk_passes_pct_launched", "gk_passes", "gk_passes_throws", "gk_pct_passes_launched", "gk_passes_length_avg", "gk_goal_kicks", "gk_pct_goal_kicks_launched", "gk_goal_kick_length_avg", "gk_crosses", "gk_crosses_stopped", "gk_crosses_stopped_pct", "gk_def_actions_outside_pen_area", "gk_avg_distance_def_actions"]
}


model_map_serializer = {
    "stats_defensiveactions_summary": [StatsDefenseSummary, StatsDefensiveActionsSerializer],    
    "stats_gk_summary": [StatsGoalkeeperSummary, StatsGKSerializer],
    "stats_miscellaneous_summary": [StatsMiscellaneousSummary, StatsMiscellaneousSerializer],
    "stats_passing_summary": [StatsPassingSummary, StatsPassingSerializer],
    "stats_passTypes_summary": [StatsPassTypesSummary, StatsPassTypesSerializer],
    "stats_possession_summary": [StatsPossessionSummary, StatsPossessionSerializer],
    "stats_summary": [StatsSummary, StatsSummarySerializer],
}

model_map = {
    "stats_defensiveactions_summary": StatsDefenseSummary, 
    "stats_gk_summary": StatsGoalkeeperSummary,
    "stats_miscellaneous_summary": StatsMiscellaneousSummary,
    "stats_passing_summary": StatsPassingSummary,
    "stats_passTypes_summary": StatsPassTypesSummary,
    "stats_possession_summary": StatsPossessionSummary,
    "stats_summary": StatsSummary,
}




stats_columns_player = {
    "passes_player_pct": {
        "tables": ["stats_passing_summary"],
        "columns": ["passes", "passes_pct", "passes_pct_short", "passes_pct_medium", "passes_pct_long"]
    },
    "passes_player_completed": {
        "tables": ["stats_passing_summary"],
        "columns": ["passes_completed", "passes_completed_short", "passes_completed_medium", "passes_completed_long"]
    },
    "passes_player": {
        "tables": ["stats_passing_summary"],
        "columns": ["passes", "passes_completed", "passes_completed_short", "passes_short", "passes_completed_medium", "passes_medium", "passes_completed_long", "passes_long"]
    },
    "tackles_player": {
        "tables": ["stats_defensiveactions_summary"],
        "columns": ["tackles", "tackles_won", "tackles_def_3rd", "tackles_mid_3rd", "tackles_att_3rd"]
    },
    "aerials_player": {
        "tables": ["stats_miscellaneous_summary"],
        "columns": ["aerials_won", "aerials_lost", "aerials_won_pct"]
    },
    "types_passes_player": {
        "tables": ["stats_passTypes_summary"],
        "columns": ["passes_live", "passes_dead", "passes_free_kicks", "through_balls", "passes_switches", "crosses", "throw_ins"]
    },
    "shots_player": {
        "tables": ["stats_summary", "stats_passing_summary"],
        "columns": ["shots", "shots_on_target", "xg", "xg_assists", "assisted_shots"]
    }
}


# Para las comparaciones de los equipos de futbol se va a hacer con lo de arriba, pero se van a mostrar todas las estadísticas, ya que no pasa como en un partido que 
# muchas pueden ser 0
# para un equipo tambien se van a mostrar las unitarias de equipo, que puede ser interesante

filter_labels_unitary = {
    "passes_player": "Distribución de pases",
    "passes_player_completed": "Pases completados",
    "passes_player_pct": "Porcentajes de pase",
    "tackles_player": "Entradas defensivas",
    "aerials_player": "Duelos aéreos",
    "types_passes_player": "Tipos de pase",
    "shots_player": "Tiros y asistencias esperadas"
}

filter_labels_match = {
    "stats_summary": "Resumen de estadísticas",
    "stats_possession_summary": "Estadísticas de posesión",
    "stats_passTypes_summary": "Estadísticas de Tipos de pase",
    "stats_passing_summary": "Estadísticas de pases",
    "stats_miscellaneous_summary": "Estadísticas de estadísticas varias",
    "stats_defensiveactions_summary": "Estadísticas de acciones defensivas",
    "stats_gk_summary": "Estadísticas del portero"
}



stats_mapping = {
                "aerials_won": {"type_stat_pct": False},
                "cards": {"type_stat_pct": False},
                "clearances": {"type_stat_pct": False},
                "corners": {"type_stat_pct": False},
                "crosses": {"type_stat_pct": False},
                "fouls": {"type_stat_pct": False},
                "goal_kicks": {"type_stat_pct": False},
                "interceptions": {"type_stat_pct": False},
                "long_balls": {"type_stat_pct": False},
                "offsides": {"type_stat_pct": False},
                "passing_accuracy": {"type_stat_pct": True},
                "possession": {"type_stat_pct": True},
                "saves": {"type_stat_pct": True},
                "shots_on_target": {"type_stat_pct": True},
                "tackles": {"type_stat_pct": False},
                "throw_ins": {"type_stat_pct": False},
                "touches": {"type_stat_pct": False},
            }