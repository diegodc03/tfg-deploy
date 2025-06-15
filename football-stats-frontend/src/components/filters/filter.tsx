import { Typography } from '@mui/material';
import GenericSelectProps from '../MultipleSelect';
import { LeagueAPI } from '../../model/LeagueAPI';

interface SelectProps {
  itemsToSelect: string[];
  selectedValue: string;
  onChange: (value: string) => void;
}

const FiltersElements = ({ itemsToSelect, selectedValue, onChange }: SelectProps) => (
  <>
    <GenericSelectProps<LeagueAPI>
      items={itemsToSelect}
      value={selectedValue}
      onChange={onChange}
      getId={(item) => item.name}
      getLabel={(item) => item.name}
    />
  </>
);

export default FiltersElements;
