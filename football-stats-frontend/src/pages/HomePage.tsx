import { Container, Box, Typography } from "@mui/material";

import realMadridImg from "../images/real_madrid.jpg";
import CardsContainer from "../components/CardsContainer";

const HomePage = () => {
    return (
        <>
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
            </Box>
        </>
        
    );
    };

export default HomePage;