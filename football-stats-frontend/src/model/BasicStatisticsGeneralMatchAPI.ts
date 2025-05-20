

import { MatchAPI } from "./MatchAPI";

export interface StatValue {
    label: string;
    local: number;
    visitor: number;
    type_stat_pct: boolean;
  }
  
  export interface BasicMatchStats {
    match_id: MatchAPI;
  
    aerials_won?: StatValue;
    cards?: StatValue;
    clearances?: StatValue;
    corners?: StatValue;
    crosses?: StatValue;
    fouls?: StatValue;
    goal_kicks?: StatValue;
    interceptions?: StatValue;
    long_balls?: StatValue;
    offsides?: StatValue;
    passing_accuracy?: StatValue;
    possession?: StatValue;
    saves?: StatValue;
    shots_on_target?: StatValue;
    tackles?: StatValue;
    throw_ins?: StatValue;
    touches?: StatValue;
  }
  