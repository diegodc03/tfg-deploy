
import { TeamAPI } from './TeamApi';

import {TournamentAPI} from './TournamentAPI';

export interface MatchAPI {
    match_id: number;
    Home: TeamAPI;
    Away: TeamAPI;
    Score: string;
    Wk: number | string;
    Date: Date;
    Season: TournamentAPI;
}



export interface MatchAPISearch extends MatchAPI {
    Attendance: string;
    Referee: string;
    Venue: string;
}