import { Container, Box, Grid, Typography, Button, CardContent, Card } from "@mui/material";
import DownloadForOfflineRoundedIcon from '@mui/icons-material/DownloadForOfflineRounded';
import { DownloadAllDocsLink, TfgDocsContent } from "../../model/constants/TfgDocsContent";

const TfgDocs = () => {


    return (
        
        <Container maxWidth="lg">

            <Box sx={{ mt: '3rem', textAlign: 'center' }}>      
                <Box 
                    sx={{ 
                        backgroundColor: 'rgba(255, 255, 255, 0.7)', 
                        padding: "1%", 
                        borderRadius: 2, 
                        mb: '10rem', 
                        mx: 'auto', 
                        paddingTop: 5, 
                        paddingBottom: 3 
                    }}
                >
                    <Typography variant="h4" fontWeight="bold" sx={{ mb: 2 }}>
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
                    <Button
                        variant="outlined"
                        href={DownloadAllDocsLink}
                        target="_blank"
                        sx={{ color: 'black', mt:2}}
                    >
                        <strong> Descargar Todo </strong>
                        <DownloadForOfflineRoundedIcon sx={{ ml: 1 }} />
                    </Button>
                </Box>    
            </Box>

            <Box sx={{ textAlign: "center", mb: 5 }}>
                
            </Box>
            <Grid container spacing={4} sx={{ mb: '5rem', mx: 'auto', paddingTop: 5,}}>
                {TfgDocsContent.map((annex, index) => (
                    <Grid size = {{ xs:12, sm:6, lg:4 }} key={index}>
                        <Card elevation={4} sx={{ borderRadius: "20px", p: 2 }}>
                            <CardContent>
                                <Typography variant="h6" fontWeight="bold" gutterBottom>
                                    {annex.title}
                                </Typography>
                                <Button
                                    variant="outlined"
                                    sx={{ backgroundColor: 'black', mt: 2, width: '100%', color: 'white', '&:hover': { backgroundColor: 'darkgray' } }}
                                    
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