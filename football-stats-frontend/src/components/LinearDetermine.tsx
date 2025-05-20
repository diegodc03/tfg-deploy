import * as React from 'react';
import Box from '@mui/material/Box';
import LinearProgress, { linearProgressClasses } from '@mui/material/LinearProgress';
import { styled } from '@mui/material/styles';

const BorderLinearProgress = styled(LinearProgress)(({ theme }) => ({
    height: 10,
    borderRadius: 5,
    [`&.${linearProgressClasses.colorPrimary}`]: {
      backgroundColor: theme.palette.grey[200],
      ...(theme.palette.mode === 'dark' && {
        backgroundColor: theme.palette.grey[800],
      }),
    },
    [`& .${linearProgressClasses.bar}`]: {
      borderRadius: 5,
      backgroundColor: '#1a90ff',
      ...(theme.palette.mode === 'dark' && {
        backgroundColor: '#308fe8',
      }),
    },
  }));
  
export default function LinearStatBar({ value }: { value: number }) {
    return (
      <Box sx={{ width: '100%' }}>
        <BorderLinearProgress variant="determinate" value={value} />
      </Box>
    );
  }