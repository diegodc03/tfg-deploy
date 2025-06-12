import { Box, Button, Container, Grid, Stack, Typography } from "@mui/material";

import realMadridImg from '../images/real_madrid.jpg';
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { LeagueAPI } from "../model/LeagueAPI";
import GenericSelectProps from "../components/MultipleSelect";
import { Season } from "../model/SeaonAPI";
import { ScoreAPI } from "../model/ScoreAPI";
import EnhancedTable from "../components/TablePlayersScore";

import { SpecificPositionAPI } from "../model/SpecificPositionAPI";
import { BasicPositionAPI } from "../model/BasicPositionAPI";
import { GameModeTypeAPI } from "../model/GameModeTypeAPI";

import { FootballField } from "../components/FootballField";

import { ChartOfNumbersOfScores } from "../components/charts/chartOfNumbers";
import { PlayersIdName } from "../model/PlayersIdName";
import { MatchPlayerScore } from "../model/ShowMatchPlayerScore";



export default function ShowScores() {

  
    const { match_id } = useParams();

  

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


    const navigate = useNavigate();

    
    const baseUrlPlayerScore: string = "http://localhost:8000/api/stats/get-stats-score-filtered-player/"
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
                const [gameTypesResponse, basicPositionsResponse, specificPositionsResponse, players_scores, playersFilter] = await Promise.all([
                    fetch('http://localhost:8000/api/all-game-modes/'),
                    fetch('http://localhost:8000/api/all-basic-positions/'),
                    fetch('http://localhost:8000/api/all-specifics-positions/'),
                    fetch(`http://localhost:8000/api/scores-of-players-match/?match_id=${match_id}`),
                    fetch(`http://localhost:8000/api/players-by-match/?match_id=${match_id}`)
                ]);
                if (!gameTypesResponse.ok || !basicPositionsResponse.ok || !specificPositionsResponse.ok || !players_scores.ok || !playersFilter.ok) {
                    throw new Error('Error fetching data');
                }
                
                const gameTypesData = await gameTypesResponse.json();
                const basicPositionsData = await basicPositionsResponse.json();
                const specificPositionsData = await specificPositionsResponse.json();
                const players_scoresData = await players_scores.json();
                const playersFilterData = await playersFilter.json();

                setGameTypes(gameTypesData);
                setBasicPositions(basicPositionsData);
                setSpecificPositions(specificPositionsData);
                setPlayersScores(players_scoresData);
                setPlayersScoresFiltered(players_scoresData); // Initialize filteredMatches with all matches
                setPlayersFilter(playersFilterData);

                console.log('Datos de los jugadores:', players_scoresData);

            } catch (error) {
                console.error('Error fetching data:', error);
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
        console.log('Datos de las puntuaciones del jugador:', data);
    }
    
    let players_labels: string[] = [];
    const labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
    const generateValuesStats = (players_scores_filtered) => {

        const bins = new Array(11).fill(0);
        
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

        return values;
    };


    // Yo aqui paso un elemtnto
    const generateScoreValuesChart = (players_scores_filtered: MatchPlayerScore[]) => {
        

        players_labels = [];
        let values: number[] = [];
        
        for (let i = 0; i < players_scores_filtered.length; i++) {
            const score = players_scores_filtered[i].score;
            if (typeof score !== 'number' || score < 0 || score > 10) {
                console.error(`Invalid score at index ${i}: ${score}`);
                continue; 
            }
            else {

                console.log(`Valid score at index ${i}: ${score}`);
                values.push(score);
                players_labels.push(players_scores_filtered[i].game_mode_id.game_mode_name);
            }
        }

        console.log('Labels de los jugadores:', players_labels);
        console.log('Valores de las puntuaciones:', values);
        return values;
    }




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
            <Container maxWidth="lg" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>

                <Typography>
                    <strong>Filtrar por Tipo de juego, posiciones basicas y posiciones específicas</strong>
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
                            <strong>Formas de juego</strong>
                        </Typography>
                        <div>
                            <GenericSelectProps<GameModeTypeAPI>
                                items={gameTypes}
                                value={gameTypeElement || ""}
                                onChange={handleChangeGameType}
                                getId={(item) => item.game_mode_name}
                                getLabel={(item) => item.game_mode_name}
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
                                getLabel={(item) => item.category_name}
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
                                getLabel={(item) => item.specific_position_name}
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

                <EnhancedTable 
                    rows={players_scores_filtered}
                />

                <Typography>
                    <strong>Gráficas interesantes </strong>
                </Typography>
                <Stack  sx={{marginTop: 6,  backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
                    <ChartOfNumbersOfScores stat={generateValuesStats(players_scores_filtered)} typeOfChart={'bar'} labels={labels}/>
                </Stack>

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
                                Filtro de jugadores a elegir
                            </Typography>
                            <div>
                                <GenericSelectProps<PlayersIdName>
                                    items={playersFilter}
                                    value={String(selectedPlayerId) || ""}
                                    onChange={handleChangePlayer}
                                    getId={(item) => String(item.player_id)}
                                    getLabel={(item) => item.name}
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
                                Filtros
                            </Button>
                        </Grid>
                        
                    </Grid>

                    <Grid size={{ xs: 12, md: 9 }}>
                        <Typography>
                            Aquí se pueden añadir más gráficas si se desea. La intención es hacer un menú para elegir jugadores. El jugador se le van a mostrar las puntuaciones según el tipo de juego que pide el entrenador.
                        </Typography>
                        <Stack sx={{ marginTop: 6, backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
                            <ChartOfNumbersOfScores stat={generateScoreValuesChart(playerScores)} typeOfChart={'bar'} labels={players_labels}/>
                        </Stack>


                    </Grid>
                </Grid>
            </Container>
        </Box> 
                
    );
}