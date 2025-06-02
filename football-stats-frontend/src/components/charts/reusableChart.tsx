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
  
  const typeOfChartColor = "positions"; // Default color scheme, can be 'positions' or 'teams'

  const ChartComponent = chartMap[typeOfChart as keyof typeof chartMap] || Bar;
  const typeColors = typeOfChartColors[typeOfChartColor as keyof typeof typeOfChartColors] || colorBasicPositionsCharts;
  // Dependiendo el grafico es necesario transformar los datos o no, ya que de linea si, pero de 

  const labels = stat.values.map((entry) => entry.player_name);
  const dataValues = stat.values.map((entry) => entry.value);

  const isSingleDatasetChart = ['bar', 'line', 'radar'];
  const isPieLikeChart = ['pie', 'doughnut'];
  const typeFilterColorChart = []

  const backgroudColors = stat.values.map((entry, index) => {
    return typeColors[entry.basic_position] || typeColors["other"]
  });



  const chartData = {
    labels: labels,
    datasets: [
      {
        label: stat.stat,
        data: dataValues,
        backgroundColor: backgroudColors,
      },
    ],
  };

  return (
    <ChartComponent
      data={chartData}
      options={{
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: stat.stat,
          },
        },
      }}
    />
  );
};
