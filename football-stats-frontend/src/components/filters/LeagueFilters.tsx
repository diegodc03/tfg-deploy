import { Typography } from '@mui/material';
import GenericSelectProps from '../MultipleSelect';
import { LeagueAPI } from '../../model/LeagueAPI';

interface LeagueSelectProps {
  leagues: LeagueAPI[];
  value: string;
  onChange: (value: string) => void;
}

const LeagueSelect = ({ leagues, value, onChange }: LeagueSelectProps) => (
  <>
    <Typography><strong>Liga</strong></Typography>
    <GenericSelectProps<LeagueAPI>
      items={leagues}
      value={value}
      onChange={onChange}
      getId={(item) => item.name}
      getLabel={(item) => item.name}
    />
  </>
);

export default LeagueSelect;
