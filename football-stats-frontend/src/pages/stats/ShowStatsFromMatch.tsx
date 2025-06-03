

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
import { Box, Button, Container, Grid, Stack, Typography } from '@mui/material';
import realMadridImg from '../../images/real_madrid.jpg';
import GenericSelectProps from '../../components/MultipleSelect';
import { BasicPositionAPI } from '../../model/BasicPositionAPI';


export const ShowStatsChartFromMatch = () => {

  const [isLoading, setIsLoading] = useState(true);
  const { match_id } = useParams();

  const [stats, setStats] = useState<Stats>([]);
  const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
  const [selectedFiltersTable, setSelectedFilterTable] = useState<string>('');


  const [basicPositions, setBasicPositions] = useState<BasicPositionAPI[]>([]);
  const [basicPositionElement, setBasicPositionElement] = useState<string>('');


  const [columna, setColumna] = useState('');

  const dictOfTables: string = "&type_table_stats=";
  const typeOfBasicPosition: string = "&basic_position="; // This can be dynamic based on user selection or other logic

  let baseurl: string = `http://localhost:8000/api/chart/statsPlayersMatchBasic/?match_id=${match_id}`;
  
  useEffect(() => {
    const fetchData = async () => {
      try {

        
        const [responseStats, responseFilters, responseBasicPositions] = await Promise.all([
          fetch(`http://localhost:8000/api/chart/statsPlayersMatchBasic/?match_id=${match_id}`),
          fetch('http://localhost:8000/api/filter/filtersUnitaryPlayerMatchChart/'),
          fetch('http://localhost:8000/api/all-basic-positions/'),
        ]);

        if (!responseStats.ok || !responseFilters.ok) {
          throw new Error('Error fetching data');
        }

        const [statsData, filtersData, filtersBasicPositions] = await Promise.all([
          responseStats.json(),
          responseFilters.json(),
          responseBasicPositions.json()
        ]);


        const filtersArrayTransform: TablesStats[] = Object.entries(filtersData).map(([key, value]) => ({
          categoryName: key,
          categoryDescription: String(value),
        }));

        setStats(statsData);
        setFiltersArray(filtersArrayTransform);
        setBasicPositions(filtersBasicPositions);
        setSelectedFilterTable(filtersArrayTransform[0]?.categoryName || ''); // Set default filter if available
        setIsLoading(false); 
        
        
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();

  }, [match_id]);
    
  const handleChangeSelectedTableFilters = (value: string) => {
    setSelectedFilterTable(value);
  }

  const handleChangeSelectedBasicPosicionsFilters = (value: string) => {
    setBasicPositionElement(value);
  }


  const handleFilter = async () => {

    if (selectedFiltersTable !== "Todos") {
      baseurl += dictOfTables + selectedFiltersTable;
    }

  
    if (basicPositionElement !== "Todos") {
      baseurl += typeOfBasicPosition + basicPositionElement;
    }

    const response = await fetch(baseurl);
    if (!response.ok) {
      throw new Error('Error fetching filtered stats');
    }
    setIsLoading(true);
    const data = await response.json();
    setStats(data);
    setIsLoading(false);
  }

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

      <Grid 
        container
        columnSpacing={{ xs: 1, sm: 2 }}
        rowSpacing={{ xs: 1, sm: 2, md: 3 }}
        spacing={{ xs: 1, sm: 2, md: 4 }}
        
        justifyContent="center"
        sx={{
            backgroundColor: '#f8f9fa',
            padding: 2,
            borderRadius: 2,
            marginTop: 1,
            marginBottom: 5,
        }}
      >
        <Grid  size={{xs:12, md:5}}>
            <Typography>
                <strong>Tablas a consultar</strong>
            </Typography>
            <div>
                
                <GenericSelectProps<TablesStats>
                    items={filtersArray}
                    value={selectedFiltersTable || ""}
                    onChange={handleChangeSelectedTableFilters}
                    getId={(item) => item.categoryName}
                    getLabel={(item) => item.categoryDescription}
                />
            </div>
        </Grid>

        <Grid  size={{xs:12, md:5}}>
            <Typography>
                <strong>Tipos de posiciones</strong>
            </Typography>
            <div>  
                <GenericSelectProps<BasicPositionAPI>
                  items={basicPositions}
                  value={basicPositionElement || ""}
                  onChange={handleChangeSelectedBasicPosicionsFilters}
                  getId={(item) => String(item.category_id)}
                  getLabel={(item) => item.category_name}
              />
            </div>
        </Grid>

        <Grid size={{xs:12,md:2}} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 3 }}>
          <Button
                  variant="contained"
                  color="primary"
                  fullWidth
                  onClick={handleFilter}
              >
              Filtrar
          </Button>
        </Grid>
        
      </Grid>
        

      <Container>
        <Stack  sx={{marginTop: 6,  backgroundColor: 'rgba(255, 255, 255, 0.9)', borderRadius: 2, padding: 10 }} >
          <StatsList name={columna} stats={stats} typeOfChart={'bar'}  />
        </Stack>
      </Container>
    
    </Box>
  );
};

