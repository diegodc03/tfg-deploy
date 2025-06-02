

/**
 * Este componente lo que hace es coger las estadísticas de un partido, y se va a comparar según los jugadores de cada tipo de posicion basica
 * Es decir, se tienen todas las estadísticas de los jugadores, y se comparan entre ellos según su posición
 * 
 * El objetivo es que el usuario pueda ver las estadísticas de un partido, y ver como han jugado los jugadores según su posición 
*/

import { useState, useEffect, useRef } from 'react';
import Chart, { ChartTypeRegistry } from 'chart.js/auto';
import axios from 'axios';
import { ChartType, StatEntry } from '../../model/statsTypes/stats';
import { ReusableChart } from '../../components/charts/reusableChart';
import { StatsList } from '../../components/charts/StatsList';
import { useParams } from 'react-router-dom';
import { TablesStats } from '../../model/tablesStats/TablesStats';
import { Stats } from '../../model/statsTypes/StatsModel';
import { Box, Container, Stack } from '@mui/material';
import realMadridImg from '../../images/real_madrid.jpg';


export const ShowStatsChartFromMatch = () => {

  const [isLoading, setIsLoading] = useState(true);
  const { match_id } = useParams();

  const [stats, setStats] = useState<Stats>([]);
  const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
  const [selectedFilters, setSelectedFilters] = useState<String>('');

    const [opciones, setOpciones] = useState<any[]>([]);
    const [tabla, setTabla] = useState('');
    const [columna, setColumna] = useState('');
    const [valores, setValores] = useState<number[]>([]);
    const [tipoGrafico, setTipoGrafico] = useState<ChartType>('bar');
    const [labels, setLabels] = useState<string[]>([]);
    const [statsEntryList, setStatsEntryList] = useState<StatEntry[]>([null]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {

        
        const [responseStats, responseFilters] = await Promise.all([
          fetch(`http://localhost:8000/api/chart/statsPlayersMatchBasic/?match_id=${match_id}`),
          fetch('http://localhost:8000/api/filter/filtersUnitaryPlayerMatchChart/')
        ]);

        if (!responseStats.ok || !responseFilters.ok) {
          throw new Error('Error fetching data');
        }

        const [statsData, filtersData] = await Promise.all([
          responseStats.json(),
          responseFilters.json()
        ]);

        console.log('Datos de las estadísticas de los jugadores:', statsData);
        console.log('Datos de los filtros de las tablas:', filtersData);

        setStats(statsData);
        setFiltersArray(filtersData);
        setIsLoading(false);          

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
    

  return (


    <Box
              sx={{
                  backgroundImage: `url(${realMadridImg})`,
                  backgroundRepeat: 'no-repeat',
                  backgroundAttachment: 'fixed',
                  backgroundSize: 'cover',
                  minHeight: '100vh',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  
              }}>

      <Container>
        <Stack  sx={{marginTop: 6,  backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
          <StatsList name={columna} stats={stats} typeOfChart={'bar'}  />
        </Stack>
      </Container>
    
    </Box>
  );
};



  {
    /*
    <div style={{ display: 'flex', gap: '1rem' }}>
          <select onChange={e => {
            const t = e.target.value;
            setTabla(t);
            const columnas = opciones.find(o => o.tabla === t)?.columnas || [];
            setColumna(columnas[0]);
          }} value={tabla}>
            {opciones.map(opt => (
              <option key={opt.tabla} value={opt.tabla}>{opt.tabla}</option>
            ))}
          </select>
  
          <select onChange={e => setColumna(e.target.value)} value={columna}>
            {(opciones.find(o => o.tabla === tabla)?.columnas || []).map(col => (
              <option key={col} value={col}>{col}</option>
            ))}
          </select>
  
          <select onChange={e => setTipoGrafico(e.target.value as ChartType)} value={tipoGrafico}>
            <option value="bar">Barras</option>
            <option value="line">Línea</option>
            <option value="pie">Tarta</option>
            <option value="doughnut">Dona</option>
            <option value="radar">Radar</option>
          </select>
        </div>
    */
  }