import { Container, Box, Grid, Typography, Button, CardContent, Card } from "@mui/material";

import realMadridImg from "../images/real_madrid.jpg";
import CardsContainer from "../components/CardsContainer";
import DownloadForOfflineRoundedIcon from '@mui/icons-material/DownloadForOfflineRounded';

const TfgDocs = () => {

    
    const annexes = [
        {
            title: "Memoria del TFG",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo I: Planificación del Proyecto",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo II: Especificación de Requisitos",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo III: Diseño de la Arquitectura",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo IV: Manual de Usuario",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo V: Manual Técnico",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
        {
            title: "Anexo VI: Resultados y Pruebas",
            link: "https://docs.google.com/document/d/1Vy6yQnUz_TBZZ5LhZXqOdNZ8bJsQ0TAgYelSz_9Nro0/edit?usp=drive_link",
        },
    ];

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
                    
            }}
        >
            <Container maxWidth="xl" sx={{ marginTop: 10, marginBottom: 5 }}>
                <Box sx={{ textAlign: "center", mb: 5 }}>
                    <Typography variant="h5" fontWeight="bold">
                        Índice de Anexos del TFG
                    </Typography>
                    <Typography variant="h6" fontWeight="bold">
                        Esta página es un proyecto de TFG de la Universidad de Salamancan del grado en Ingeniería Informática
                    </Typography>
                    <Typography variant="h6" fontWeight="bold">
                        Está realizado por: Diego de Castro Merillas
                    </Typography>
                    <Typography variant="subtitle1" fontWeight="bold" mt={2}>
                        Descarga cada documento en formato PDF desde los enlaces disponibles
                    </Typography>
                </Box>
                <Grid container spacing={4}>
                    {annexes.map((annex, index) => (
                        <Grid size = {{ xs:12, sm:6, lg:4 }} key={index}>
                            <Card elevation={4} sx={{ borderRadius: "20px", p: 2 }}>
                                <CardContent>
                                    <Typography variant="h6" fontWeight="bold" gutterBottom>
                                        {annex.title}
                                    </Typography>
                                    <Button
                                        variant="outlined"
                                        color="primary"
                                        href={annex.link}
                                        target="_blank"
                                    >
                                        Descargar
                                        <DownloadForOfflineRoundedIcon sx={{ ml: 1 }} />
                                    </Button>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </Container>
        </Box>


    );
};

export default TfgDocs;