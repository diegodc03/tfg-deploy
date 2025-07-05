import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';

import { StatAPI } from '../model/StatsAPI/StatsAPI';
import { statTranslation } from '../model/constants/Translate';

type Props = {
  data: StatAPI[]; 
};

const generateColumns = (data: Record<string, any>[]): GridColDef[] => {
  if (data.length === 0) return [];

  return Object.keys(data[0]).map((key) => ({
    field: key,
    headerName:  statTranslation[key]|| key.charAt(0).toUpperCase() + key.slice(1),
    width: 150,
    editable: key !== 'id', // No editable el ID
  }));
};


export default function StatsTables({data}: Props) {

    const transformedData = data.map((row) => {

        let stats: any = {...row.stats };
      
        if (row.starter_status) {
            stats = {
            'Tiempo jugado': row.starter_status === 'starter' ? 'Titular +70m' : 'Suplente -70m',
            ...stats
            };
        }
        if (row.league_year) {
            stats = {
              'Temporada': row.league_year,
              ...stats
            };
        }
        if (row.team_name) {
            stats = {
              'Equipo': row.team_name,
            ...stats
            };
        }
        
        return stats;
    }, [data]);

    

  const columns = React.useMemo(() => generateColumns(transformedData), [transformedData]);

  return (
    <Box sx={{ width: '100%'}}>
      <DataGrid
        rows={transformedData}
        columns={columns}
        getRowId={(row) =>`${row['Temporada']}-${row['Tiempo jugado']}` } // Usar el nombre del jugador o id como ID
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
