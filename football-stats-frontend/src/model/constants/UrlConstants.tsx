

const API_BASE_URL1 = 'https://tfg-backend.blackcliff-a1282891.spaincentral.azurecontainerapps.io/api';
const API_BASE_URL2 = 'http://localhost:8000/api'; // For local development, you can switch to this URL

const API_BASE_URL = 'https://backend-stats-deploy-a4g7bzdng4h8f6d6.spaincentral-01.azurewebsites.net/api/'; // For production, you can switch to this URL

const API_STATS = 'stats';
const API_FILTER = 'filter';
const API_CHART = 'chart';


export const API_ENDPOINTS = {
    ALL_SEASONS: `${API_BASE_URL}/all-seasons/`,
    ALL_LEAGUES: `${API_BASE_URL}/all-leagues/`,
    ALL_SEASON_TOURNAMENTS: `${API_BASE_URL}/season-tournaments/`,


    ALL_GAME_MODES: `${API_BASE_URL}/all-game-modes/`,
    ALL_SPECIFIC_POSITIONS: `${API_BASE_URL}/all-specifics-positions/`,
    ALL_BASIC_POSITIONS: `${API_BASE_URL}/all-basic-positions/`,
    ALL_PLAYERS_BY_MATCH: `${API_BASE_URL}/players-by-match/?match_id=`,
    ALL_SCORES_PLAYERS_MATCH: `${API_BASE_URL}/scores-of-players-match/?match_id=`,
    

    ALL_STATS_MATCH: `${API_BASE_URL}/${API_STATS}/getStatsOfMatch/?match_id=`,

    //api/stats/get-stats-score-filtered-player/
    PLAYER_SCORE_FILTERED: `${API_BASE_URL}/${API_STATS}/get-stats-score-filtered-player/`,
    // http://localhost:8000/api/all-matches/?league_id=${leagueId}
    ALL_MATCHES_BY_LEAGUE_ID: `${API_BASE_URL}/all-matches/?league_id=`,
    // http://localhost:8000/api/match-info/?match_id=${match_id}`
    PRINCIPAL_MATCH_STATS: `${API_BASE_URL}/match-info/?match_id=`,
    // http://localhost:8000/api/get-basic-stats-of-match-comparator/?match_id=
    PRINCIPAL_MATCH_STATS_COMPARATOR: `${API_BASE_URL}/get-basic-stats-of-match-comparator/?match_id=`,
    // api/chart/statsPlayersMatchBasic/?match_id=${match_id}
    STATS_PLAYERS_MATCH_BY_BASIC_POSITION_AND_ORDER_STATS: `${API_BASE_URL}/${API_CHART}/statsPlayersMatchBasic/?match_id=`,
    // http://localhost:8000/api/chart/statsPlayersMatchToChart/?match_id=
    STATS_PLAYERS_MATCH_TO_CHART: `${API_BASE_URL}/${API_CHART}/statsPlayersMatchToChart/?match_id=`,

    
    // http://localhost:8000/api/filter/filtersUnitaryPlayerMatchChart
    FILTER_STATS_MODIFIED: `${API_BASE_URL}/${API_FILTER}/filtersUnitaryPlayerMatchChart/`,
    FILTER_COLUMNS: `${API_BASE_URL}/${API_FILTER}/filterColumnsOfTable/`,
    FILTER_TEAMS: `${API_BASE_URL}/${API_FILTER}/filterTeamsOfLeagues/`,
    FILTER_TABLES_OF_ALL_STATS_OF_MATCH: `${API_BASE_URL}/${API_FILTER}/filtersMatchChart/`,
    FILTER_TABLES_ORDER_STATS_OF_MATCH: `${API_BASE_URL}/${API_FILTER}/filtersUnitaryPlayerMatchChart/`,


    // http://localhost:8000/api/stats/tournaments/get-stats-by-leagues/?league_name=La%20Liga&type_of_stats=passes_team_pct
    LEAGUES_STATS: `${API_BASE_URL}/${API_STATS}/tournaments/get-stats-by-leagues/`,
    LEAGUE_CHART: `${API_BASE_URL}/${API_CHART}/tournaments/get-unitary-stat-by-leagues/`,

    TEAM_STATS: `${API_BASE_URL}/${API_STATS}/teams/get-stats-by-teams-of-match/`,
    TEAM_CHART: `${API_BASE_URL}/${API_CHART}/teams/get-unitary-stat-by-teams-of-match/`,


};
