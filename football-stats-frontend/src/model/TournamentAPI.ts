



export interface SeasonTournament {
    season_id: number;
    season_year: string;
}
  
export interface Tournament {
    tournament_id: number;
    nombre_liga: string;
    season_tournament: SeasonTournament;
}
