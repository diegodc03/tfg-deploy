
import { Bar, Line, Pie, Doughnut, Radar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  ArcElement,
  PointElement,
  RadialLinearScale,
  Tooltip,
  Legend,
  Title,
} from 'chart.js';
import { StatEntry, ChartType, PlayerStatGroup } from '../../model/statsTypes/stats';
import { StatValues } from '../../model/statsTypes/StatsModel';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  ArcElement,
  PointElement,
  RadialLinearScale,
  Tooltip,
  Legend,
  Title
);

import { colorBasicPositionsCharts, colorGameModesCharts, colorTeamCharts, colorTotalScoresCharts, otherColors } from '../../model/constants/constants';

const chartMap = {
  bar: Bar,
  line: Line,
  pie: Pie,
  doughnut: Doughnut,
  radar: Radar,
};

const typeOfChartColors = {
    positions: colorBasicPositionsCharts,
    teams: colorTeamCharts,
    gameModes: colorGameModesCharts,
    totalScores: colorTotalScoresCharts,
    other: otherColors
  
};

interface Props {
  stat: StatEntry;
  typeOfChart: string;
  typeOfChartColor?: 'positions' | 'teams' | 'gameModes' | 'totalScores' | 'other';
  
}




export const ReusableChart1 = ({ stat, typeOfChart, typeOfChartColor }: Props) => {

    
    const ChartComponent = chartMap[typeOfChart as keyof typeof chartMap] || Bar;
    const typeColors = typeOfChartColors[typeOfChartColor as keyof typeof typeOfChartColors] || colorBasicPositionsCharts;

    const colorValues = Object.values(typeColors);

    
    
    
    const getSeasonFromLabel = (label: string) => label.split(" - ")[0];
    // Mapear cada temporada única a un color
    const uniqueSeasons = Array.from(new Set(stat.labels.map(getSeasonFromLabel)));
    const seasonToColor: Record<string, string> = {};

    uniqueSeasons.forEach((season, index) => {
        seasonToColor[season] = colorValues[index % colorValues.length]; // Cicla si hay más temporadas que colores
    });

    
    
    
    const backgroundColor = stat.labels.map(label => {
        const season = getSeasonFromLabel(label);
        return seasonToColor[season] || '#000000'; // Color por defecto si algo falla
    });


    const tittleIfNotExists = () => {
        if (typeOfChartColor === "positions") {
            return "Estadísticas por Posición";
        } else if (typeOfChartColor === "totalScores") {
            return "Estadísticas Totales";
        } else {
            return "Estadísticas";
        }
    };

    const chartOptions = {
        responsive: true,
        plugins: {
        title: {
            display: true,
            text: stat.title || tittleIfNotExists(),
        },
        legend: {
            display: true,
            labels: {
            generateLabels: () => {
                const positionsUsed = new Set(
                    (typeOfChartColor === 'other'
                        ? stat.labels.map(label => getSeasonFromLabel(label))
                        : stat.labels.map(label => label || 'other'))
                );

                return Array.from(positionsUsed).map((element, i) => ({
                    text: element,
                    fillStyle: seasonToColor[element] || backgroundColor[i] || '#000000',
                    strokeStyle: seasonToColor[element] || backgroundColor[i] || '#000000',
                    lineWidth: 0,
                    hidden: false,
                    index: 0,
           }));
            },
            },
        },
        datalabels: {
            display: true,
            color: 'black',
            font: {
                weight: 'bold',
                size: 12,
            },
                formatter: (value) => value,  // Muestra el valor directamente
                anchor: 'end',
                align: 'top',
            },
        },
    };


    const chartData = {
        labels: stat.labels,
        datasets: [
            {
                label: stat.title,
                data: stat.data,
                backgroundColor,
            },
        ],
    };

    return (
        <ChartComponent
        data={chartData}
        options={chartOptions}
        />
    );
    };
