

export interface StatAPI {
  league_year: string;
  league_name?: string;
  team_name?: string;
  starter_status: StarterStatus;
  stats: StatRecord;
}


type StarterStatus = 'starter' | 'substitute';

type StatRecord = {
  [key: string]: number; 
};