
import HomeIcon from '@mui/icons-material/Home';
import SearchIcon from '@mui/icons-material/Search';
import ContactMailIcon from '@mui/icons-material/ContactMail';
import ArticleIcon from '@mui/icons-material/Article';

import documentationPhoto from '../../images/homePage/Documentation.png';
import aboutUsPhoto from '../../images/homePage/about-us.png';
import statisticPhoto from '../../images/homePage/statistic-matchs.png';
import ComparacionDeJugadoresYGraficas from '../../images/matchStatsServices/ComparacionDeJugadoresYGraficas.png';
import EstadisticasDeJugadores from '../../images/matchStatsServices/EstadísticasDeJugadores.png';
import GraficosDeJugadores from '../../images/matchStatsServices/GráficosDeJugadores.png';
import GraficosDeLiga from '../../images/matchStatsServices/GráficosDeLiga.png';
import Puntuaciones from '../../images/matchStatsServices/Puntuaciones.png';
import GraficosDeComparacionDeEquipos from '../../images/matchStatsServices/GraficosDeComparaciónDeEquipos.png';

export const menuItems = [
  {
    label: 'Inicio',
    icon: <HomeIcon />,
    path: '/',
  },
  {
    label: 'Buscar Partidos',
    icon: <SearchIcon />,
    path: '/filter-by-season-and-league',
  },
  {
    label: 'Sobre Nosotros',
    icon: <ContactMailIcon />,
    path: '/contacto',
  },
  {
    label: 'Documentacion TFG',
    icon: <ArticleIcon />,
    path: '/documentacion-tfg',
  },
];


export const serviceItems = [
    {
        image: documentationPhoto,
        title: 'Documentación TFG',
        text: 'Accede a la documentación del TFG',
        navigateElement: 'documentacion-tfg',
    },
    {
        image: aboutUsPhoto,
        title: 'Sobre Nosotros',
        text: 'Conoce quiénes somos',
        navigateElement: 'contacto',
    },
    {
        image: statisticPhoto,
        title: 'Estadísticas',
        text: 'Revisa estadísticas detalladas que ofrecemos',
        navigateElement: 'filter-by-season-and-league',
    }
];



// Define CardItem type if not already defined or import it from the correct module
type CardItem = {
  title: string;
  text: string;
  image: string;
  navigateElement: string;
};

export const serviceItemsStatsPage = (match_id: string, tournament_id: string): CardItem[] => [
  {
    title: "Estadísticas de jugadores",
    text: "Todas las estadísticas de los jugadores (pases, goles...)",
    image: EstadisticasDeJugadores,
    navigateElement: `/match-players-stats/${match_id}`,
  },
  {
    title: "Comparación de jugadores y Gráficas",
    text: "Compara los jugadores del partido para ver cosas que nunca habías visto",
    image: ComparacionDeJugadoresYGraficas,
    navigateElement: `/stats-players-match/${match_id}`,
  },
  {
    title: "Puntuaciones",
    text: "Puntuaciones de los jugadores del partido según su posición y forma de juego",
    image: Puntuaciones,
    navigateElement: `/scores-of-players-match/${match_id}`,
  },
  {
    title: "Gráficos de jugadores",
    text: "Gráficos de los jugadores según la gráfica",
    image: GraficosDeJugadores,
    navigateElement: `/stats-chart-of-match/${match_id}`,
  },
  {
    title: "Gráficos de la liga",
    text: "Gráficos de comparacion con la liga",
    image: GraficosDeLiga,
    navigateElement: `/leagues-comparison`,
  },
  {
    title: "Gráficos de comparación de equipos",
    text: "Comparación de equipos de la liga como unitarios por temporada",
    image: GraficosDeComparacionDeEquipos,
    navigateElement: `/show-stats-comparison-from-teams/${tournament_id}`,
  },
];

