# apps/api/urls/season_tournament_view_urls.py
from django.urls import path

from ..api.filter_chart_labels.get_teams_of_league_view import GetTeamsOfLeagueView
from ..api.filter_chart_labels.get_only_tables_filters import FiltersColumnOfTableView
from ..api.get_chart_unitary_stat_league import GetUnitaryStatTournamentComparisonOfLeaguesView
from ..api.get_chart_unitary_stat_team import GetUnitaryStatTeamsComparisonOfLeaguesView
from ..api.get_all_season_league_comparison import GetStatsLeaguesComparison
from ..api.get_teams_stats_comparison_of_leagues_view import GetStatsTeamsComparisonOfLeaguesView
from ..api.players_view import PlayersView
from ..api.get_stats_score_of_filtered_players_view import GetStatsScoreFilteredPlayerView
from ..api.get_stats_match_to_chart_basic_stats import GetStatsMatchToChartBasicStatsView
from ..api.get_stats_teams_view import GetStatsTeamsUnitaryView
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

from ..api.filter_chart_labels.filter_match_chart import FiltersMatchChartView
from ..api.filter_chart_labels.filter_unitary_player_match_chart import FiltersUnitaryPlayerMatchChartView

from ..api.get_stats_for_match_unique_players_to_chart import GetStatsPlayersToChartView
from ..api.get_stats_match_to_chart_view import GetStatsMatchToChartView

from ..api.get_stats_of_players_match_view import GetStatsOfPlayersMatchView


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
    
    

    path('filter/filtersMatchChart/', FiltersMatchChartView.as_view(), name='filters_match_chart'),  # Ruta para obtener los filtros de los partidos
    path('filter/filtersUnitaryPlayerMatchChart/', FiltersUnitaryPlayerMatchChartView.as_view(), name='filters_unitary_player_match_chart'),  # Ruta para obtener los filtros de los partidos
    path('filter/filterColumnsOfTable/', FiltersColumnOfTableView.as_view(), name='filter_columns_of_table'),  # Ruta para obtener los filtros de las columnas de la tabla
    path('filter/filterTeamsOfLeagues/', GetTeamsOfLeagueView.as_view(), name='filter_teams_of_leagues'),  # Ruta para obtener los equipos de las ligas
    
    path('chart/statsPlayersMatchToChart/', GetStatsPlayersToChartView.as_view(), name='get_stats_players_to_chart'),  # Ruta para obtener los filtros de los partidos
    path('chart/statsToChart/', GetStatsMatchToChartView.as_view(), name='get_stats_of_match_chart'),  # Ruta para obtener las estadísticas de los jugadores en un partido
    path('chart/statsPlayersMatchBasic/', GetStatsMatchToChartBasicStatsView.as_view(), name='get_stats_of_match_basic_stats'),  # Ruta para obtener las estadísticas básicas de los jugadores en un partido


    path('stats/getStatsOfMatch/', GetStatsOfPlayersMatchView.as_view(), name='get_stats_of_players_match'),  # Ruta para obtener las estadísticas de los jugadores en un partido
    path('stats/getTeamsStats/', GetStatsTeamsUnitaryView.as_view(), name='get_stats_of_teams_match'),  # Ruta para obtener las estadísticas de los equipos en un partido
    
    path('stats/get-stats-score-filtered-player/', GetStatsScoreFilteredPlayerView.as_view(), name='get_stats_score_of_filtered_players'),  # Ruta para obtener las estadísticas de los jugadores en un partido filtrado por jugador y partido
    path('players-by-match/', PlayersView.as_view(), name='get_stats_of_players_match'),  # Ruta para obtener las estadísticas de los jugadores en un partido
    
    
    
    path('stats/teams/get-stats-by-teams-of-match/', GetStatsTeamsComparisonOfLeaguesView.as_view(), name='get_stats_by_teams_of_match'),  # Ruta para obtener las estadísticas de los equipos en un partido
    path('chart/teams/get-unitary-stat-by-teams-of-match/', GetUnitaryStatTeamsComparisonOfLeaguesView.as_view(), name='get_stats_by_teams_of_match_chart'),  # Ruta para obtener las estadísticas de los equipos en un partido
    
    
    path('stats/tournaments/get-stats-by-leagues/', GetStatsLeaguesComparison.as_view(), name='get_stats_by_leagues'),  # Ruta para obtener las estadísticas de los equipos en un partido
    path('chart/tournaments/get-unitary-stat-by-leagues/', GetUnitaryStatTournamentComparisonOfLeaguesView.as_view(), name='get_unitary_stat_by_leagues'),  # Ruta para obtener las estadísticas de los equipos en un partido
    # Falta hacer los endpoints para devolver las puntuaciones de los equipos
    # Falta hacer los endpoints para devolver las puntuaciones por liga
    # Se hara un chart parecido como el de arriba, tiene que ser que se elija un equipo o liga y se compare con las difrentes ligas

]

