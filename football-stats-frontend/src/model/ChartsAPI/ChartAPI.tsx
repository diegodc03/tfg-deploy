

export interface ChartAPI {
  league_year: string;
  league_name?: string;
  team_name?: string;
  starter_status: StarterStatus;
  value: number;
}

type StarterStatus = 'starter' | 'substitute';

