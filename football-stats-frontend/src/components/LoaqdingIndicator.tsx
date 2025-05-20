import React from 'react';
import { Backdrop, CircularProgress, Box } from '@mui/material';

// Componente LoadingIndicator que puede ser reutilizado en cualquier parte
const LoadingIndicator = ({ isLoading }: { isLoading: boolean }) => {
  return (
    <Backdrop
      sx={{
        color: '#fff',
        zIndex: (theme) => theme.zIndex.drawer + 1,
      }}
      open={isLoading}
    >
      <CircularProgress color="inherit" />
    </Backdrop>
  );
};

export default LoadingIndicator;
