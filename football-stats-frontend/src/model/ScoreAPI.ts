
import { MatchStatisticsAPI } from "./MatchStatisticsAPI";
import { BasicPositionAPI } from "./BasicPositionAPI";
import { SpecificPositionAPI } from "./SpecificPositionAPI";
import { GameModeTypeAPI } from "./GameModeTypeAPI";

export interface ScoreAPI {
    match_player_score_id: number;
    team_name?: string;
    match_player_id: MatchStatisticsAPI;
    specific_position_id: SpecificPositionAPI;
    basic_position_id: BasicPositionAPI;
    score: number;
    game_mode_id: GameModeTypeAPI;
}



    


