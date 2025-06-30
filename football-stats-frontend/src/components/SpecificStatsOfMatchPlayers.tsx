import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';



type Props = {
  data: any[]; 
};

const generateColumns = (data: any[]): GridColDef[] => {
  if (data.length === 0) return [];

  return Object.keys(data[0]).map((key) => ({
    field: key,
    headerName: key.charAt(0).toUpperCase() + key.slice(1),
    width: 150,
    editable: key !== 'id',
  }));
};



export default function SpecificStatsOfMatchPlayers({data}: Props) {

    // Se tiene que convertir en texto plano para que se pueda mostrar el datagrid
    const transformedData = data.map((row) => {
        const base = {Nombre: row.jugador};
        row.values.forEach((value) => {
            base[value.column] = value.value;
        });
        return base;
        
    });
    const columns = React.useMemo(() => generateColumns(transformedData), [transformedData]);


  return (
    <Box sx={{ height: 1000, width: '100%' }}>
      <DataGrid
        rows={transformedData}
        columns={columns}
        getRowId={(row) => row.Nombre}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 20,
            },
          },
        }}
        pageSizeOptions={[5]}
      />
    </Box>
  );
}