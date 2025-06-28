

import { Typography, Grid, Button, Container} from '@mui/material';


import {useEffect, useState} from 'react';

import { useNavigate } from 'react-router-dom';
import {LeagueAPI} from '../../model/LeagueAPI';
import {Season} from '../../model/SeaonAPI';
import {Tournament} from '../../model/TournamentAPI';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import LeagueSelect from '../../components/filters/LeagueFilters';
import CardShowOptions from '../../components/CardShowOptions';
import SeasonSelect from '../../components/filters/SeasonFilters';
import { API_ENDPOINTS } from '../../model/constants/UrlConstants';
import { ERROR_MESSAGES } from '../../model/constants/errorConstants';
import ErrorSnackbar from '../../components/showError';





const FilterSeasonLeague = () => {

    const [isLoading, setIsLoading] = useState(true);
    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

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
                    fetch(API_ENDPOINTS.ALL_SEASONS),
                    fetch(API_ENDPOINTS.ALL_LEAGUES),
                    fetch(API_ENDPOINTS.ALL_SEASON_TOURNAMENTS)
                ]);  
                   
                
                if (!seasonsResponse.ok || !leaguesResponse.ok || !tournamentsResponse.ok) {
                    throw new Error(ERROR_MESSAGES.NOT_FOUND_LEAGUES);
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

            } catch (error: any) {
                setErrorMessage(ERROR_MESSAGES.NOT_FOUND_LEAGUES);
                setShowError(true);
                setIsLoading(false); 
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

        <Container maxWidth="lg" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>
            <ErrorSnackbar
                open={showError}
                onClose={() => setShowError(false)}
                message={errorMessage ?? "Ha ocurrido un error inesperado"}
                position={{ vertical: 'top', horizontal: 'right' }}
                large={true}
            />


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
                    <LeagueSelect
                        leagues={leagues}
                        value={leagueElement || ''}
                        onChange={handleChangeLeague}
                    />
                </Grid>
                
                <Grid  size={{xs:12, md:5}}>
                    <SeasonSelect
                        seasons={seasons}
                        value={seasonElement || ''}
                        onChange={handleChangeSeason}
                    />
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
            
            <Grid
                container 
                spacing={2} 
                justifyContent="center" 
                alignItems="center" 
                sx={{ 
                    marginTop: 4, 
                    backgroundColor: 'rgba(255, 255, 255, 0.9)', 
                    padding: 3, 
                    borderRadius: 2 
                }} 
            >
                <LoadingIndicator isLoading={isLoading} />
                {
                filteredResults.map((item, index) => (
                    <Grid size={{ xs: 6, sm: 6, md: 3 }} sx={{ display: 'flex', justifyContent: 'center' }}  key={index} onClick={() => handleChangeLeagueView(item.tournament_id)} >
                        <CardShowOptions 
                            title={item.nombre_liga} 
                            season={item.season_tournament.season_year} 
                        /> 
                    </Grid>   
                                    ))
                }
            </Grid>



        </Container>

    );
}

export default FilterSeasonLeague;