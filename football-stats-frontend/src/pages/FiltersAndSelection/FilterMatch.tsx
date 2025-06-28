

import { Grid, Container, Typography, Button } from '@mui/material';
import {useEffect, useState} from 'react';
import { useNavigate, useParams } from 'react-router-dom';

import { MatchAPI } from '../../model/MatchAPI';
import LoadingIndicator from '../../components/LoaqdingIndicator';
import CardShowOptions from '../../components/CardShowOptions';
import { API_ENDPOINTS } from '../../model/constants/UrlConstants';
import FiltersElements from '../../components/filters/filter';
import { ERROR_MESSAGES } from '../../model/constants/errorConstants';
import ErrorSnackbar from '../../components/showError';

import { startTransition } from 'react';

export default function FilterMatch() {

    const navigate = useNavigate();
    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoadingFilters, setIsLoadingFilters] = useState(true);


    const { leagueId } = useParams();
    const [weeks, setWeeks] = useState<string[]>([]);
    const [teams, setTeams] = useState<string[]>([]);
    const [results, setResults] = useState<string[]>([]);
    const [matches, setMatches] = useState<MatchAPI[]>([]);

    const [selectedWeek, setSelectedWeek] = useState<string>();
    const [selectedTeam, setSelectedTeam] = useState<string>();
    const [selectedResult, setSelectedResult] = useState<string>();

    const [filteredMatches, setFilteredMatches] = useState<MatchAPI[]>(matches);

    const [isLoading, setIsLoading] = useState(true);

    

    useEffect(() => {
    const fetchAndPrepareMatches = async () => {
        try {
        const response = await fetch(API_ENDPOINTS.ALL_MATCHES_BY_LEAGUE_ID + leagueId);
        if (!response.ok) throw new Error('Error fetching partidos');

        const data = await response.json();

        // Estado principal (carga inmediata)
        setMatches(data);
        setFilteredMatches(data);
        setIsLoading(false);

        // Filtros (menos urgentes, diferidos)
        startTransition(async () => {
            if (data.length > 0) {
            const [w, t, r] = await Promise.all([
                getAllUniqueWeeks(data),
                getAllUniqueTeams(data),
                getAllUniqueResults(data),
            ]);
            setWeeks(w);
            setTeams(t);
            setResults(r);
            }
        });

        } catch (error: any) {
        setErrorMessage(ERROR_MESSAGES.NOT_FOUND_MATCHES_ON_LEAGUE);
        setShowError(true);
        setIsLoading(false);
        }
    };

    fetchAndPrepareMatches();
    }, [leagueId]);



    const getAllUniqueResults = (matches: MatchAPI[]) => {
        const uniqueResults = new Set<string>();
        matches.forEach(match => {
            uniqueResults.add(match.Score);
        });
        return Array.from(uniqueResults);
    }

    const getAllUniqueTeams = (matches: MatchAPI[]) => {
        const uniqueTeams = new Set<string>();
        matches.forEach(match => {
            uniqueTeams.add(match.Home.team_name);
            uniqueTeams.add(match.Away.team_name);
        });
        return Array.from(uniqueTeams);
    }

    const getAllUniqueWeeks = (matches: MatchAPI[]) => {
        const uniqueJornadas = new Set<string>();
        matches.forEach(match => {
            uniqueJornadas.add(match.Wk.toString());
        });
        return Array.from(uniqueJornadas);
    }


    const filterMatches = () => {
        const filteredMatches = matches.filter(match => {
            
            const filters = []

            if (selectedWeek) {
                filters.push(match.Wk.toString() === selectedWeek);
            }
            if (selectedResult) {
                filters.push(match.Score === selectedResult);
            }
            if (selectedTeam) {
                filters.push(match.Home.team_name === selectedTeam || match.Away.team_name === selectedTeam);
            }

            return filters.every(Boolean); 
        }) 
        setFilteredMatches(filteredMatches);
    };



    const handleClickMatch = (match: MatchAPI) => {
        console.log("match", match);
        navigate(`/show-match/${match.match_id}`);
    }
    const handleChangeWeeks = (value: string) => {
        setSelectedWeek(value);
    };
    const handleChangeTeams = (value: string) => {
        setSelectedTeam(value);
    }
    const handleChangeResult = (value: string) => {
        setSelectedResult(value);
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
            <LoadingIndicator isLoading={isLoading} />
            
            <Typography  gutterBottom>
                <strong>Filtrar por Jornada, Equipos y Resultado</strong>
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
                
                <Grid  size={{xs:12, sm:6, md:3}}>
                    <Typography gutterBottom>
                        <strong>Jornadas</strong>
                    </Typography>
                    {isLoadingFilters ? (
                        <Typography variant="body2">Cargando jornadas...</Typography>
                    ) : (
                        <FiltersElements
                            itemsToSelect={weeks}
                            selectedValue={selectedWeek || ""}
                            onChange={handleChangeWeeks}
                        />
                    )}

                </Grid>
        
                <Grid  size={{xs:12, sm:6, md:3}}>
                    <Typography gutterBottom>
                        <strong>Equipos</strong>
                    </Typography>
                    {isLoadingFilters ? (
                        <Typography variant="body2">Cargando jornadas...</Typography>
                    ) : (
                        <FiltersElements
                                itemsToSelect={teams}
                                selectedValue={selectedTeam || ""}
                                onChange={handleChangeTeams}
                        />
                    )}

                </Grid>
        
                <Grid size={{xs:12, sm:6, md:3}}>
                    <Typography gutterBottom>
                        <strong>Resultado</strong>
                    </Typography>
                    {isLoadingFilters ? (
                        <Typography variant="body2">Cargando jornadas...</Typography>
                    ) : (
                        <FiltersElements 
                            itemsToSelect={results}
                            selectedValue={selectedResult || ""}
                            onChange={handleChangeResult}
                        />
                    )}
                    
                    
                </Grid>
       
            
                <Grid size={{xs:12, sm:6, md:3}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
                    <Button
                        variant="contained"
                        color="primary"
                        fullWidth
                        sx={{ width: '100%' }}
                        onClick={() => filterMatches()}
                    >
                    Filtros
                    </Button>
                </Grid>
            </Grid>
            
            <Typography gutterBottom>
                <strong>Listado de resultados </strong>
            </Typography>

            <Grid container spacing={2} justifyContent="center" alignItems="center" sx={{ marginTop: 4, backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: 3, borderRadius: 2 }}>
                    <LoadingIndicator isLoading={isLoading} />      
                    {filteredMatches.map((match) => (
                        <Grid size={{xs:12, sm:6, md:3}}  sx={{ display: 'flex', justifyContent: 'center' }} key={match.match_id} onClick={() => handleClickMatch(match)}>
                            <CardShowOptions 
                                title={match.Home.team_name + "-" + match.Away.team_name} 
                                result={match.Score}
                                week={match.Wk.toString()}
                            />
                        </Grid>
                    ))}
            </Grid>
            
        </Container>
     
        );
}