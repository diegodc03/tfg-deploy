import { MatchAPISearch } from "../MatchAPI";



export const matchBasicInfo = (matchStats: MatchAPISearch) => {
    return [
        { label: "Partido", value: matchStats.Home.team_name + " - " + matchStats.Away.team_name },
        { label: "Resultado", value: matchStats.Score },
        { label: "Fecha", value: matchStats.Date.toString() },
        { label: "Jornada", value: matchStats.Wk },
        { label: "Asistencia", value: matchStats.Attendance },
        { label: "Estadio de Juego", value: matchStats.Venue },
        { label: "Árbitro Principal", value: matchStats.Referee }
    ];
}
