

export const colorBasicPositionsCharts = {
    goalkeepers: '#FF5733',
    defenders: '#33FF57',
    midfielders: '#3357FF',
    forwards: '#FF33A1',
    other: '#CCCCCC',
}


export const colorTeamCharts = {
    home: '#FF8C00',
    away: '#1E90FF',

}




export const getBackgroundColorByLeague = (leagueName?: string): string => {
  switch (leagueName) {
    case 'La Liga':
      return '#FFF4B2'; // Amarillo pastel (inspirado en España)
    case 'Premier League':
      return '#E6D6EC'; // Lila claro (refleja el morado Premier)
    case 'Serie A':
      return '#D6EAF8'; // Azul celeste suave (Italia/Azzurro)
    case 'Bundesliga':
      return '#FADBD8'; // Rojo claro rosado (inspirado en Alemania)
    case 'Ligue 1':
      return '#DDEAF6'; // Azul muy claro (azul francés sobrio)
    default:
      return '#ffffff'; // Blanco por defecto
  }
};


export const getBackgroundGradientByLeague = (leagueName?: string): string => {
  switch (leagueName) {
    case 'La Liga': // España 🇪🇸 (rojo y amarillo)
      return 'linear-gradient(to bottom, rgb(204, 0, 0) 0%, rgb(204, 0, 0) 25%, #FFC107 25% 75%, rgb(204, 0, 0) 75% 100%)';
    case 'Premier League': // Reino Unido 🇬🇧 (azul, rojo, blanco)
      return '';
    case 'Serie A': // Italia 🇮🇹 (verde, blanco, rojo)
      return 'linear-gradient(to bottom, #008C45 33.33%, #FFFFFF 33.33% 66.66%, #CD212A 66.66%)';
    case 'Bundesliga': // Alemania 🇩🇪 (negro, rojo, amarillo)
      return 'linear-gradient(to bottom, #000000 33.33%, #DD0000 33.33% 66.66%, #FFCE00 66.66%)';
    case 'Ligue 1': // Francia 🇫🇷 (azul, blanco, rojo)
      return 'linear-gradient(to right, #0055A4 33%, #FFFFFF 33% 66%, #EF4135 66%)';
    default:
      return 'linear-gradient(135deg, #ECEFF1, #CFD8DC)'; // Gris suave neutro
  }
};
