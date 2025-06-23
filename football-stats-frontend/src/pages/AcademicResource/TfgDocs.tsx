import { Container, Box, Grid, Typography, Button, CardContent, Card } from "@mui/material";
import DownloadForOfflineRoundedIcon from '@mui/icons-material/DownloadForOfflineRounded';
import { TfgDocsContent } from "../../model/constants/TfgDocsContent";

const TfgDocs = () => {


    return (
        
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
                {TfgDocsContent.map((annex, index) => (
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

    );
};

export default TfgDocs;