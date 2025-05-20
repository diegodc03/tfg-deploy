import { PlayerAPI } from "./PlayerAPI";
import { MatchAPI } from "./MatchAPI";

export interface MatchStatisticsAPI {

    stadistic_id: number;
    match_id: MatchAPI; 
    player_id: PlayerAPI; 
    minutes: number; 
    goals: number;
    assists: number;
}





    