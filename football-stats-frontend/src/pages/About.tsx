import { Container, Box, Typography, Link, Grid } from "@mui/material";

import realMadridImg from "../images/real_madrid.jpg";
import CardsContainer from "../components/CardsContainer";
import { GitHub, LinkedIn, Email } from '@mui/icons-material';

const About = () => {
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
                                
                }}
            >
                <Container maxWidth="xl" sx={{ marginTop: '15vh', marginBottom: '5vh' }}>
                    <Grid container 
                        spacing={6} 
                        justifyContent="center"
                        alignItems="center" 
                        sx={{ 
                            backgroundColor: 'rgba(255, 255, 255, 0.7)', 
                            padding: "1%", 
                            borderRadius: 2, 
                            mb: '20vh', 
                            mx: 'auto', 
                            paddingTop: 5, 
                            paddingBottom: 5 
                    }}>
                        <Box sx={{ textAlign: 'center', mb: 5 }}>
                            <Typography variant="h3" fontWeight="bold" gutterBottom>
                                Sobre Mí
                            </Typography>
                            <Typography variant="h6">
                                ¡Hola! Soy un apasionado de la informática, con gran interés por el desarrollo web y todo lo relacionado con la tecnología.
                                Además de pasar tiempo programando, disfruto mucho del baloncesto, el tenis y el deporte en general. Me encanta aprender y construir proyectos útiles y visualmente atractivos.
                            </Typography>
                        </Box>

                        <Box>
                            <Typography variant="h5" fontWeight="bold" gutterBottom>
                                Tecnologías que utilizo:
                            </Typography>
                            <Typography variant="body1">
                                He trabajado con herramientas y tecnologías como:
                                <ul>
                                <li>Frontend: React, JavaScript, HTML, CSS, Material UI</li>
                                <li>Backend: Django, Django REST Framework, Python</li>
                                <li>Bases de datos: PostgreSQL, SQLite</li>
                                <li>Otras: Git, GitHub, Docker, Postman</li>
                                </ul>
                            </Typography>
                        </Box>

                        <Box>
                            <Typography variant="h5" fontWeight="bold" gutterBottom>
                                Contacto
                            </Typography>
                            <Typography variant="body1" gutterBottom>
                                Puedes encontrarme y contactar conmigo en las siguientes plataformas:
                            </Typography>
                            <Grid container spacing={2} justifyContent="center">
                                <Grid >
                                    <Link href="https://github.com/tu_usuario" target="_blank" color="inherit">
                                        <GitHub fontSize="large" />
                                    </Link>
                                </Grid>
                                <Grid >
                                    <Link href="https://www.linkedin.com/in/tu_usuario" target="_blank" color="inherit">
                                        <LinkedIn fontSize="large" />
                                    </Link>
                                </Grid>
                                <Grid >
                                    <Link href="mailto:tuemail@ejemplo.com" color="inherit">
                                        <Email fontSize="large" />
                                    </Link>
                                </Grid>
                            </Grid>
                        </Box>
                    </Grid>
                </Container>
            </Box>
        </>
        
    );
    };

export default About;