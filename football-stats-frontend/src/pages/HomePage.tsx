import { Container, Box } from "@mui/material";

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
                <Container maxWidth="xl" sx={{ marginTop:20 }}>
                    <Box sx={{ mt: '15vh', textAlign: 'center' }}>
                    <h1 style={{ fontWeight: 'bold' }}>Player And Teams FootBall Stats</h1>
                    <p style={{ fontWeight: 'bold' }}>
                        Your Clubpage to check the stats of your favorite players and teams
                    </p>
                    </Box>
                    <CardsContainer />
                </Container>
            </Box>
        </>
        
    );
    };

export default HomePage;