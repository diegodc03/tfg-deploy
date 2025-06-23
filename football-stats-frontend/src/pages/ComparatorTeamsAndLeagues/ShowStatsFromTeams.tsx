








import { Button, Container, Grid, Stack, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import GenericSelectProps from '../../components/MultipleSelect';
import { TablesStats } from '../../model/tablesStats/TablesStats';
import { API_ENDPOINTS} from '../../model/constants/UrlConstants';
import { ChartAPI } from '../../model/ChartsAPI/ChartAPI';
import { StatAPI } from '../../model/StatsAPI/StatsAPI';
import { ChartOfNumbersOfScores } from '../../components/charts/chartOfNumbers';
import StatsTables from '../../components/StatsTables';
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



export default function ShowStatsFromTeams() {


    const {league_id} = useParams();
    const [isLoading, setIsLoading] = useState(true);


    const [chartData, setChartData] = useState<ChartAPI[]>([]);
    const [data, setData] = useState<StatAPI[]>([]); 

    const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
    const [filterColumnsTable, setFilterColumnsTable] = useState<string[]>([]);

    const [teamsArray, setTeamsArray] = useState<TablesStats[]>([]);
    const [selectedTeam, setSelectedTeam] = useState<string | null>(null);
    const navigate = useNavigate();

    const [selectedFiltersTable, setSelectedFiltersTable] = useState<string | null>(null);
    const [selectedTypePlayer, setSelectedTypePlayer] = useState<string | null>(null);

    let [beforeSelectedTablesFilter, setBeforeSelectedTablesFilter] = useState<string | null>(null);
    let [beforeSelectedTeamFilter, setBeforeSelectedTeamFilter] = useState<string | null>(null);
    let [beforeSelectedTypePlayerFilter, setBeforeSelectedTypePlayerFilter] = useState<string | null>(null);
    
    const [selectColumn, setSelectedColumn] = useState<string | null>(null);

    const typePlayersFilter: TablesStats[] = [
        { categoryName: "substitute", categoryDescription: "Suplentes" },
        { categoryName: "starter", categoryDescription: "Titulares" },
    ]


    useEffect(() => {
        const fetchData = async () => {
            try {

                const [playersStatsResponse, filterTablesResponse, chartResponse, columns_tables, filterTeamsResponse] = await Promise.all([
                    fetch(API_ENDPOINTS.TEAM_STATS),
                    fetch(API_ENDPOINTS.FILTER_STATS_MODIFIED),
                    fetch(API_ENDPOINTS.TEAM_CHART ),
                    fetch(API_ENDPOINTS.FILTER_COLUMNS),
                    fetch(API_ENDPOINTS.FILTER_TEAMS + `?league_id=${league_id}`),

                ]);

                console.log(API_ENDPOINTS.FILTER_TEAMS + `?league_id=${league_id}`);

                if (!playersStatsResponse.ok || !filterTablesResponse.ok || !chartResponse.ok || !columns_tables.ok || !filterTeamsResponse.ok) {
                    throw new Error('Error fetching data');
                }

                const [playersStatsData, filterTablesData, chartData, filter_columns_table, filterTeamsData] = await Promise.all([
                    playersStatsResponse.json(),
                    filterTablesResponse.json(),
                    chartResponse.json(),
                    columns_tables.json(),
                    filterTeamsResponse.json(),
                ]);

                
                const filtersArrayTransform: TablesStats[] = Object.entries(filterTablesData).map(([key, value]) => ({
                    categoryName: key,
                    categoryDescription: String(value),
                }));

                const filterTeamsDataTransform: TablesStats[] = Object.entries(filterTeamsData).map(([key, value]) => ({
                    categoryName: key,
                    categoryDescription: String(value),
                }));
                
                console.log(playersStatsData);

                setTeamsArray(filterTeamsDataTransform);
                setFiltersArray(filtersArrayTransform)
                setData(playersStatsData);
                setChartData(chartData);
                setFilterColumnsTable(filter_columns_table);
                
            } catch (error) {
                console.error('Error fetching player stats:', error);
            } finally {
                setIsLoading(false);
            }
        
    }
        console.log('League ID:', league_id);
        fetchData();
    }, [league_id]);

    const { labels: chartLabels, scores: chartScores } = React.useMemo(() => {
            const labels = chartData.map(player => `${player.league_year} - ${player.starter_status}`);
            const scores = chartData.map(player => player.value);
            return { labels, scores };
        }, [chartData]);

    const handleChangeSelectedTableFilters = (value: string) => {
        setSelectedFiltersTable(value);
    };

    const handleChangeSelectedTypePlayer = (value: string) => {
        setSelectedTypePlayer(value);
    }

    const handleChangeFilterTeam = (value: string) => {
        setSelectedTeam(value);
    }
    
    const handleFilter = async () => {
        let newURL: string = API_ENDPOINTS.TEAM_STATS;

        if ((selectedFiltersTable != beforeSelectedTablesFilter || beforeSelectedTypePlayerFilter != selectedTypePlayer) && selectedFiltersTable !== null) {
            console.log('Selected Filters Table:', selectedFiltersTable);
            //beforeSelectedTablesFilter = selectedFiltersTable;
            setBeforeSelectedTablesFilter(selectedFiltersTable);
            newURL += `?type_of_stats=${selectedFiltersTable}`;
        }

        if ((selectedTeam != beforeSelectedTeamFilter || beforeSelectedTypePlayerFilter != selectedTypePlayer) &&  selectedTeam !== null) {
            //beforeSelectedTeamFilter = selectedTeam; 
            setBeforeSelectedTeamFilter(selectedTeam);  
            if (newURL.includes('?')) {
                newURL += `&team_name=${selectedTeam}`;
            } else {
                newURL += `?team_name=${selectedTeam}`;
            }
        }

    
        try {
            const response = await fetch(newURL);
            if (!response.ok) {
                throw new Error('Error fetching filtered data');
            }
            const filteredData = await response.json();

            if (selectedTypePlayer && selectedTypePlayer !== "Todos") {
                const typeFilteredData = filteredData.filter(player => player.starter_status === selectedTypePlayer);
                setData(typeFilteredData);
            } else {
                setData(filteredData);
            }

            handleChangeChart(selectedTeam, selectedFiltersTable);

        } catch (error) {
            console.error('Error fetching filtered data:', error);
        }
    }
    
    const handleChangeChart = async (teamName: string, selectedFiltersTable: string | null) => {
        
        if (selectedFiltersTable){

            const chartColumns = await fetch(API_ENDPOINTS.FILTER_COLUMNS + `?table=${selectedFiltersTable}`);
            
            if (!chartColumns.ok) {
                throw new Error('Error fetching filter columns');
            }

            const filterColumnsData = await chartColumns.json();
            setFilterColumnsTable(filterColumnsData);

            const firstStat = String(filterColumnsData[0] ?? "");

            console.log('First Stat:', firstStat);
            let newURL: string = API_ENDPOINTS.TEAM_CHART + `?team_name=${teamName}&type_of_stats=${firstStat}`;
            try {
                const chartResponse = await fetch(newURL);
                if (!chartResponse.ok) {
                    throw new Error('Error fetching filtered data');
                }
                const filteredChartData = await chartResponse.json();
                setChartData(filteredChartData);
            } catch (error) {
                console.error('Error fetching filtered data:', error);
            }

        }
        
        
    }

    const handleChangeColumn = (value: string) => {
        setSelectedColumn(value);
    }

    const handleChangeColumnElection = async () => {
        if (selectColumn) {
            
            let newURL: string = API_ENDPOINTS.TEAM_CHART + `?type_of_stats=${selectColumn}&team_name=${selectedTeam}`;
            
            try {
                const response = await fetch(newURL);
                if (!response.ok) {
                    throw new Error('Error fetching filtered data');
                }
                const filteredData = await response.json();                
                setChartData(filteredData);
            
            } catch (error) {
            console.error('Error fetching filtered data:', error);
            }
        }
    }



    return (
       
        <Container maxWidth="lg" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>
            <LoadingIndicator isLoading={isLoading} />
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


                <Grid  size={{xs:12, md:3}}>
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

                <Grid  size={{xs:12, md:4}}>
                    <Typography>
                        <strong>Rendimiento: Suplente o Titular</strong>
                    </Typography>
                    <div>
                        <GenericSelectProps<TablesStats>
                            items={typePlayersFilter}
                            value={selectedTypePlayer || ""}
                            onChange={handleChangeSelectedTypePlayer}
                            getId={(item) => item.categoryName}
                            getLabel={(item) => item.categoryDescription}
                        />
                    </div>
                </Grid>

                <Grid  size={{xs:12, md:4}}>
                    <Typography>
                        <strong>Equipo a consultar de la liga</strong>
                    </Typography>
                    <div>    
                        <GenericSelectProps<TablesStats>
                            items={teamsArray}
                            value={selectedTeam || ""}
                            onChange={handleChangeFilterTeam}
                            getId={(item) => item.categoryDescription}
                            getLabel={(item) => item.categoryDescription}
                        />
                    </div>
                </Grid>

                <Grid size={{xs:12,md:1}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
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
            
            
            <Typography gutterBottom>
                <strong>Listado de resultados </strong>
            </Typography>
            <Typography variant="body1">
                Tabla de estadísticas los equipos segun la temporada
            </Typography>
            <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ marginTop: 4, backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: 3, borderRadius: 2 }} >
                <StatsTables data={data} />
            </Grid>

            <Grid
                container
                spacing={2}
                sx={{
                    backgroundColor: 'rgba(255, 255, 255, 0.9)',
                    borderRadius: 2,
                    padding: 3,
                    marginTop: 4
                }}
            >
                
                    <Grid size={{ xs: 12, md: 3 }}>
                        <Grid  size={{xs:12, md:12}}>
                            <Typography>
                                Filtro de Posición a elegir
                            </Typography>
                            <div>
                                <GenericSelectProps<string[]>
                                    items={filterColumnsTable}
                                    value={String(selectColumn) || ""}
                                    onChange={handleChangeColumn}
                                    getId={(item) => String(item)}
                                    getLabel={(item) => String(item)}
                                />
                            </div>
                        </Grid>
                        <Grid size={{xs:12, sm:6, md:6}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                            <Button
                                variant="contained"
                                color="primary"
                                fullWidth
                                sx={{ width: '100%' }}
                                onClick={() => handleChangeColumnElection()}
                            >
                                Filtros
                            </Button>
                        </Grid>
                        
                    </Grid>

                    <Grid size={{ xs: 12, md: 9 }}>
                        <Typography variant="body1">
                                Tabla de estadísticas los equipos segun la temporada
                            </Typography>
                        <Stack sx={{ marginTop: 6, backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
                            <ChartOfNumbersOfScores stat={chartScores} typeOfChart={'bar'} labels={chartLabels}/>
                        </Stack>
                    </Grid>
                </Grid>
        </Container>
    );
}