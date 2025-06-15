
import { Container, Grid, CssBaseline, Typography, Box } from '@mui/material';
import statsImage from '../images/stats.png';
import CardShow from './Cards';
import React from 'react';
import About from '../pages/About';
import TfgDocs from '../pages/TfgDocs';
import { serviceItems } from '../model/constants/menuItems';

import { useNavigate } from 'react-router-dom';

export default function CardsContainer() {

    const navigate = useNavigate();
    const handleNavigate = (path: string) => {
        navigate(path);
    };
    return (
        <>
        <CssBaseline />
        <Container maxWidth="lg" sx={{ mt: 45 }}>
            <Grid container spacing={6} justifyContent="center" alignItems="center" sx={{ backgroundColor: 'rgba(255, 255, 255, 0.7)', padding: "1%", borderRadius: 2, 
            mb: '20vh', mx: 'auto', paddingTop: 5, paddingBottom: 5 }}>
                <Box>
                    <Typography>
                        <h1 style={{ fontWeight: 'bold', textAlign: 'center' }}>Nuestros servicios</h1>
                        <p style={{ fontWeight: 'bold', textAlign: 'center' }}>
                        Esta página intenta ofrecer otra forma de ver el futbol, puediendo ver las estadisticas de los jugadores y equipos de una forma más visual y sencilla, junto con 
                        una forma diferente de puntuar a los jugadores, pudiendo así ver de una forma más objetiva el rendimiento de los jugadores.
            
                        </p>
                    </Typography>
                </Box>

                {serviceItems.map((item) => (
                    <Grid size={{ xs: 12, sm: 6, md: 3 }} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                        <CardShow title={item.title} text={item.text} image={item.image} navigateElement={item.navigateElement} />
                    </Grid>
                ))}
            </Grid>
        </Container>
    </>
    );
}