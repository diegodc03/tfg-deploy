
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';




interface GenericSelectProps<T> {
  items: T[] | string[];
  value: string;
  onChange: (value: string) => void;
  getId?: (item: T) => string;
  getLabel?: (item: T) => string;
  labelTodosShow?: boolean; // Si es true, muestra la opción "Todos" al inicio
}

export default function GenericSelect<T>({
  items,
  value,
  onChange,
  getId,
  getLabel,
  labelTodosShow = true,
}: GenericSelectProps<T>) {
  
  const handleChange = (event: SelectChangeEvent) => {
    onChange(event.target.value);
  };

  const isStringArray = items && items.length > 0 && typeof items[0] === 'string';


  return (
    <FormControl sx={{ width: '90%' }} size="small">
      <Select value={value} onChange={handleChange} displayEmpty>

        {labelTodosShow && (
          <MenuItem value="">
            <em>Todos</em>
          </MenuItem>
        )}
        {isStringArray 
        ? (items as string[]).map((item) => (
            <MenuItem key={item} value={item}>
              {item}
            </MenuItem>
          ))

        : (items as T[]).map((item) => (
            <MenuItem key={getId ? getId(item) : ''} value={getId ? getId(item) : ''}>
              {getLabel ? getLabel(item) : ''}
            </MenuItem>
          ))}
      </Select>
        
    </FormControl>
  );
}
