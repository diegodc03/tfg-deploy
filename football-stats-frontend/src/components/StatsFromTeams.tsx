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
    editable: key !== 'id', // Por ejemplo: no editar el id
  }));
};



