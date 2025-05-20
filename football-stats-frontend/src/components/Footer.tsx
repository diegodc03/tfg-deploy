


import React from 'react';
import { Box, Container, Grid, Typography } from "@mui/material";



const Footer = () => {
  return (
    <Box component="footer" sx={{ backgroundColor: '#212529', color: '#fff', py: 2 }}>
      <Container maxWidth="xl">
      <Grid container justifyContent="center" columnSpacing={20} textAlign="center">
          <Grid  size={{xs:12, sm:6, md:4}}>
            <Typography variant="body1" >
              <strong>DESARROLLADO POR:</strong> DIEGO DE CASTRO MERILLAS
            </Typography>
          </Grid>
          <Grid  size={{xs:12, sm:6, md:4}}>
            <Typography variant="body1">
              © 2024 - Trabajo de Fin de Grado - Universidad de Salamanca
            </Typography>
          </Grid>
        </Grid>
      </Container>
    </Box>
);
};

export default Footer;