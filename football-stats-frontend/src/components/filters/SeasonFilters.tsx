import { Typography } from '@mui/material';
import GenericSelectProps from '../MultipleSelect';
import { LeagueAPI } from '../../model/LeagueAPI';
import { Season } from '../../model/SeaonAPI';

interface SeasonSelectProps {
  seasons: Season[];
  value: string;
  onChange: (value: string) => void;
}

const SeasonSelect = ({ seasons, value, onChange }: SeasonSelectProps) => (
    <>
        <Typography>
            <strong>Temporada</strong>
        </Typography>
        <div>
            <GenericSelectProps<Season>
                items={seasons}
                value={value || ''}
                onChange={onChange}
                getId={(item) => String(item.season_id)}
                getLabel={(item) => item.season_year}
            />
        </div>
    </>
);

export default SeasonSelect;
