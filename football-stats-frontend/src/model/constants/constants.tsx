

export const colorBasicPositionsCharts = {
    goalkeepers: '#FF5733',
    defenders: '#33FF57',
    midfielders: '#3357FF',
    forwards: '#FF33A1',
    other: '#CCCCCC',
}

export const colorGameModesCharts = {
    bloque_medio: '#FF5733',
    bloque_bajo: '#3357FF',
    tiki_taka: '#FF33A1',
    contraataque: '#CCCCCC',
    presion_alta: '#FF8C00',
    juego_por_bandas: '#1E90FF',
}

export const otherColors = {
    yellow: '#FFFF00',
    red: '#FF0000',
    green: '#00FF00',
    blue: '#0000FF',
    black: '#000000',
    gray: '#808080',
    orange: '#FFA500',
    purple: '#800080',
    pink: '#FFC0CB',
    brown: '#A52A2A',
    cyan: '#00FFFF',
    magenta: '#FF00FF',
    lightBlue: '#ADD8E6',
}

export const colorTotalScoresCharts = {
    1: '#FF5733',
    2: '#33FF57',
    3: '#3357FF',
    4: '#FF33A1',
    5: '#CCCCCC',
    6: '#FF8C00',
    7: '#1E90FF',
    8: '#FFB6C1',
    9: '#FFD700',
    10: '#FF4500',
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
      return 'default'; // Gris suave neutro
  }
};



