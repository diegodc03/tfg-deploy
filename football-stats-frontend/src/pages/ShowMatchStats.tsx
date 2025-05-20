import { Box, Container, Stack, Typography } from "@mui/material";
import realMadridImg from "../images/real_madrid.jpg";
import CardShow from "../components/Cards";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { MatchAPISearch } from "../model/MatchAPI";
import BasicInfoMatch from "../components/BasicInfoMatch";

const ShowMatchStats = () => {

    const [isLoading, setIsLoading] = useState(true);

    const { match_id } = useParams();
    const [matchStats, setMatchStats] = useState<MatchAPISearch>();

    const type_of_stats_recorded = [
        { image: realMadridImg, title: 'Puntuaciones', text: 'Puntuaciones de los jugadores del partido segun su posicion y tambien la forma de juego' },
        { image: realMadridImg, title: 'Estadísticas de jugadores', text: 'Todas las estadísticas de los jugadores (pases, goles...) ' },
        { image: realMadridImg, title: 'Comparacion de jugadores', text: 'Compara los jugadores del partido para poder ver cosas que nunca habias visto' },
      ];

   

        
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/match-info/?match_id=${match_id}`);
               
                if (!response.ok) {
                    throw new Error('Error fetching match stats');
                }
                const data = await response.json();
                
                setMatchStats(data);
                console.log(data);
                setIsLoading(false);
            } catch (error) {
                console.error('Error fetching match stats:', error);
            }
        };
        fetchData();
    }
    , [match_id]);

    const stats = matchStats
        ? [
            { label: "match_id", value: matchStats.match_id },
            { label: "Partido", value: matchStats.Home.team_name +" - "+ matchStats.Away.team_name},
            { label: "Resultado", value: matchStats.Score },
            { label: "Fecha", value: matchStats.Date.toString() },
            { label: "Jornada", value: matchStats.Wk },
            { label: "Attendance", value: matchStats.Attendance },
            { label: "Stadium", value: matchStats.Venue },
            { label: "Referee", value: matchStats.Referee },

        ]
    : [];

    return (
        <Box
                sx={{
                    backgroundImage: `url(${realMadridImg})`,
                    backgroundRepeat: 'no-repeat',
                    backgroundAttachment: 'fixed',
                    backgroundSize: 'cover',
                    minHeight: '100vh',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    
                }}>
            <Container>
                            
                <Typography gutterBottom sx={{ marginTop: 4, fontWeight: 'bold' }}>
                    <strong>Listado de resultados </strong>
                </Typography>
                    
                <BasicInfoMatch  stats={stats} />

                <Typography gutterBottom sx={{ marginTop: 6, fontWeight: 'bold', color: 'black' }}>
                    <strong>Estadísticas disponibles del partido</strong>
                </Typography>
                <Stack direction={"row"}  sx={{  backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 3 }} >
                    <CardShow title={"Estadísticas de jugadores"} text={"Todas las estadísticas de los jugadores (pases, goles...) "} image={realMadridImg} />
                    <CardShow title={"Comparacion de jugadores"} text={"Compara los jugadores del partido para poder ver cosas que nunca habias visto"} image={realMadridImg} />
                    <CardShow title={"Puntuaciones"} text={"Puntuaciones de los jugadores del partido segun su posicion y tambien la forma de juego"} image={realMadridImg} navigateElement={`/match-stats-score/${match_id}`}  />
                </Stack>
            </Container>
        </Box>
    );
}



export default ShowMatchStats;