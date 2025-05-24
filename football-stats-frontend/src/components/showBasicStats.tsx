
import React, { useEffect } from 'react';
import { BasicMatchStats, StatValue } from '../model/BasicStatisticsGeneralMatchAPI';
import { Line } from 'react-chartjs-2';
import LinearStatBar from './LinearDetermine';
import Tipography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

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
                const response = await fetch(`http://localhost:8000/api/get-basic-stats-of-match-comparator/?match_id=${matchId}`);
                if (!response.ok) {
                    throw new Error('Error fetching basic stats');
                }
                const data: BasicMatchStats = await response.json();
                        // Filtrar las estadísticas dependiendo de type_stat_pct
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
          
            <h3>Estadísticas Generales</h3>
            <Grid container spacing={1}>
                {basicStats.map((stat, index) => (    
                    <Grid size={{ xs: 12, sm: 6, md: 3 }}>
                        <div key={index} style={{ marginBottom: '16px', display:"flex", flexDirection: 'column',alignItems: 'center', }} >
                                <p>{stat.local} - {stat.label} - {stat.visitor}</p>
                        </div>
                    </Grid>

                ))}
            </Grid>

                <h3>Estadísticas de Porcentaje</h3>
                {basicStatsPct.map((stat, index) => (
                <div key={index} style={{ marginBottom: '16px' }}>
                
                    <div style={{ display: 'flex', alignItems: 'center' }}>
                        <div style={{ marginRight: '8px', flex: 1 }}>
                            <Tipography variant="body2" color="textSecondary">
                                {stat.local} 
                            </Tipography>
                            <LinearStatBar value={stat.local} />
                        </div>
                        <p>{stat.label}</p>

                        <div style={{ marginLeft: '8px', flex: 1, direction: 'rtl' }}>
                            <Tipography variant="body2" color="textSecondary">
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