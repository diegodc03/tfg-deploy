import { Container, Box, Typography } from "@mui/material";
import CardsContainer from "../../components/CardsContainer";
import { useChargeAllFilters } from "../../hooks/ChargeFilters";
import ErrorSnackbar from "../../components/showError";
import LoadingIndicator from "../../components/LoaqdingIndicator";
import { useStadium } from "../../layout/StadiumContext";
import { stadiumName } from "../../model/constants/StadiumName";

const HomePage = () => {

    const { isLoading, showError, setShowError, errorMessage } = useChargeAllFilters();
    const { selected } = useStadium();

    


    return (
        <>
            <ErrorSnackbar
                open={showError}
                onClose={() => setShowError(false)}
                message={errorMessage ?? "Ha ocurrido un error inesperado"}
                position={{ vertical: 'top', horizontal: 'right' }}
                large={true}
            />
            <LoadingIndicator isLoading={isLoading} />
            
            <Container maxWidth="lg" >
                <Box sx={{ mt: '3rem', textAlign: 'center' }}>
                     
                        <Box 
                            justifyContent="center" 
                            alignItems="center"
                            sx={{ 
                                backgroundColor: 'rgba(255, 255, 255, 0.7)', 
                                padding: "1%", 
                                borderRadius: 4, 
                                mb: '20vh', 
                                mx: 'auto', 
                                paddingTop: 5, 
                                paddingBottom: 5 
                            }}
                        >
                            <Typography variant="h3" gutterBottom sx={{ fontWeight: 'bold' }}>
                                Player And Teams FootBall Stats
                            </Typography>
                            <Typography sx={{ fontWeight: 'bold' }} variant="h6" gutterBottom>
                                Tu página para analizar estadísticas de jugadores y equipos de fútbol
                            </Typography>
                        </Box>
                
                </Box>
                <CardsContainer />
            </Container>
        </>
        
    );
    };

export default HomePage;