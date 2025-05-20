import { ReusableChart } from './reusableChart';
import { Bar, Line, Pie, Doughnut, Radar } from 'react-chartjs-2';
import { PlayerStatGroup, StatEntry } from '../../model/statsTypes/stats';

interface Props {
    name: string;
    stats: StatEntry[];

}

export const StatsList = ({ name, stats }: Props) => {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">{name}</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {stats.map((stat, index) => (
          <div key={index} className="bg-white rounded-lg shadow p-4">
            <ReusableChart stat={stat} />
          </div>
        ))}
      </div>
    </div>
  );
};
