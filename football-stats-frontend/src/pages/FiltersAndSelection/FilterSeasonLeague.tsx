

import { Typography, Grid, Button, Container, Box} from '@mui/material';


import {useEffect, useState} from 'react';

import { useNavigate } from 'react-router-dom';
import {LeagueAPI} from '../../model/LeagueAPI';
import {Season} from '../../model/SeaonAPI';
import {Tournament} from '../../model/TournamentAPI';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import CardShowOptions from '../../components/CardShowOptions';
import SeasonSelect from '../../components/filters/SeasonFilters';

import { ERROR_MESSAGES } from '../../model/constants/errorConstants';
import ErrorSnackbar from '../../components/showError';
import { STORAGE_KEYS } from '../../model/constants/StorageKeys';
import FiltersElements from '../../components/filters/filter';




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
    const getStoredData = () => {
        try {
            const seasonsData = JSON.parse(localStorage.getItem(STORAGE_KEYS.seasons) || '[]');
            const leaguesData = JSON.parse(localStorage.getItem(STORAGE_KEYS.leagues) || '[]');
            const tournamentsData = JSON.parse(localStorage.getItem(STORAGE_KEYS.season_tournaments) || '[]');

            if (!Array.isArray(seasonsData) || !Array.isArray(leaguesData) || !Array.isArray(tournamentsData)) {
                throw new Error("Datos corruptos en localStorage");
            }

            setSeasons(seasonsData);
            setLeagues(leaguesData);
            setTournaments(tournamentsData);
            setFilteredResults(tournamentsData);
            setIsLoading(false);
        } catch (error: any) {
            setErrorMessage(ERROR_MESSAGES.NOT_FOUND_LEAGUES);
            setShowError(true);
            setIsLoading(false);
        }
    };

    getStoredData();
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
                    <Typography >
                        <strong>Filtrar por temporada y liga</strong>
                    </Typography>
                </Box>

                <Grid
                    container
                    spacing={{ xs: 1, sm: 2, md: 3 }}
                    justifyContent="center"
                    sx={{ padding: 3, borderBottom: '3px solid #ddd' }}
                >
                    <Grid size={{ xs: 12, md: 5 }}>
                        <Typography>
                            <strong>Liga</strong>
                        </Typography>
                        <FiltersElements
                            itemsToSelect={leagues.map(l => l.name)}
                            selectedValue={leagueElement || ''}
                            onChange={handleChangeLeague}
                        />
                    </Grid>

                    <Grid size={{ xs: 12, md: 5 }}>
                        <SeasonSelect
                            seasons={seasons}
                            value={seasonElement || ''}
                            onChange={handleChangeSeason}
                        />
                    </Grid>

                    <Grid
                        size={{ xs: 12, sm: 6, md: 2 }}
                        sx={{
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            mt: { xs: 2, md: 3 },
                        }}
                    >
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
            </Box>
   
            
            <Box
                sx={{
                    backgroundColor: 'rgba(255, 255, 255, 0.85)',
                    borderRadius: 4,
                    boxShadow: 2,
                    overflow: 'hidden',
                    marginBottom: 5,
                }}
            >
                <Box
                    sx={{
                        backgroundColor: 'rgba(255, 255, 255, 0.6)',
                        padding: 2,
                        paddingBottom:0,
                        paddingLeft: 3,
                    }}
                >
                    <Typography gutterBottom>
                        <strong>Listado de resultados </strong>
                    </Typography>
                </Box>

                <Grid
                    container 
                    spacing={2} 
                    justifyContent="center" 
                    alignItems="center" 
                    sx={{ 
                        padding: 3, 
                        borderRadius: 4
                    }} 
                >
                    
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
            </Box>

        </Container>

    );
}

export default FilterSeasonLeague;