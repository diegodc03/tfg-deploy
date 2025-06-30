export const STORAGE_KEYS = {
  season_tournaments: 'unique_tournaments', // Aún no está en API_ENDPOINTS, se ignora o puedes añadirlo si es necesario
  seasons: 'unique_seasons',
  leagues: 'unique_leagues',
  basicPositions: 'unique_basic_positions',
  specificPositions: 'unique_specific_positions',
  gameModes: 'unique_game_modes',

// 🔽 Añadimos estas dos claves nuevas con `match_id` dinámico
  playersByMatch: (matchId: string | number) => `players_match_${matchId}`,
  scoresByMatch: (matchId: string | number) => `scores_match_${matchId}`,
};