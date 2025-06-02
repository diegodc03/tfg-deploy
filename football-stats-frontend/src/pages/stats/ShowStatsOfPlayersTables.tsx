




import { Box, Button, Container, Grid, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import realMadridImg from "../../images/real_madrid.jpg";
import GenericSelectProps from '../../components/MultipleSelect';
import { TablesStats } from '../../model/tablesStats/TablesStats';
import StatsOfMatchPlayers from '../../components/statsOfMatchPlayers';
import { StatsList } from '../../components/charts/StatsList';
/**
 * 
 * Este componente se va a encargar de mostrar las tablas de las diferentes estadísticas de los jugadores en un partido
 * La intencion es poder filtrar por cada una de las tablas de estadísticas pero tambien poder mostrar todas las statísticas
 * Por último se va a filtrar también por  posicion básica del jugador 
 * 
 * 
 * @returns JSX.Element
 * @description This component is used to show the stats from teams.
 */



export default function ShowStatsOfPlayersOnMatch() {


    const {match_id} = useParams();
    const [isLoading, setIsLoading] = useState(true);

    const [type_table_stats, setTypeTableStats] = useState<string>('stats_summary'); 
    const [filterSetTableStats, setFilterSetTableStats] = useState<TablesStats[]>(); 

    const [data, setData] = useState<any[]>([]); // Aquí se guardarán los datos de las estadísticas de los jugadores

    useEffect(() => {
        const fetchData = async () => {
            try {

                const [playersStatsResponse, filterTablesResponse] = await Promise.all([
                    fetch(`http://localhost:8000/api/stats/getStatsOfMatch/?match_id=${match_id}`),
                    fetch(`http://localhost:8000/api/filter/filtersMatchChart/`)
                ]);

                if (!playersStatsResponse.ok || !filterTablesResponse.ok) {
                    throw new Error('Error fetching data');
                }

                const [playersStatsData, filterTablesData] = await Promise.all([
                    playersStatsResponse.json(),
                    filterTablesResponse.json()
                ]); 


                setFilterSetTableStats(filterTablesData);
                setData(playersStatsData);

                setIsLoading(false);

                console.log('Datos de las estadísticas de los jugadores:', playersStatsData);
                console.log('Datos de los filtros de las tablas:', filterTablesData);

            } catch (error) {
                console.error('Error fetching player stats:', error);
            }
        
    }
        fetchData();
    }, [match_id]);

    const handleChangeTableStats = (value: string) => {
        setTypeTableStats(value);
    };

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
            }}
        >
            <LoadingIndicator isLoading={isLoading} />


            <Container maxWidth="lg" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>
            
                <Typography>
                    <strong>Filtrar por tipo de estadística y equipo</strong>
                </Typography>

                <Grid 
                    container
                    columnSpacing={{ xs: 1, sm: 2 }}
                    rowSpacing={{ xs: 1, sm: 2, md: 3 }}
                    spacing={{ xs: 1, sm: 2, md: 4 }}
                    
                    justifyContent="center"
                    sx={{
                        backgroundColor: '#f8f9fa',
                        padding: 2,
                        borderRadius: 2,
                        marginTop: 1,
                        marginBottom: 5,
                    }}
                >


                    

                    {/** Aqui faltaría meter tipo de grafico que se quiere */}



                    
                    {/** Aqui faltaría meter tipo de jugador básico */}


                </Grid>
                
                
                <Typography gutterBottom>
                    <strong>Listado de resultados </strong>
                </Typography>
                <Typography variant="body1">
                    Tabla de estadísticas de los jugadores
                </Typography>
                <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ marginTop: 4, backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: 3, borderRadius: 2 }} >
                    <StatsOfMatchPlayers data={data} />
                </Grid>
                

            </Container>

            
        </Box>
            
        
    );
}