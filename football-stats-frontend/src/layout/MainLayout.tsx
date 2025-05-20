

import { Outlet } from "react-router-dom";
import Header from "../components/Header";  
import Footer from "../components/Footer";
import { Box } from "@mui/material";

export default function MainLayout() {
    return (
        <>
            <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', overflowY: "auto",  flexGrow: 1 }}>
                <Header />
                <main 
                    style={{
                        marginTop: '64px', // Altura de la barra de navegación
                    }}
                >
                    {/* Aquí se renderizarán las rutas hijas */}
                    {/* <Outlet /> */}
                    <Outlet />
                </main>
                <Footer />

            </Box>

        </>
        
    );
}

