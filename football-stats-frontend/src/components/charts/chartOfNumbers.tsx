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
  console.log("stat", stat);
  console.log("typeOfChart", typeOfChart);
  console.log("labels", labels);
  const chartData = {
    labels: labels,
    datasets: [
      {
        data: stat,
        backgroundColor: [
          "#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF",
          "#FF9F40", "#C9CBCF", "#8BC34A", "#E91E63", "#00BCD4",
          "#FFEB3B", "#9C27B0", "#607D8B", "#F44336", "#3F51B5"
        ],
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
            text: "Notas totales de los jugadores",
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
