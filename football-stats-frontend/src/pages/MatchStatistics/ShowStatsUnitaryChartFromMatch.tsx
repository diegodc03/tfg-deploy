

/**
 * Este componente lo que hace es coger las estadísticas de un partido, y se va a comparar según los jugadores de cada tipo de posicion basica
 * Es decir, se tienen todas las estadísticas de los jugadores, y se comparan entre ellos según su posición
 * 
 * El objetivo es que el usuario pueda ver las estadísticas de un partido, y ver como han jugado los jugadores según su posición 
*/

import { useState, useEffect, useRef } from 'react';

import { StatsList } from '../../components/charts/StatsList';
import { useParams } from 'react-router-dom';
import { TablesStats } from '../../model/tablesStats/TablesStats';
import { Stats } from '../../model/statsTypes/StatsModel';
import { Box, Button, Container, Grid, Stack, Typography } from '@mui/material';
import GenericSelectProps from '../../components/MultipleSelect';
import { BasicPositionAPI } from '../../model/BasicPositionAPI';
import { API_ENDPOINTS } from '../../model/constants/UrlConstants';
import ErrorSnackbar from '../../components/showError';
import { ERROR_MESSAGES } from '../../model/constants/errorConstants';
import { positionTranslation } from '../../model/constants/Translate';


export const ShowStatsChartFromMatch = () => {

  const [isLoading, setIsLoading] = useState(true);
  const [showError, setShowError] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  
  const { match_id } = useParams();

  const [stats, setStats] = useState<Stats>([]);

  const [filtersArray, setFiltersArray] = useState<TablesStats[]>([]);
  const [selectedFiltersTable, setSelectedFilterTable] = useState<string>('');


  const [basicPositions, setBasicPositions] = useState<BasicPositionAPI[]>([]);
  const [basicPositionElement, setBasicPositionElement] = useState<string>('');


  const [columna, setColumna] = useState('');

  const dictOfTables: string = "&type_table_stats=";
  const typeOfBasicPosition: string = "&basic_position="; // This can be dynamic based on user selection or other logic

  
  let baseurl: string = API_ENDPOINTS.STATS_PLAYERS_MATCH_BY_BASIC_POSITION_AND_ORDER_STATS + `${match_id}`;
  
  useEffect(() => {
    const fetchData = async () => {
      try {

        
        const [responseStats, responseFilters, responseBasicPositions] = await Promise.all([
          fetch(API_ENDPOINTS.STATS_PLAYERS_MATCH_BY_BASIC_POSITION_AND_ORDER_STATS + `${match_id}`),
          fetch(API_ENDPOINTS.FILTER_TABLES_ORDER_STATS_OF_MATCH),
          fetch(API_ENDPOINTS.ALL_BASIC_POSITIONS),
        ]);

        if (!responseStats.ok || !responseFilters.ok || !responseBasicPositions.ok) {
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
        setSelectedFilterTable(filtersArrayTransform[0]?.categoryName || ''); 
        setIsLoading(false); 
        
        
      } catch (error) {
        setErrorMessage(ERROR_MESSAGES.NOT_FOUND_MATCHES_ON_LEAGUE);
        setShowError(true);
        setIsLoading(false);
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

      <Container maxWidth="lg" sx={{ marginTop: '3rem', marginBottom: '5vh' }}>

        <ErrorSnackbar
            open={showError}
            onClose={() => setShowError(false)}
            message={errorMessage ?? "Ha ocurrido un error inesperado"}
            position={{ vertical: 'top', horizontal: 'right' }}
            large={true}
        />

        <Box
          sx={{
              backgroundColor: '#f8f9fa',
              borderRadius: 4,
              boxShadow: 2,
              overflow: 'hidden',
              marginBottom: 5,
              
          }}
        >
          <Box
              sx={{
                  backgroundColor: '#ffffff',
                  padding: 2,
                  paddingBottom:0,
                  paddingLeft: 3,
              }}
          >
              <Typography>
                  <strong>Filtros</strong>
              </Typography>
          </Box>

          <Grid 
            container
            spacing={{ xs: 1, sm: 2, md: 4 }}
            
            justifyContent="center"
            sx={{
                backgroundColor: '#f8f9fa',
                padding: 2,
                borderRadius: 4,
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
                        labelTodosShow={false}
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
                      getLabel={(item) => positionTranslation[item.category_name] ?? item.category_name}
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
        </Box>

           
        <Stack
          sx={{
            marginTop: 6,
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            borderRadius: 2,
            alignItems: 'center',
            paddingTop: 5,
            width: '100%',
          }}
        >
          <Box sx={{ width: '100%', paddingLeft: 5, paddingRight:5, paddingTop: 2, alignItems: 'center' }}>
            <StatsList name={columna} stats={stats} typeOfChart={'bar'} />
          </Box>
        </Stack>

        
      </Container>
  );
};

         
