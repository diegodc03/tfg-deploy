import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { statTranslation } from '../model/constants/Translate';



type Props = {
  data: any[]; 
};

const generateColumns = (data: any[]): GridColDef[] => {
  if (data.length === 0) return [];

  return Object.keys(data[0]).map((key) => ({
    field: key,
    headerName: statTranslation[key] || key.charAt(0).toUpperCase() + key.slice(1), // Traduce si existe
    width: 150,
    editable: key !== 'id', // No editable el ID
  }));
};


export default function StatsOfMatchPlayers({data}: Props) {

  const transformedData = data.map((row) => {
    const { estatistic_id, stat_id, player_id, ...rest } = row;

    return{
      Jugador: player_id?.player_name || 'Desconocido',
      ...rest
    };
  });

  const columns = React.useMemo(() => generateColumns(transformedData), [transformedData]);

  return (
    <Box sx={{ height: 1000, width: '100%' }}>
      <DataGrid
        rows={transformedData}
        columns={columns}
        getRowId={(row) => row.Jugador} // Usar el nombre del jugador como ID
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
