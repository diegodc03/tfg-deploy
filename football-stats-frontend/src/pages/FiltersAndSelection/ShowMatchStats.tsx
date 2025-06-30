import { Box, Container, Grid, Stack, Typography } from "@mui/material";

import CardShow from "../../components/Cards";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { MatchAPISearch } from "../../model/MatchAPI";
import BasicInfoMatch from "../../components/BasicInfoMatch";
import ShowBasicStats from "./showBasicStats";
import { API_ENDPOINTS } from "../../model/constants/UrlConstants";
import { serviceItemsStatsPage } from "../../model/constants/menuItems";
import { matchBasicInfo } from "../../model/constants/GeneralInfoOfMatch";
import ErrorSnackbar from "../../components/showError";
import {ERROR_MESSAGES} from '../../model/constants/errorConstants';


const ShowMatchStats = () => {

    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    const { match_id } = useParams();
    const [tournamentId, setTournamentId] = useState<number | undefined>(undefined);
    const [matchStats, setMatchStats] = useState<MatchAPISearch>();

           
    useEffect(() => {

        if (!match_id) return;

        const fetchData = async () => {
            try {
                const response = await fetch(API_ENDPOINTS.PRINCIPAL_MATCH_STATS + `${match_id}`);
                
                if (!response.ok) {
                    throw new Error(ERROR_MESSAGES.NOT_FOUND_MATCH_INFO);
                }
                const data = await response.json();
                
                setMatchStats(data);
                setTournamentId(data.Season?.tournament_id);
                setIsLoading(false);

            } catch (error: any) {
                setErrorMessage(ERROR_MESSAGES.NOT_FOUND_MATCH_INFO);
                setShowError(true);
                setIsLoading(false); 
            }
        };
        
        fetchData();
    }
    , [match_id]);

    
    useEffect(() => {
        if (!match_id) return;

        const preloadPlayerData = async () => {
            try {
                const [playersRes] = await Promise.all([
                    fetch(`${API_ENDPOINTS.ALL_PLAYERS_BY_MATCH}${match_id}`),
                ]);

                if (!playersRes.ok) {
                    throw new Error('Error preloading scores or players');
                }

                const players = await playersRes.json();

                localStorage.setItem(`players_match_${match_id}`, JSON.stringify(players));

            } catch (err) {
                console.warn('Error precargando datos de jugadores:', err);
            }
        };

        preloadPlayerData();
    }, [match_id]);


    return (
        <>
            <ErrorSnackbar
                open={showError}
                onClose={() => setShowError(false)}
                message={errorMessage ?? "Ha ocurrido un error inesperado"}
                position={{ vertical: 'top', horizontal: 'right' }}
                large={true}
            />


            <Container maxWidth="lg" sx={{ marginTop: '3rem', marginBottom: '5vh' }}>           
                
                <Box
                    sx={{
                        backgroundColor: 'rgba(255, 255, 255, 0.7)',
                        padding: 2,
                        paddingBottom:0,
                        paddingLeft: 3,
                        borderRadius: 4,
                    }}
                >
                    <Typography gutterBottom  variant="h6" sx={{ fontWeight: 'bold', marginBottom: 2 }}>
                        <strong>Listado de resultados </strong>
                    </Typography>
                    {matchStats && matchStats.Home && matchStats.Away && (
                        <BasicInfoMatch stats={matchBasicInfo(matchStats)} />
                    )}


                </Box>
          


                <Box
                    sx={{
                        backgroundColor: 'rgba(255, 255, 255, 0.7)',
                        padding: 2,
                        marginTop: 6,
                        borderRadius: 4,
                      
                    }}
                >
                    <Typography gutterBottom  variant="h6" sx={{  fontWeight: 'bold' ,marginBottom: 2 }}>
                        <strong>Estadísticas disponibles del partido</strong>
                    </Typography>
                    <Grid
                        container
                            size={{ xs: 12, sm: 6, md: 3 }}
                            spacing={5}
                            sx={{
                                borderRadius: 4,
                                
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
                </Box>
                <Stack  sx={{  backgroundColor: 'rgba(255, 255, 255, 0.7)', borderRadius: 4, padding: 3, marginBottom:6, marginTop: 8 }} >
                    <ShowBasicStats matchId={Number(match_id)} />
                </Stack>
                
            </Container>
        </>
    );
}


export default ShowMatchStats;