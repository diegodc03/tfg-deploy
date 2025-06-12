

const API_BASE_URL = 'http://localhost:8000/api';

const API_STATS = 'stats';
const API_FILTER = 'filter';
const API_CHART = 'chart';


export const API_ENDPOINTS = {
    ALL_MATCHES: `${API_BASE_URL}/all-matches/`,
    ALL_SEASONS: `${API_BASE_URL}/all-seasons/`,
    ALL_LEAGUES: `${API_BASE_URL}/all-leagues/`,
    ALL_TOURNAMENTS: `${API_BASE_URL}/season-tournaments/`,
    ALL_BASIC_POSITIONS: `${API_BASE_URL}/all-basic-positions/`,

    //http://localhost:8000/api/filter/filtersUnitaryPlayerMatchChart
    FILTER_STATS_MODIFIED: `${API_BASE_URL}/${API_FILTER}/filtersUnitaryPlayerMatchChart/`,
    FILTER_COLUMNS: `${API_BASE_URL}/${API_FILTER}/filterColumnsOfTable/`,

    //http://localhost:8000/api/stats/tournaments/get-stats-by-leagues/?league_name=La%20Liga&type_of_stats=passes_team_pct
    LEAGUES_STATS: `${API_BASE_URL}/${API_STATS}/tournaments/get-stats-by-leagues/`,
    LEAGUE_CHART: `${API_BASE_URL}/${API_CHART}/tournaments/get-unitary-stat-by-leagues/`,

    TEAM_STATS: `${API_BASE_URL}/${API_STATS}/teams/get-stats-by-teams-of-match/`,
    TEAM_CHART: `${API_BASE_URL}/${API_CHART}/teams/get-unitary-stat-by-teams-of-match/`,
};
