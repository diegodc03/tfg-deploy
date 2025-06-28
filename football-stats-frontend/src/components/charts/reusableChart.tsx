// components/ReusableChart.tsx

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
import { StatEntry, ChartType } from '../../model/statsTypes/stats';
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

import { colorBasicPositionsCharts, colorTeamCharts } from '../../model/constants/constants';

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
};

interface Props {
  stat: StatValues;
  typeOfChart: string;
  
  
}




export const ReusableChart = ({ stat, typeOfChart }: Props) => {
  console.log("stat", stat);
  const typeOfChartColor = "positions"; // Default color scheme, can be 'positions' or 'teams'

  const ChartComponent = chartMap[typeOfChart as keyof typeof chartMap] || Bar;
  const typeColors = typeOfChartColors[typeOfChartColor as keyof typeof typeOfChartColors] || colorBasicPositionsCharts;

  const labels = stat.values.map((entry) => entry.player_name);
  const dataValues = stat.values.map((entry) => entry.value);
  const backgroundColor = stat.values.map(entry => typeColors[entry.basic_position] || typeColors['other']); // ['#33FF57', '#3357FF', ...]


  const chartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: stat.stat,
      },
      legend: {
        display: true,
        labels: {
          generateLabels: () => {
            const positionsUsed = new Set(stat.values.map(v => v.basic_position || 'other'));

            return Array.from(positionsUsed).map(position => ({
              text: position,
              fillStyle: typeColors[position] || typeColors["other"],
              strokeStyle: typeColors[position] || typeColors["other"],
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
    labels: labels,
    datasets: [
      {
        label: stat.stat,
        data: dataValues,
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
