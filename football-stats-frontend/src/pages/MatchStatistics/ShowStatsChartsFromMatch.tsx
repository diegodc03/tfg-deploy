

import { Box, Button, Container, Grid, Typography } from '@mui/material';
import  { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import GenericSelectProps from '../../components/MultipleSelect';
import { TablesStats } from '../../model/tablesStats/TablesStats';
import SpecificStatsOfMatchPlayers from '../../components/SpecificStatsOfMatchPlayers';
import { BasicPositionAPI } from '../../model/BasicPositionAPI';
import { API_ENDPOINTS } from '../../model/constants/UrlConstants';
import ErrorSnackbar from '../../components/showError';
import { ERROR_MESSAGES } from '../../model/constants/errorConstants';
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



export default function ShowStatsFromMatch() {


    const {match_id} = useParams();
    const [isLoading, setIsLoading] = useState(true);
    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);


    const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
    const [selectedFiltersTable, setSelectedFilterTable] = useState<string>('');
    
    const [basicPositions, setBasicPositions] = useState<BasicPositionAPI[]>([]);
    const [basicPositionElement, setBasicPositionElement] = useState<string>('');
     
    const [stats, setStats] = useState<any[]>([]); // Aquí se guardarán los datos de las estadísticas de los jugadores

    const dictOfTables: string = "&type_table_stats=";
    const typeOfBasicPosition: string = "&basic_position="; // This can be dynamic based on user selection or other logic

    let baseurl: string = API_ENDPOINTS.STATS_PLAYERS_MATCH_TO_CHART + `${match_id}`;

    useEffect(() => {
        const fetchData = async () => {
            try {

                const [responseStats, responseFilters, responseBasicPositions] = await Promise.all([
                    fetch(API_ENDPOINTS.STATS_PLAYERS_MATCH_TO_CHART + `${match_id}`),
                    fetch(API_ENDPOINTS.FILTER_STATS_MODIFIED),
                    fetch(API_ENDPOINTS.ALL_BASIC_POSITIONS),
                ]);

                if (!responseStats.ok || !responseFilters.ok || !responseBasicPositions.ok) {
                    throw new Error('Error fetching data');
                }

                const [statsData, filtersData, filtersBasicPositions] = await Promise.all([
                    responseStats.json(),
                    responseFilters.json(),
                    responseBasicPositions.json()
                ]);


                const filtersArrayTransform: TablesStats[] = Object.entries(filtersData).map(([key, value]) => ({
                    categoryName: key,
                    categoryDescription: String(value),
                }));

                setStats(statsData);
                setFiltersArray(filtersArrayTransform);
                setBasicPositions(filtersBasicPositions);
                setSelectedFilterTable(filtersArrayTransform[0]?.categoryName || ''); // Set default filter if available
                setIsLoading(false); 

            } catch (error) {
                setErrorMessage(ERROR_MESSAGES.NOT_FOUND_CHARTS_FROM_MATCH);
                setShowError(true);
                setIsLoading(false);
            }
    }
        fetchData();
    }, [match_id]);

    
    const handleChangeSelectedTableFilters = (value: string) => {
        setSelectedFilterTable(value);
    }

    const handleChangeSelectedBasicPosicionsFilters = (value: string) => {
        setBasicPositionElement(value);
    }

    const handleFilter = async () => {
        let newURL: string = baseurl;
        if (selectedFiltersTable !== "Todos") {
            newURL += dictOfTables + selectedFiltersTable;
        }

    
        if (basicPositionElement !== "Todos") {
            newURL += typeOfBasicPosition + basicPositionElement;
        }

        const response = await fetch(newURL);
        if (!response.ok) {
            throw new Error('Error fetching filtered stats');
        }

        setIsLoading(true);
        const data = await response.json();
        setStats(data);
        setIsLoading(false);
    }


    return (

        <Container maxWidth="lg" sx={{ marginTop: '3rem', marginBottom: '5vh' }}>
            
            <ErrorSnackbar
                open={showError}
                onClose={() => setShowError(false)}
                message={errorMessage ?? "Ha ocurrido un error inesperado"}
                position={{ vertical: 'top', horizontal: 'right' }}
                large={true}
            />

            <LoadingIndicator isLoading={isLoading} />


            <Box
                sx={{
                    backgroundColor: '#f8f9fa',
                    borderRadius: 4,
                    boxShadow: 2,
                    overflow: 'hidden',
                    marginBottom: 5,
                    
                }}
            >
                <Box
                    sx={{
                        backgroundColor: '#ffffff',
                        padding: 2,
                        paddingBottom:0,
                        paddingLeft: 3,
                    }}
                >
                    <Typography>
                        <strong>Filtrar por tipo de estadística y equipo</strong>
                    </Typography>
                </Box>

            

                <Grid 
                    container
                    spacing={{ xs: 1, sm: 2, md: 4 }}
                    
                    justifyContent="center"
                    sx={{
                        backgroundColor: '#f8f9fa',
                        padding: 2,
                        borderRadius: 4,
                    }}
                >
                    <Grid  size={{xs:12, md:5}}>
                        <Typography>
                            <strong>Tablas a consultar</strong>
                        </Typography>
                        <div>
                            
                            <GenericSelectProps<TablesStats>
                                items={filtersArray}
                                value={selectedFiltersTable || ""}
                                onChange={handleChangeSelectedTableFilters}
                                getId={(item) => item.categoryName}
                                getLabel={(item) => item.categoryDescription}
                            />
                        </div>
                    </Grid>
        
                    <Grid  size={{xs:12, md:5}}>
                        <Typography>
                            <strong>Tipos de posiciones</strong>
                        </Typography>
                        <div>  
                            <GenericSelectProps<BasicPositionAPI>
                            items={basicPositions}
                            value={basicPositionElement || ""}
                            onChange={handleChangeSelectedBasicPosicionsFilters}
                            getId={(item) => String(item.category_id)}
                            getLabel={(item) => item.category_name}
                        />
                        </div>
                    </Grid>
                
                        <Grid size={{xs:12,md:2}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                            <Button
                                    variant="contained"
                                    color="primary"
                                    fullWidth
                                    onClick={handleFilter}
                                >
                                Filtrar
                            </Button>
                        </Grid>    
                    </Grid>
                </Box>
            

            <Box
                sx={{
                    backgroundColor: 'rgba(255, 255, 255, 0.7)',
                    borderRadius: 4,
                    boxShadow: 2,
                    overflow: 'hidden',
                }}
            >
                <Box
                    sx={{
                        padding: 2,
                        paddingBottom:0,
                        paddingLeft: 3,
                    }}
                >
                    <Typography gutterBottom>
                        <strong>Listado de resultados </strong>
                    </Typography>
                    <Typography variant="body1">
                        Tabla de estadísticas de los jugadores por tipos
                    </Typography>
                </Box>
            
                <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ padding: 3, borderRadius: 4 }} >
                    <SpecificStatsOfMatchPlayers data={stats} />
                </Grid>
            </Box>
            

        </Container>
    );
}