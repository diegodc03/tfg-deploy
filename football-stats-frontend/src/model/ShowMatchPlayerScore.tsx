
import { GameModeTypeAPI } from './GameModeTypeAPI';
import { BasicPositionAPI } from './BasicPositionAPI';
import { SpecificPositionAPI } from './SpecificPositionAPI';

export interface MatchPlayerScore {
  match_player_score_id: number;
  match_player_id: number;
  specific_position_id: SpecificPositionAPI;
  basic_position_id: BasicPositionAPI;
  score: number;
  game_mode_id: GameModeTypeAPI;
}