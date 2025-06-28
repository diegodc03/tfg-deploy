import React from 'react';
import { Snackbar, Alert, AlertColor } from '@mui/material';

interface ErrorSnackbarProps {
  open: boolean;
  onClose: () => void;
  message: string;
  severity?: AlertColor; // "error" | "warning" | "info" | "success"
  position?: {
    vertical: 'top' | 'bottom';
    horizontal: 'left' | 'center' | 'right';
  };
  large?: boolean; // si true, agranda visualmente el Alert
}

const ErrorSnackbar: React.FC<ErrorSnackbarProps> = ({
  open,
  onClose,
  message,
  severity = 'error',
  position = { vertical: 'top', horizontal: 'center' },
  large = false,
}) => {
  return (
    <Snackbar
      open={open}
      autoHideDuration={6000}
      onClose={onClose}
      anchorOrigin={position}
    >
      <Alert
        onClose={onClose}
        severity={severity}
        sx={{
          width: large ? '100%' : 'auto',
          fontSize: large ? '1.2rem' : 'inherit',
          p: large ? 3 : 1,
        }}
      >
        {message}
      </Alert>
    </Snackbar>
  );
};

export default ErrorSnackbar;
