

/**
 * Este archivo va a encargar de comparar las estadísticas de cada temporada
 * 
 * Se tiene una lista de estadísticas totales por temporada, y se va a comparar cada una de ellas
 * 
 * Tambien se va a comparar por temporada  y posiciones, es decir, se va a comparar cada una de las estadísticas de cada jugador por su posición
 * 
 * Tambien se va a comparar por equipo, es decir, se va a comparar las estadísticas de un jugador por su equipo
 */


import { Button, Container, Grid, Stack, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import LoadingIndicator from "../../components/LoaqdingIndicator";
import { StatAPI } from "../../model/StatsAPI/StatsAPI";
import StatsTables from "../../components/StatsTables";
import { API_ENDPOINTS} from '../../model/constants/UrlConstants';
import { ChartOfNumbersOfScores } from "../../components/charts/chartOfNumbers";
import { ChartAPI } from "../../model/ChartsAPI/ChartAPI";
import { TablesStats } from "../../model/tablesStats/TablesStats";
import GenericSelectProps from '../../components/MultipleSelect';
import { ChartType, StatEntry } from "../../model/statsTypes/stats";
import { ReusableChart1 } from "../../components/charts/reusableChart1";
import { generateScoreValuesChart } from "./utilsComparison";


export default function ShowStatsComparisonFromLeague() {

    
    const chartType: ChartType = 'bar';
    const [chartData, setChartData] = useState<ChartAPI[]>([]);

    const [isLoading, setIsLoading] = useState(true);
    const [data, setData] = useState<StatAPI[]>([]); 
    
    const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
    const [filterColumnsTable, setFilterColumnsTable] = useState<string[]>([]);

    const [selectedFiltersTable, setSelectedFiltersTable] = useState<string | null>(null);
    const [selectedTypePlayer, setSelectedTypePlayer] = useState<string | null>(null);
    const [selectColumn, setSelectedColumn] = useState<string | null>(null);

    const typePlayersFilter: TablesStats[] = [
        { categoryName: "substitute", categoryDescription: "Suplentes" },
        { categoryName: "starter", categoryDescription: "Titulares" },
    ]

    useEffect(() => {

        const fetchData = async () => {
            try {
                const [responseData, responseChartAPI, filterTables, columns_tables] = await Promise.all([
                    fetch(API_ENDPOINTS.LEAGUES_STATS),
                    fetch(API_ENDPOINTS.LEAGUE_CHART),
                    fetch(API_ENDPOINTS.FILTER_STATS_MODIFIED),
                    fetch(API_ENDPOINTS.FILTER_COLUMNS),
                ]);
                
                console.log(API_ENDPOINTS.LEAGUES_STATS);
                console.log(API_ENDPOINTS.LEAGUE_CHART);
                console.log(API_ENDPOINTS.FILTER_STATS_MODIFIED);
                console.log(API_ENDPOINTS.FILTER_COLUMNS);

                if (!responseData.ok || !responseChartAPI.ok || !filterTables.ok || !columns_tables.ok) {
                    throw new Error('Error fetching data');
                }
                
                const [data, chartData, filterDataTables, filter_columns_table] = await Promise.all([
                    responseData.json(),
                    responseChartAPI.json(),
                    filterTables.json(),
                    columns_tables.json(),
                ]);
                setChartData(chartData);
                setData(data);;
                setFilterColumnsTable(filter_columns_table);

                const filtersArrayTransform: TablesStats[] = Object.entries(filterDataTables).map(([key, value]) => ({
                    categoryName: key,
                    categoryDescription: String(value),
                    }));
                
                setFiltersArray(filtersArrayTransform);

            } catch (error) {
                console.error('Error fetching data:', error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();

    }, []);


    const handleChangeSelectedTableFilters = (value: string) => {
        setSelectedFiltersTable(value);
    };

    const handleChangeSelectedTypePlayer = (value: string) => {
        setSelectedTypePlayer(value);
    }
   
    const { labels: chartLabels, scores: chartScores } = React.useMemo(() => {
        const labels = chartData.map(player => `${player.league_year} - ${player.starter_status}`);
        const scores = chartData.map(player => player.value);
        return { labels, scores };
    }, [chartData]);


    const handleFilter = async () => {

        console.log("Selected Filters Table:", selectedFiltersTable);

        let newURLStats: string = API_ENDPOINTS.LEAGUES_STATS;
        let newURLChart: string = API_ENDPOINTS.LEAGUE_CHART;

        if (selectedFiltersTable && selectedFiltersTable !== "Todos") {
            newURLStats += `?type_of_stats=${selectedFiltersTable}`;
        }

        try {
            const response = await fetch(newURLStats);
            if (!response.ok) {
                throw new Error('Error fetching filtered data');
            }
            const filteredData = await response.json();

            if (selectedTypePlayer && selectedTypePlayer !== "Todos") {
                const typeFilteredData = filteredData.filter(player => player.starter_status === selectedTypePlayer);

                const chartResponse = chartData.filter(player => player.starter_status === selectedTypePlayer);
                setChartData(chartResponse);
                setData(typeFilteredData);
            } else {
                setData(filteredData);
            }
        } catch (error) {
            console.error('Error fetching filtered data:', error);
        }
    }

    const handleChangeColumn = (value: string) => {
        setSelectedColumn(value);
    }


    const handleChangeColumnElection = async () => {
        if (selectColumn) {
            
            let newURL: string = API_ENDPOINTS.LEAGUE_CHART + `?type_of_stats=${selectColumn}`;
            
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
                    <strong>Filtrar Si ha jugado mas de 70 min</strong>
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
                            <strong>Rendimiento del Jugador suplente y titular</strong>
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

                    {/** Aqui faltaría meter tipo de jugador básico */}
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
                
                
                <Typography gutterBottom>
                    <strong>Listado de resultados </strong>
                </Typography>
                <Typography variant="body1">
                    Tabla de estadísticas los equipos segun la temporada
                </Typography>
                <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ marginTop: 4, backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: 3, borderRadius: 2 }} >
                    <StatsTables data={data} />
                </Grid>

                <Typography gutterBottom sx={{ marginTop: 6, fontWeight: 'bold', color: 'black' }}>
                    <strong>Estadísticas disponibles de la liga</strong>
                </Typography>


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
                        <Typography>
                            Estadísticas que se muestra una unica estadística para cada Liga
                        </Typography>
                        <Stack sx={{ marginTop: 6, backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
                            <ReusableChart1 stat={generateScoreValuesChart(chartData, selectColumn)} typeOfChart={'bar'} typeOfChartColor="other"/>
                        </Stack>
                    </Grid>
                </Grid>
            </Container>
    );

}

