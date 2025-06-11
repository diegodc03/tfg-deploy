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
import {  ChartType } from '../../model/statsTypes/stats';


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
  stat: number[];
  typeOfChart: string;
  labels: string[]; 
  
}

type dictNumbers = {
    numberELement: number[];
}



export const ChartOfNumbersOfScores = ({ stat, typeOfChart, labels }: Props) => {
  
  const chartData = {
    labels: labels,
    datasets: [
      {
        data: stat,
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"],
      },
    ],
  };

  const ChartComponent = chartMap[typeOfChart as ChartType] || Bar;

  return (
    <ChartComponent
      data={chartData}
      options={{
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: "Statistics Chart",
          },
          legend: {
            display: true,
            labels: {
              color: 'black',
            },
          },
        },
      }}
    />
  );
};
