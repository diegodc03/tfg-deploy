
import React, { useEffect } from 'react';
import { BasicMatchStats, StatValue } from '../model/BasicStatisticsGeneralMatchAPI';
import { Line } from 'react-chartjs-2';
import LinearStatBar from './LinearDetermine';


const ShowBasicStats = ({ stats }: { stats: any }) => {


    const [basicStats, setBasicStats] = React.useState<StatValue[]>([]);
    const [basicStatsPct, setBasicStatsPct] = React.useState<StatValue[]>([]);
    
    // Aqui hacemos peticion a la API para obtener las estadisticas del partido
    useEffect(() => {
        
        const  fetchBasicStats = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/basic-match-stats/`);
                if (!response.ok) {
                    throw new Error('Error fetching basic stats');
                }
                const data: BasicMatchStats = await response.json();
                        // Filtrar las estadísticas dependiendo de type_stat_pct
                const basicStats: StatValue[] = [];
                const basicStatsPct: StatValue[] = [];
                
                Object.entries(data).forEach(([key, value]) => {
                    if (key === 'match_id' || !value) return;
          
                    if (value.type_stat_pct) {
                      basicStatsPct.push(value);
                    } else {
                      basicStats.push(value);
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
            <div>
                <h2>Estadísticas del Partido</h2>
                
                <h3>Estadísticas Generales</h3>
                {basicStats.map((stat, index) => (
                    <div key={index} style={{ marginBottom: '16px' }}>

                        <p>
                            {stat.local} - {stat.label} - {stat.visitor}
                        </p>
                    
                    </div>
                ))}

                <h3>Estadísticas de Porcentaje</h3>
                {basicStatsPct.map((stat, index) => (
                <div key={index} style={{ marginBottom: '16px' }}>
                    {/* Aquí envolvemos el label y las barras dentro de un solo div */}
                    <p>{stat.label}</p>

                    <div style={{ display: 'flex', alignItems: 'center' }}>
                    <div style={{ marginRight: '8px', flex: 1 }}>
                        <LinearStatBar value={stat.local} />
                    </div>

                    <div style={{ marginLeft: '8px', flex: 1 }}>
                        <LinearStatBar value={stat.visitor} />
                    </div>
                    </div>
                </div>
                ))}
            </div>
        </>
    );

}
export default ShowBasicStats;