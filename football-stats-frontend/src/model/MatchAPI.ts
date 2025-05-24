
import { TeamAPI } from './TeamApi';

import {Tournament} from './TournamentAPI';

export interface MatchAPI {
    match_id: number;
    Home: TeamAPI;
    Away: TeamAPI;
    Score: string;
    Wk: number | string;
    Date: Date;
    Season: Tournament;
}



export interface MatchAPISearch extends MatchAPI {
    Attendance: string;
    Referee: string;
    Venue: string;
}