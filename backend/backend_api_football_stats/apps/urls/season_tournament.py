# apps/api/urls/season_tournament_view_urls.py
from django.urls import path

from ..api.basic_visualize_of_match import BasicVisualizeOfMatchView
from ..api.basic_stats_of_match_comparator_view import BasicStatsOfMatchComparatorView
from ..api.season_tournament_view import SeasonTournamentView
from ..api.tournament_view import TournamentView
from ..api.season_view import SeasonView
from ..api.football_match_view import FootballMatchView
from ..api.Leagues_view import LeaguesView
from ..api.match_stats_score_view import MatchStatsScoreView
from ..api.basic_positions_view import BasicPositionsView
from ..api.specific_positions_view import SpecificPositionsView
from ..api.game_modes_view import GameModesView

app_name = 'season_tournament'  # Esto le da un nombre a este conjunto de rutas

urlpatterns = [
    path('season-tournaments/', SeasonTournamentView.as_view(), name='season_tournament_list'),
    path('all-tournaments/', TournamentView.as_view(), name='all_tournament_list'),  # Ruta para obtener todos los torneos
    path('all-seasons/', SeasonView.as_view(), name='all_season_list'),  # Ruta para obtener todas las temporadas
    path('all-matches/', FootballMatchView.as_view(), name='all_matches_list'),  # Ruta para obtener todos los partidos
    path('all-leagues/', LeaguesView.as_view(), name='all_leagues'),  # Ruta para obtener todas las temporadas
    path('match-info/', BasicVisualizeOfMatchView.as_view(), name='match_info'),  # Ruta para obtener información de un partido específico
    path('get-basic-stats-of-match-comparator/', BasicStatsOfMatchComparatorView.as_view(), name='get_basic_stats_of_match_comparator'),  # Ruta para obtener estadísticas básicas de un partido
    path('scores-of-players-match/', MatchStatsScoreView.as_view(), name='get_scores_of_matchs'),  # Ruta para obtener estadísticas básicas de un partido
    path('all-game-modes/', GameModesView.as_view(), name='get_game_modes'),  # Ruta para obtener estadísticas básicas de un partido
    path('all-basic-positions/', BasicPositionsView.as_view(), name='get_basic_position_category'),  # Ruta para obtener estadísticas básicas de un partido
    path('all-specifics-positions/', SpecificPositionsView.as_view(), name='get_specifics_positions_by_category'),  # Ruta para obtener estadísticas básicas de un partido
]

