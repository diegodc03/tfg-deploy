

import { Box, Typography, Grid, Button, Container} from '@mui/material';

import realMadridImg from '../images/real_madrid.jpg';
import CardShow from '../components/Cards';

import {useEffect, useState} from 'react';

import { useNavigate } from 'react-router-dom';
import {LeagueAPI} from '../model/LeagueAPI';
import GenericSelectProps from '../components/MultipleSelect';
import {Season} from '../model/SeaonAPI';

import {Tournament} from '../model/TournamentAPI';
import LoadingIndicator from '../components/LoaqdingIndicator';





const FilterSeasonLeague = () => {

    const [isLoading, setIsLoading] = useState(true);


    const [seasons, setSeasons] = useState<Season[]>([]);
    const [leagues, setLeagues] = useState<LeagueAPI[]>([]);
    const [tournaments, setTournaments] = useState<Tournament[]>([]);

    const navigate = useNavigate();

    const [seasonElement, setSeasonElement] = useState<string>('');
    const [leagueElement, setLeagueElement] = useState<string>('');
    const [filteredResults, setFilteredResults] = useState(tournaments);


    useEffect(() => {
        
        const fetchData = async () => {
            try {
                const [seasonsResponse, leaguesResponse, tournamentsResponse] = await Promise.all([
                    fetch('http://localhost:8000/api/all-seasons/'),
                    fetch('http://localhost:8000/api/all-leagues/'),
                    fetch('http://localhost:8000/api/season-tournaments/')
                ]);  
                   
                
                if (!seasonsResponse.ok || !leaguesResponse.ok || !tournamentsResponse.ok) {
                    throw new Error('Error fetching data');
                }

                const [seasonsData, leaguesData, tournamentsData] = await Promise.all([
                    seasonsResponse.json(),
                    leaguesResponse.json(),
                    tournamentsResponse.json()
                ]);

                setSeasons(seasonsData);
                setLeagues(leaguesData);
                setTournaments(tournamentsData);

                setFilteredResults(tournamentsData); 
                console.log(seasonsResponse, leaguesResponse, tournamentsResponse);
                setIsLoading(false);

            } catch (error) {
                console.error('Error fetching seasons:', error);
            }
        }

        fetchData();
        
      
    }, []);

    
    const handleChangeSeason = (value: string) => {
        setSeasonElement(value);
    };
    const handleChangeLeague = (value: string) => {
        setLeagueElement(value);
    };
    const handleChangeLeagueView = (tournamentId: number) => {
        navigate(`/filter-match/${tournamentId}`);
    };


    const filteredTournaments = () => {
        const filtered = tournaments.filter(tournament => {
            if (seasonElement && leagueElement) {
                return tournament.season_tournament.season_id === parseInt(seasonElement) && tournament.nombre_liga === leagueElement;
            } else if (seasonElement) {
                return tournament.season_tournament.season_id === parseInt(seasonElement);
            } else if (leagueElement) {
                return tournament.nombre_liga === leagueElement;
            }
            return true; // If no filters are applied, show all tournaments
        });
        setFilteredResults(filtered);
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
                
            }}>
                
            <LoadingIndicator isLoading={isLoading} />

            <Container maxWidth="lg" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>

                <Typography>
                    <strong>Filtrar por temporada y liga</strong>
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
                            <strong>Liga</strong>
                        </Typography>
                        <div>
                            
                            <GenericSelectProps<LeagueAPI>
                                items={leagues}
                                value={leagueElement || ""}
                                onChange={handleChangeLeague}
                                getId={(item) => item.name}
                                getLabel={(item) => item.name}
                            />
                        </div>
                    </Grid>
                    
                    <Grid  size={{xs:12, md:5}}>
                        <Typography>
                            <strong>Temporada</strong>
                        </Typography>
                        <div>
                            <GenericSelectProps<Season>
                                items={seasons}
                                value={seasonElement || ''}
                                onChange={handleChangeSeason}
                                getId={(item) => String(item.season_id)}
                                getLabel={(item) => item.season_year}
                            />
                        </div>
                    </Grid>

                    <Grid size={{xs:12,md:2}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                        <Button
                                variant="contained"
                                color="primary"
                                fullWidth
                                onClick={filteredTournaments}
                            >
                            Filtrar
                        </Button>
                    </Grid>
                </Grid>
                
                <Typography gutterBottom>
                    <strong>Listado de resultados </strong>
                </Typography>
                
                <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ marginTop: 4, backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: 3, borderRadius: 2 }} >
                    {
                    filteredResults.map((item, index) => (
                        <Grid size={{ xs: 6, sm: 6, md: 3 }} key={index} onClick={() => handleChangeLeagueView(item.tournament_id)} >
                            <CardShow title={item.nombre_liga} text={item.season_tournament.season_year} image={realMadridImg} /> 
                        </Grid>   
                                        ))
                    }
                </Grid>



            </Container>
        </Box>
    );
}

export default FilterSeasonLeague;