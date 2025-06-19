import { Container, Box, Typography } from "@mui/material";
import CardsContainer from "../components/CardsContainer";


const HomePage = () => {


    return (
        <>
            
            <Container maxWidth="xl" >
                <Box sx={{ mt: '15vh', textAlign: 'center' }}>
                    
                    <Typography variant="h3" gutterBottom sx={{ fontWeight: 'bold' }}>
                        Player And Teams FootBall Stats
                    </Typography>
                    <Typography sx={{ fontWeight: 'bold' }} variant="h6" gutterBottom>
                        Tu página para analizar estadísticas de jugadores y equipos de fútbol
                    </Typography>
                </Box>
                <CardsContainer />
            </Container>
        </>
        
    );
    };

export default HomePage;