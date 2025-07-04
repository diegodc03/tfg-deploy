
import { Box, Container, Typography, Grid, Stack } from '@mui/material';
import { HelpingPageContent } from '../../model/constants/HelpingPageContent';


const HelpingPage = () => {
  return (
    

      <Container maxWidth="lg">
        <Typography variant="h3" gutterBottom sx={{ fontWeight: 'bold', marginTop: '15vh', textAlign: 'center', marginBottom: '10vh' }}>
          Ayuda y Soporte
        </Typography>

        <Grid container spacing={6} justifyContent="center" alignItems="center" sx={{ backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: "2rem", borderRadius: 4, mb: '20vh', mx: 'auto', paddingTop: 5, paddingBottom: 5 }}>
          <Stack sx={{ width: '100%', height: '100%' }} justifyContent="center" alignItems="center">
            <Typography sx={{ fontWeight: 'bold' }} variant="h6" gutterBottom align='center'>
              Para mayor explicación, vaya a Documentacion TFG, donde puede descargar el manual de usuario y el manual técnico del proyecto.
            </Typography>
          </Stack>

          {HelpingPageContent.map((section, index) => (
            <Grid container spacing={4} alignItems="center" key={index} direction={section.reverse ? 'row-reverse' : 'row'} sx={{ mb: 4 }}>
              <Grid size={{ xs:12, md:6}}>
                <Box
                  component="img"
                  src={section.image}
                  alt={`section-${index}`}
                  sx={{ width: '100%', borderRadius: 2, boxShadow: 3 }}
                />
              </Grid>
              <Grid size={{ xs:12, md:6}}>
                <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                  {section.text}
                </Typography>
              </Grid>
            </Grid>
          ))}

        </Grid>
      </Container>

  );
};

export default HelpingPage;
