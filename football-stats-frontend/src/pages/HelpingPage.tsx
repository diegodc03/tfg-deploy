
import { Box, Container, Typography, Grid, Stack } from '@mui/material';
import EstadisticasGenerales from "../images/helpingPage/EstadísticaGenerales.png";
import EstadisticasEspecificas from "../images/helpingPage/EstadísticasEspecíficasPartido.png";
import filtroDeLigas from "../images/helpingPage/filtroDeLigas.png";
import initPage from "../images/helpingPage/InitPage.png";
import serviceOfferInitPage from "../images/helpingPage/serviceOfferInitPage.png";
import filtrosPartidos from "../images/helpingPage/filtrosPartidos.png";
import infoPartido from "../images/helpingPage/infoPartido.png";
import estadísticasJugadoresTabla from "../images/helpingPage/EstadísticasDeJugadores.png";
import ComparaciónDeJugadoresyGráficasTabla from "../images/helpingPage/ComparaciónDeJugadoresyGráficas.png";
import PuntuacionesTabla from "../images/helpingPage/Puntuaciones.png";
import Puntuaciones_2Grafica from "../images/helpingPage/Puntuaciones_2.png";
import Puntuaciones_3Grafica from "../images/helpingPage/Puntuaciones_3.png";
import GraficosJugadoresComparacionGrafica from "../images/helpingPage/GráficosDeJugadores.png";
import GraficosLiga1Tabla from "../images/helpingPage/GraficosLiga_1.png";
import GraficosLiga2Grafica from "../images/helpingPage/GraficosLiga_2.png";
import graficosComparacionEquiposTabla from "../images/helpingPage/GraficosComparacionEquipos_1.png";
import graficosComparacionEquipos2Grafica from "../images/helpingPage/GraficosComparacionEquipos_2.png";


const content = [
    {
        text: "Aquí encontrarás información útil para resolver tus dudas y problemas en la interfaz de usuario. También puedes escribirnos a través de nuestro correo electrónico para obtener asistencia personalizada.",
        image: initPage,
        reverse: false,
    },
    {
        text: "La página está constituida por 3 grandes secciones: Documentación TFG, Sobre Nosotros y Estadísticas. En estadísticas se centraliza la funcionalidad principal de la aplicación, permitiendo consultar estadísticas de jugadores y equipos.",
        image: serviceOfferInitPage,
        reverse: true,
    },
    {
        text: "En el apartado de estadísticas se ofrece el filtrado de temporadas para hacer la búsqueda del partido más sencilla, pudiendo filtrar por temporada y liga.",
        image: filtroDeLigas,
        reverse: false,
    },
    {
        text: "Tras filtrar, se muestra una página con los partidos de esa liga y temporada. Puedes filtrar por equipo, jornada o resultado del partido.",
        image: filtrosPartidos,
        reverse: true,
    },
    {
        text: "Tras seleccionar el partido, se va a mostrar una página con los datos del partido, incluyendo el nombre de los equipos, la fecha y hora del partido, y el resultado.",
        image: infoPartido,
        reverse: false,
    },
    {
        text: "Se mostrará también en la página, las estadísticas genéricas del partido: resultado, tarjetas, goles y estadísticas totales por equipo.",
        image: EstadisticasGenerales,
        reverse: true,
    },
    {
        text: "Además, se ofrecen varias secciones con estadísticas más detalladas y puntuaciones de jugadores, equipos y ligas: estadísticas de jugadores, estadísticas de equipos, y estadísticas de ligas.",
        image: EstadisticasEspecificas,
        reverse: false,
    },
    {
        text: "Vista de estadísticas de jugadores en tabla, con todos los datos numéricos relevantes de rendimiento individual. (todas las estadísticas de los jugadores del partido)",
        image: estadísticasJugadoresTabla,
        reverse: true,
    },
    {
        text: "Vista de estadísticas de jugadores en tabla, con todos los datos numéricos filtrados segun diferentes tipos de estadísticas (tiros, pases, etc.).",
        image: ComparaciónDeJugadoresyGráficasTabla,
        reverse: false,
    },
    {
        text: "Visualización de puntuaciones generales de jugadores en formato tabla. Estas puntuaciones son respecto a su rendimiento en el partido. EL usuario puede elegir el rol del jugador para ver como se comporta mejor. Tambien puede filtrar para asi comparar con diferentes posiciones, tanto muy espeíficas (delantero centro, mediocentro defensivo, etc.) como más generales (delantero, centrocampista, defensa, portero).",
        image: PuntuacionesTabla,
        reverse: true,
    },
    {
        text: "Gráfica de evolución de puntuaciones totales para asi poder ver la media del partido",
        image: Puntuaciones_2Grafica,
        reverse: false,
    },
    {
        text: "Gráfica de las puntuaciones comparativas según el rol del jugador. Esta gráfica permite ver cómo se comporta cada jugador según su rol en el partido.",
        image: Puntuaciones_3Grafica,
        reverse: true,
    },
    {
        text: "Compracion visual de los jugadores del partido, mostrando sus estadísticas clave en una gráfica comparativa.",
        image: GraficosJugadoresComparacionGrafica,
        reverse: false,
    },
    {
        text: "Visualización en tabla de las estadísticas por liga.",
        image: GraficosLiga1Tabla,
        reverse: true,
    },
    {
        text: "Gráficos de rendimiento agregado de la liga, mostrando la comparación en diferentes años con una estadística clave.",
        image: GraficosLiga2Grafica,
        reverse: false,
    },
    {
        text: "Tabla de comparación entre equipos con sus respectivas métricas clave.",
        image: graficosComparacionEquiposTabla,
        reverse: true,
    },
    {
        text: "Gráfica visual de la comparación entre los diferentes años de un equipo, para poder ver la mejora o empeoramiento del equipo a lo largo de los años.",
        image: graficosComparacionEquipos2Grafica,
        reverse: false,
    }
];

const HelpingPage = () => {
  return (
    

      <Container maxWidth="lg">
        <Typography variant="h3" gutterBottom sx={{ fontWeight: 'bold', marginTop: '15vh', textAlign: 'center', marginBottom: '10vh' }}>
          Ayuda y Soporte
        </Typography>

        <Grid container spacing={6} justifyContent="center" alignItems="center" sx={{ backgroundColor: 'rgba(255, 255, 255, 0.9)', padding: "1%", borderRadius: 2, mb: '20vh', mx: 'auto', paddingTop: 5, paddingBottom: 5 }}>
          <Stack sx={{ width: '100%', height: '100%' }} justifyContent="center" alignItems="center">
            <Typography sx={{ fontWeight: 'bold' }} variant="h6" gutterBottom>
              Correo de contacto: <a href="mailto:diegodecastro@usal.es" style={{ color: 'inherit', textDecoration: 'none' }}>Enviar correo</a>
            </Typography>
          </Stack>

          {content.map((section, index) => (
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
