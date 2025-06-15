
import React, { useEffect } from 'react';
import { BasicMatchStats, StatValue } from '../model/BasicStatisticsGeneralMatchAPI';
import { Line } from 'react-chartjs-2';
import LinearStatBar from './LinearDetermine';
import Tipography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import { Divider, Paper, Stack, Typography } from '@mui/material';
import { API_ENDPOINTS } from '../model/constants/UrlConstants';

interface MatchIdProp {
    matchId: number;
  }



const ShowBasicStats = ({ matchId }: MatchIdProp) => {


    const [basicStats, setBasicStats] = React.useState<StatValue[]>([]);
    const [basicStatsPct, setBasicStatsPct] = React.useState<StatValue[]>([]);
    
    // Aqui hacemos peticion a la API para obtener las estadisticas del partido
    useEffect(() => {
        
        const  fetchBasicStats = async () => {
            try {  
                const response = await fetch(API_ENDPOINTS.PRINCIPAL_MATCH_STATS_COMPARATOR + `${matchId}`);
                
                if (!response.ok) {
                    throw new Error('Error fetching basic stats');
                }
                const data: BasicMatchStats = await response.json();
                const basicStats: StatValue[] = [];
                const basicStatsPct: StatValue[] = [];
                
                Object.entries(data).forEach(([key, value]) => {
                    if (key === 'match_id' || !value) return;
                    console.log(key, value);
          
                    const stat: StatValue = {
                        label: key,
                        local: value.local,
                        visitor: value.visitor,
                        type_stat_pct: value.type_stat_pct
                    };

                    if (value.type_stat_pct) {
                      basicStatsPct.push(stat);
                    } else {
                      basicStats.push(stat);
                    }
                });

                setBasicStats(basicStats);
                setBasicStatsPct(basicStatsPct);

            } catch (error) {
                console.error('Error fetching basic stats:', error);
            }
        }
        fetchBasicStats();
    }, [setBasicStats]);


    return (
        <>
            <Typography variant="h6"  sx={{  marginBottom: 2, fontWeight: 'bold' }}>
                    Estadísticas Generales
                </Typography> 
            <Grid container spacing={1}>
                {basicStats.map((stat, index) => (    
                    <Grid size={{ xs: 12, sm: 6, md: 3 }}>
                        <div key={index} style={{ marginBottom: '16px', display:"flex", flexDirection: 'column',alignItems: 'center' }} >
                            <Paper
                                elevation={4}
                                sx={{
                                    padding: 2,
                                    borderRadius: 2,
                                    bgcolor: 'background.default',
                                    border: '1px solid #ccc',
                                }}
                                >
                                <Stack direction="row" spacing={1} justifyContent="center" alignItems="center">
                                    <Paper elevation={3} style={{ padding: '8px', width: '100%', textAlign: 'center', minWidth: '40px', fontWeight: 'bold'  }}>
                                        {stat.local}
                                    </Paper>
                                    <Paper elevation={10} style={{ padding: '10px', width: '100%', textAlign: 'center', minWidth: '120px', fontWeight: 'bold' }}>
                                        {stat.label}
                                    </Paper>
                                    <Paper elevation={3} style={{ padding: '8px', width: '100%', textAlign: 'center', minWidth: '40px', fontWeight: 'bold' }}>
                                        {stat.visitor}
                                    </Paper>
                                </Stack>
                            </Paper>
                        </div>
                    </Grid>

                ))}
            
            </Grid>
                <Typography variant="h6"  sx={{ marginTop: 5, marginBottom: 2, fontWeight: 'bold' }}>
                    Estadísticas de Porcentaje
                </Typography>   
                {basicStatsPct.map((stat, index) => (
                <div key={index} style={{ marginBottom: '16px' }}>
                    <div style={{ display: 'flex', alignItems: 'center' }}>
                        <div style={{ marginRight: '8px', flex: 1 }}>
                            <Tipography variant="body2" fontWeight={1000}> 
                                {stat.local} 
                            </Tipography>
                            <LinearStatBar value={stat.local} />
                        </div>
                        <Paper elevation={10} 
                                style={{ padding: '10px', textAlign: 'center', minWidth: '150px' }} 
                                sx={{
                                    padding: 2,
                                    borderRadius: 2,
                                    bgcolor: 'background.default',
                                    border: '1px solid #ccc',
                                    fontWeight: 'bold'
                                }} >
                            {stat.label}
                        </Paper>

                        <div style={{ marginLeft: '8px', flex: 1, direction: 'rtl' }}>
                            <Tipography variant="body2" fontWeight={1000}>
                                {stat.visitor} 
                            </Tipography>
                            <LinearStatBar value={stat.visitor} reverse/>
                        </div>
                    </div>
                </div>
            
                ))} 
        </>
    );
}


export default ShowBasicStats;