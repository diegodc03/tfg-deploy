

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



export const ShowStatsFromMatch = () => {
    const [opciones, setOpciones] = useState<any[]>([]);
    const [tabla, setTabla] = useState('');
    const [columna, setColumna] = useState('');
    const [valores, setValores] = useState<number[]>([]);
    const [tipoGrafico, setTipoGrafico] = useState<ChartType>('bar');
    const [labels, setLabels] = useState<string[]>([]);
    const [statsEntryList, setStatsEntryList] = useState<StatEntry[]>([null]);
  
    useEffect(() => {
      axios.get('http://localhost:8000/api/estadisticas/opciones/')
        .then(res => {
          setOpciones(res.data);
          if (res.data.length > 0) {
            setTabla(res.data[0].tabla);
            setColumna(res.data[0].columnas[0]);
          }
        });
    }, []);
  
    useEffect(() => {
      if (!tabla || !columna) return;
  
      axios.get(`http://localhost:8000/api/estadisticas/?tabla=${tabla}&columna=${columna}`)
        .then(res => {
          setValores(res.data.valores);
          setLabels(res.data.labels || res.data.valores.map((_: any, i: number) => `Item ${i + 1}`));
        });
    }, [tabla, columna]);


    useEffect(() => {
  
      axios.get(`http://localhost:8000/api/estadisticas/todas`)
        .then(res => {
          const stats = res.data.map((stat: any) => ({
            title: stat.title,
            labels: stat.labels,
            data: stat.data,
            type: stat.type || 'bar',
          }));
          setStatsEntryList(stats);
        });
    }
    , [tabla, columna]);
        
  

  
    return (
      <div>
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
  
        <div style={{ marginTop: '2rem', maxWidth: '800px' }}>
  
          {/* <ReusableChart stat={statEntry} />*/}

          <StatsList name={columna} stats={statsEntryList} />
        </div>
      </div>
    );
  };