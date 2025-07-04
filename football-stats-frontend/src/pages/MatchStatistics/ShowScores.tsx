import { Box, Button, Container, Grid, Stack, Typography } from "@mui/material";


import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {StatEntry, ChartType} from "../../model/statsTypes/stats";
import GenericSelectProps from "../../components/MultipleSelect";

import { ScoreAPI } from "../../model/ScoreAPI";
import EnhancedTable from "../../components/TablePlayersScore";

import { SpecificPositionAPI } from "../../model/SpecificPositionAPI";
import { BasicPositionAPI } from "../../model/BasicPositionAPI";
import { GameModeTypeAPI } from "../../model/GameModeTypeAPI";

import { ChartOfNumbersOfScores } from "../../components/charts/chartOfNumbers";
import { PlayersIdName } from "../../model/PlayersIdName";
import { MatchPlayerScore } from "../../model/ShowMatchPlayerScore";

import { API_ENDPOINTS } from "../../model/constants/UrlConstants";
import { ReusableChart1 } from "../../components/charts/reusableChart1";
import ErrorSnackbar from "../../components/showError";
import { ERROR_MESSAGES } from "../../model/constants/errorConstants";
import { STORAGE_KEYS } from "../../model/constants/StorageKeys";
import LoadingIndicator from "../../components/LoaqdingIndicator";
import { positionTranslation, specificPositionTranslation, gameModeTranslation } from "../../model/constants/Translate";



export default function ShowScores() {

    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const { match_id } = useParams();
    const [isLoading, setIsLoading] = useState(true);


    const [gameTypes, setGameTypes] = useState<GameModeTypeAPI[]>([]);
    const [basicPositions, setBasicPositions] = useState<BasicPositionAPI[]>([]);
    const [specificPositions, setSpecificPositions] = useState<SpecificPositionAPI[]>([]);
    
    const [players_scores, setPlayersScores] = useState<ScoreAPI[]>([]);
    const [players_scores_filtered, setPlayersScoresFiltered] = useState<ScoreAPI[]>([]);


    const [gameTypeElement, setGameTypeElement] = useState<string>('');
    const [basicPositionElement, setBasicPositionElement] = useState<string>('');
    const [specificPositionElement, setSpecificPositionElement] = useState<string>('');
    
    const [playersFilter, setPlayersFilter] = useState<PlayersIdName[]>([]);
    const [selectedPlayerId, setSelectedPlayerId] = useState<string>();


    const [playerScores, setPlayerScores] = useState<MatchPlayerScore[]>([]);

    const chartType: ChartType = "bar"
    const navigate = useNavigate();

    
    //const baseUrlPlayerScore: string = "http://localhost:8000/api/stats/get-stats-score-filtered-player/"
    const baseUrlPlayerScore: string = API_ENDPOINTS.PLAYER_SCORE_FILTERED;
    const match_id_url: string = `?match_id=${match_id}`;
    const player_id_url: string = `&player_id=${selectedPlayerId}`;

    function handleChangeGameType(value: string): void {
        setGameTypeElement(value);
    }

    function handleHangeBasicPosition(value: string): void {
        setBasicPositionElement(value);
    }

    function handleChangeSpecificPosition(value: string): void {
        setSpecificPositionElement(value);
    }

    function handleChangePlayer(value: string): void {
        setSelectedPlayerId(value);
        
    }



    useEffect(() => {
        const fetchData = async () => {
            try {

                const gameTypesData = JSON.parse(localStorage.getItem(STORAGE_KEYS.gameModes) || '[]');
                const basicPositionsData = JSON.parse(localStorage.getItem(STORAGE_KEYS.basicPositions) || '[]');
                const specificPositionsData = JSON.parse(localStorage.getItem(STORAGE_KEYS.specificPositions) || '[]');
                const playersFiltersData= JSON.parse(localStorage.getItem(STORAGE_KEYS.playersByMatch(match_id)) || '[]');
                // Validación opcional: si alguno no está, lanza error
                if (!gameTypesData.length || !basicPositionsData.length || !specificPositionsData.length || !playersFiltersData.length) {
                    throw new Error('Missing cached data');
                }

                const [players_scores] = await Promise.all([
                    fetch(`${API_ENDPOINTS.ALL_SCORES_PLAYERS_MATCH}${match_id}`),
                ]);

                if (!players_scores.ok ) {
                    throw new Error('Error fetching data');
                }

                const players_scoresData = await players_scores.json();

                // Setear todo
                setGameTypes(gameTypesData);
                setBasicPositions(basicPositionsData);
                setSpecificPositions(specificPositionsData);
                setPlayersScores(players_scoresData);
                setPlayersScoresFiltered(players_scoresData);
                setPlayersFilter(playersFiltersData);
                //setSelectedPlayerId(playersFiltersData[0]?.player_id.toString() || '');


            } catch (error) {
                setErrorMessage(ERROR_MESSAGES.NOT_FOUND_SCORES_OF_PLAYERS);
                setShowError(true);
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();
    }, []);


    const filterScores = () => {
        const filteredMatches = players_scores.filter(scores => {
            
            const filters = []

            if (gameTypeElement) {
                filters.push(scores.game_mode_id.game_mode_name === gameTypeElement);
            }
            if (basicPositionElement) {
                filters.push(scores.basic_position_id.category_name === basicPositionElement);
            }
            if (specificPositionElement) {
                filters.push(scores.specific_position_id.specific_position_name === specificPositionElement);
            }

            return filters.every(Boolean); 
        }) 
        setPlayersScoresFiltered(filteredMatches);
    };


    const handleChangePlayerElection = async () => {

        let url = baseUrlPlayerScore + match_id_url + player_id_url;

        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Error fetching filtered stats');
        }
        
        const data = await response.json(); 
        setPlayerScores(data);
    }
    
    
    const generateValuesStats = (players_scores_filtered): StatEntry => {

        const bins = new Array(11).fill(0);
        const labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
        
        players_scores_filtered.forEach(element => {
           const value = element.score;

           if (typeof value === 'number' && value >= 0 && value <= 10) {
               const index = Math.floor(value);
               bins[index] += 1;
           }
        });

        let values:number[] = [];
        for (let i = 0; i < bins.length; i++) {
            values.push(bins[i]);
        }

        return {
            title: "Numero",
            labels: labels,
            data: values,
            type: chartType,
        };
    };


    const generateScoreValuesChart = (players_scores_filtered: MatchPlayerScore[]): StatEntry => {
        
        let players_labels: Set<string> = new Set();
        let data: number[] = [];
        
        for (let i = 0; i < players_scores_filtered.length; i++) {
            let score = players_scores_filtered[i].score;
            if (typeof score !== 'number') {
                console.error(`Invalid score at index ${i}: ${score}`);
                continue; 
            } else if (score < 0 || score > 10) {
                if (score < 0) {
                    score = 0; 
                } else {
                    score = 10; 
                }
            } 

            data.push(score);
            if (players_scores_filtered[i].game_mode_id.game_mode_name != "no_existencia") {
                players_labels.add(players_scores_filtered[i].game_mode_id.game_mode_name);
            }
        }

        if (data.length === 0) {
            console.error('No valid scores found in players_scores_filtered');
        }

        return {
            title: playersFilter.find(player => player.player_id === Number(selectedPlayerId))?.name || 'Jugador',
            labels: Array.from(players_labels),
            data,
            type: chartType,
        };
    }


    return (
        
            <Container maxWidth="lg" sx={{ marginTop: '3rem', marginBottom: '5vh' }}>
                <LoadingIndicator isLoading={isLoading} />
                <ErrorSnackbar
                    open={showError}
                    onClose={() => setShowError(false)}
                    message={errorMessage ?? "Ha ocurrido un error inesperado"}
                    position={{ vertical: 'top', horizontal: 'right' }}
                    large={true}
                />
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
                            <strong>Filtrar por Tipo de juego, posiciones basicas y posiciones específicas</strong>
                        </Typography>
                    </Box>

                    <Grid 
                        container
                        columnSpacing={{ xs: 1, sm: 2 }}
                        rowSpacing={{ xs: 1, sm: 2, md: 3 }}
                        spacing={{ xs: 1, sm: 2, md: 4 }}
                        
                        justifyContent="center"
                        sx={{
                            backgroundColor: '#f8f9fa',
                            padding: 2,
                            borderRadius: 4,
                        }}
                    >
                        <Grid  size={{xs:12, md:3}}>
                            <Typography>
                                <strong>Formas de juego</strong>
                            </Typography>
                            <div>
                                <GenericSelectProps<GameModeTypeAPI>
                                    items={gameTypes}
                                    value={gameTypeElement || ""}
                                    onChange={handleChangeGameType}
                                    getId={(item) => item.game_mode_name}
                                    getLabel={(item) => gameModeTranslation[item.game_mode_name] ?? item.game_mode_name}
                                />
                            </div>
                        </Grid>
                        <Grid  size={{xs:12, md:3}}>
                            <Typography>
                                <strong>Posiciones Básicas</strong>
                            </Typography>
                            <div>
                                
                                <GenericSelectProps<BasicPositionAPI>
                                    items={basicPositions}
                                    value={basicPositionElement || ""}
                                    onChange={handleHangeBasicPosition}
                                    getId={(item) => item.category_name}
                                    getLabel={(item) => positionTranslation[item.category_name] ?? item.category_name}
                                />
                            </div>
                        </Grid>
                        <Grid  size={{xs:12, md:3}}>
                            <Typography>
                                <strong>Posiciones Específicas</strong>
                            </Typography>
                            <div> 
                                <GenericSelectProps<SpecificPositionAPI>
                                    items={specificPositions}
                                    value={specificPositionElement || ""}
                                    onChange={handleChangeSpecificPosition}
                                    getId={(item) => item.specific_position_name}
                                    getLabel={(item) => specificPositionTranslation[item.specific_position_name] ?? item.specific_position_name}

                                />
                            </div>
                        </Grid>
                        <Grid size={{xs:12, sm:6, md:3}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                            <Button
                                variant="contained"
                                color="primary"
                                fullWidth
                                sx={{ width: '100%' }}
                                onClick={() => filterScores()}
                            >
                                Filtros
                            </Button>
                        </Grid>
                    </Grid> 
                </Box>


                <Box
                    sx={{
                        borderRadius: 4,
                        boxShadow: 2,
                        overflow: 'hidden',
                        marginBottom: 5,
                    }}
                >
                    <EnhancedTable 
                        rows={players_scores_filtered}
                    />
                </Box>
            
                <Box
                    sx={{
                        backgroundColor: 'rgba(255, 255, 255, 0.7)',
                        borderRadius: 4,
                        boxShadow: 2,
                        overflow: 'hidden',
                        marginBottom: 5
                    }}
                >
                    <Box
                        sx={{
                            padding: 2,
                            paddingBottom:0,
                            paddingLeft: 3,
                        }}
                    >
                        <Typography variant="h6" gutterBottom>
                            <strong>Gráficas </strong>
                        </Typography>
                    </Box>
                
                    <Stack   sx={{ padding: 3, borderRadius: 4, backgroundColor: 'rgba(255, 255, 255, 0.8)', alignItems:'center'}} >
                        <ReusableChart1 stat={generateValuesStats(players_scores_filtered)} typeOfChart={'bar'} typeOfChartColor="totalScores"/>
                    </Stack>
                </Box>
                
                <Grid
                    container
                    spacing={2}
                    sx={{
                        backgroundColor: 'rgba(255, 255, 255, 0.7)',
                        borderRadius: 4,
                        padding: 3,
           
                    }}
                >
                    <Grid size={{ xs: 12, md: 3 }}
                    >
                        <Grid  size={{xs:12, md:12}}>
                            <Typography>
                                <strong>Filtro de jugadores a elegir</strong>
                            </Typography>
                            <div>
                                <GenericSelectProps<PlayersIdName>
                                    items={playersFilter}
                                    value={String(selectedPlayerId) || ""}
                                    onChange={handleChangePlayer}
                                    getId={(item) => String(item.player_id)}
                                    getLabel={(item) => item.name}
                                    labelTodosShow={false}
                                />
                            </div>
                        </Grid>
                        <Grid size={{xs:12, sm:6, md:6}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                            <Button
                                variant="contained"
                                color="primary"
                                fullWidth
                                sx={{ width: '100%' }}
                                onClick={() => handleChangePlayerElection()}
                            >
                                Filtrar
                            </Button>
                        </Grid>
                    </Grid>

                    <Grid size={{ xs: 12, md: 9 }}>
                        <Typography>
                            <strong>Gráfica de puntuaciones del jugador seleccionado</strong>
                            <br />
                            { !selectedPlayerId ? 'Elija un jugador' : ''}    
                            
                        </Typography>
                        <Stack sx={{ marginTop: 3, backgroundColor: 'rgba(255, 255, 255, 0.8)', borderRadius: 4, alignItems: 'center', padding:5 }} >
                            <ReusableChart1 stat={generateScoreValuesChart(playerScores)} typeOfChart={'bar'} typeOfChartColor="gameModes"/>
                        </Stack>
                    </Grid>
                </Grid>
            </Container>
        
                
    );
}