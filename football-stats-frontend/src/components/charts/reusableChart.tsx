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

const chartMap = {
  bar: Bar,
  line: Line,
  pie: Pie,
  doughnut: Doughnut,
  radar: Radar,
};

interface Props {
  stat: StatEntry;
}

export const ReusableChart = ({ stat }: Props) => {
  const ChartComponent = chartMap[stat.type || 'bar'];

  const chartData = {
    labels: stat.labels,
    datasets: [
      {
        label: stat.title,
        data: stat.data,
        backgroundColor: [
          '#1abc9c', '#3498db', '#9b59b6',
          '#f1c40f', '#e67e22', '#e74c3c'
        ],
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
            text: stat.title,
          },
        },
      }}
    />
  );
};
