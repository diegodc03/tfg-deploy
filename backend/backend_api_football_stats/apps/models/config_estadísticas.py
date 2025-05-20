ESTADISTICAS_INTERESANTES = {
    'stats_summary': {
        'modelo': 'app.stats_summary',
        'columnas': ['touches', 'passes_completed', 'passes', 'passes_pct', 'carries'],
    },
    'stats_defensiveactions_summary': {
        'modelo': 'app.stats_defensiveactions_summary',
        'columnas': ['tackles', 'interceptions', 'tackles_interceptions', 'clearances', 'challenges'],
    },
    'stats_gk_summary': {
        'modelo': 'app.stats_gk_summary',
        'columnas': ['gk_shots_on_target_against', 'gk_goals_against', 'gk_saves', 'gk_save_pct', 'gk_psxg', 'gk_passes', 'gk_passes_length_avg', 'gk_crosses', 'gk_avg_distance_def_actions'],
    },
    'stats_miscellaneous_summary': {
        'modelo': 'app.stats_miscellaneous_summary',
        'columnas': ['fouls', 'fouled', 'ball_recoveries'],
    },
    'stats_passing_summary': {
        'modelo': 'app.stats_passing_summary',
        'columnas': ['passes', 'passes_completed', 'passes_pct', 'passes_total_distance', 'passes_progressive_distance', 'xg_assists', 'passes_into_final_third', 'passes_into_penalty_area'],
    },
    'stats_possession_summary': {
        'modelo': 'app.stats_possession_summary',
        'columnas': ['touches', 'touches_live_ball', 'carries', 'carries_progressive_distance', 'passes_received'],
    },
    'stats_passTypes_summary': {
        'modelo': 'app.stats_passTypes_summary',
        'columnas': ['passes', 'passes_live', 'passes_dead', 'passes_free_kicks', 'passes_completed', 'passes_blocked'],
    },
}