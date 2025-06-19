

import { Outlet } from "react-router-dom";
import { useEffect, useState } from 'react';
import Header from "../components/Header";  
import Footer from "../components/Footer";
import { Box, Button } from "@mui/material";
import { colorsAsociatedToStadium } from "../model/constants/ColorSystemAndBackground";
import { useNavigate } from "react-router-dom";



export default function MainLayout() {

    const navigate = useNavigate();
    const [showButtons, setShowButtons] = useState(true);
    const [electedStadium, setElectedStadium] = useState(0);

    const handleChangeColor = () => {
        const nextIndex = (electedStadium + 1) % colorsAsociatedToStadium.length;
        setElectedStadium(nextIndex);
    };

    const handleChangeScoresView = () => {
        if (navigate) {
            console.log("navegando a: helping-page");
            navigate(`helping-page`);   
        }
    };

    const { backGcolor: backgroundColorSelected, image: backgroundImageSelected, backGButtons: secondaryColorSelected, textColor: textColorSelected } = colorsAsociatedToStadium[electedStadium];

    useEffect(() => {
        let lastScrollTop = 0;

        const handleScroll = () => {
            const currentScrollTop = window.scrollY;

            if (currentScrollTop > lastScrollTop) {
                setShowButtons(false);
            } else {
                setShowButtons(true);
            }

            lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop;
        };

        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    
    return (
    <>
        <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', overflowY: "auto", flexGrow: 1 }}>
            
            <Header backGcolor={backgroundColorSelected} backGButtons={secondaryColorSelected} textColor={textColorSelected}/>
            
            <main style={{ marginTop: '64px' }}>
            
            <Box
                sx={{
                backgroundImage: `url(${backgroundImageSelected})`,
                backgroundRepeat: 'no-repeat',
                backgroundAttachment: 'fixed',
                backgroundSize: 'cover',
                minHeight: '100vh',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                }}
            >
                <Button
                    variant="contained"
                    onClick={handleChangeColor}
                    sx={{ margin: 2, backgroundColor: backgroundColorSelected, color: textColorSelected, position: 'fixed', 
                        bottom: 20, left: 20, zIndex: 1000,         
                        opacity: showButtons ? 1 : 0, transition: 'opacity 0.5s ease', 
                        '&:hover': { backgroundColor: secondaryColorSelected } }}
                    >
                    Cambiar Estadio por si no eres del Real Madrid
                </Button>
                <Button
                    variant="contained"
                    onClick={() => {handleChangeScoresView()}}
                    sx={{ margin: 2, backgroundColor: backgroundColorSelected, color: textColorSelected, position: 'fixed', 
                        bottom: 20, right: 20, zIndex: 1000,         
                        opacity: showButtons ? 1 : 0, transition: 'opacity 0.5s ease', 
                        '&:hover': { backgroundColor: secondaryColorSelected } }}
                    >
                    Ayuda de interfaz de usuario 
                </Button>
          
                <Outlet />
            </Box>
            </main>
            <Footer />
        </Box>
    </>
  );

}

