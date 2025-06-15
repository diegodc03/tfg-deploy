import { Box, Container, Grid, Stack, Typography } from "@mui/material";
import realMadridImg from "../images/real_madrid.jpg";
import CardShow from "../components/Cards";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { MatchAPISearch } from "../model/MatchAPI";
import BasicInfoMatch from "../components/BasicInfoMatch";
import ShowBasicStats from "../components/showBasicStats";
import { API_ENDPOINTS } from "../model/constants/UrlConstants";
import { serviceItemsStatsPage } from "../model/constants/menuItems";


const ShowMatchStats = () => {

    const [isLoading, setIsLoading] = useState(true);

    const { match_id } = useParams();
    const [tournamentId, setTournamentId] = useState<number | undefined>(undefined);
    const [matchStats, setMatchStats] = useState<MatchAPISearch>();

           
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(API_ENDPOINTS.PRINCIPAL_MATCH_STATS + `${match_id}`);
                if (!response.ok) {
                    throw new Error('Error fetching match stats');
                }
                const data = await response.json();
                
                setMatchStats(data);
                setTournamentId(data.Season?.tournament_id);
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
            { label: "Partido", value: matchStats.Home.team_name +" - "+ matchStats.Away.team_name},
            { label: "Resultado", value: matchStats.Score },
            { label: "Fecha", value: matchStats.Date.toString() },
            { label: "Jornada", value: matchStats.Wk },
            { label: "Asistencia", value: matchStats.Attendance },
            { label: "Estadio de Juego", value: matchStats.Venue },
            { label: "Árbitro Principal", value: matchStats.Referee }
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
                <Grid
                    container
                        size={{ xs: 12, sm: 6, md: 3 }}
                        spacing={5}
                        sx={{
                            backgroundColor: 'rgba(255, 255, 255, 0.9)',
                            borderRadius: 2,
                            padding: 3,
                            marginLeft:'auto',
                            marginRight:'auto',
                            display: 'flex', 
                            justifyContent: 'center', 
                            alignItems: 'center'
                        }}
                    >
                    {serviceItemsStatsPage(
                        match_id as string,
                        String(tournamentId)
                    ).map((item, index) => (
                        <Grid key={index}  >
                            <CardShow {...item} />
                        </Grid>
                    ))}
                </Grid>
                
                <Stack  sx={{  backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 3, marginBottom:6, marginTop: 8 }} >
                    <ShowBasicStats matchId={Number(match_id)} />
                </Stack>

            </Container>
        </Box>
    );
}



export default ShowMatchStats;