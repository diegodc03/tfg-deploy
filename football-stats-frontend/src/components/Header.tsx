import {useState} from 'react';

import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Button,
  Stack,
  Drawer,
  List,
  ListItemButton,
  ListItemText,
  Box,
  Container,
} from '@mui/material';
import LocalLibraryIcon from '@mui/icons-material/LocalLibrary';
import SportsSoccerIcon from '@mui/icons-material/SportsSoccer';
import { Link } from 'react-router-dom';





export default function Header() {

  const [drawerOpen, setDrawerOpen] = useState(false);

  const handleDrawerToggle = () => {
    setDrawerOpen(!drawerOpen);
  };

  const menuItems = ['Inicio', 'Buscar Partidos', 'Contacto', 'Documentacion TFG', ];



    return (
      <>
      <AppBar position="static" sx={{ backgroundColor: '#f8f9fa', color: 'black',  position: 'fixed', top: 0, width: '100%', height: '64px', zIndex: 1000 }}>
        <Container maxWidth="lg">
          <Toolbar >
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 1, ml:10 }}
            >
              <SportsSoccerIcon />
            </IconButton>
            <Typography
              variant="h6"
              component="div"
              sx={{ flexGrow: 1, display: { xs: 'flex', md: 'flex', fontWeight: 'bold'  } }}
            >
              Player And Teams FootBall Stats
            </Typography>

            {/* Menú horizontal visible en pantallas grandes */}
            <Stack
              direction="row"
              justifyContent="right"
              spacing={2}
              sx={{ display: { xs: 'none', md: 'flex' }, flexGrow: 1, mr: 10 }}
            >
              
              <Button variant="contained" color="inherit" sx={{ fontWeight: 'bold' }}>
                <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                  Inicio
                </Link>
              </Button>
              <Button variant="contained" color="inherit" sx={{ fontWeight: 'bold' }}>
                <Link to="filter-by-season-and-league" style={{ textDecoration: 'none', color: 'inherit' }}>
                  Buscar Partidos
                </Link>
              </Button>
              
              <Button variant="contained" color="inherit" sx={{ fontWeight: 'bold' }}>
                <Link to="tfg-docs" style={{ textDecoration: 'none', color: 'inherit' }}>
                  Documentación TFG
                </Link>
              </Button>
              
              <Button variant="contained" color="inherit" sx={{ fontWeight: 'bold' }}>
                <Link to="about" style={{ textDecoration: 'none', color: 'inherit' }}>
                  Sobre Nosotros
                </Link>
              </Button>


            </Stack>

            {/* Botón para abrir Drawer en móviles */}
            <IconButton
              size="large"
              edge="end"
              color="inherit"
              sx={{ display: { xs: 'flex', md: 'none' } }}
              onClick={handleDrawerToggle}
            >
              <LocalLibraryIcon />
            </IconButton>
          </Toolbar>
        </Container>
        
      </AppBar>

      {/* Drawer para móviles */}
      <Drawer anchor="right" open={drawerOpen} onClose={handleDrawerToggle}>
        <Box sx={{ width: 250 }} role="presentation" onClick={handleDrawerToggle}>
          <List>
            {menuItems.map((item) => (
              <ListItemButton key={item}>
              <ListItemText primary={item} />
            </ListItemButton>
            ))}
          </List>
        </Box>
      </Drawer>
    </>
    );
  }