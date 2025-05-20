

/**
 * Este archivo va a encargar de comparar las estadísticas de cada temporada
 * 
 * Se tiene una lista de estadísticas totales por temporada, y se va a comparar cada una de ellas
 * 
 * Tambien se va a comparar por temporada  y posiciones, es decir, se va a comparar cada una de las estadísticas de cada jugador por su posición
 * 
 * Tambien se va a comparar por equipo, es decir, se va a comparar las estadísticas de un jugador por su equipo
 */


import { Box } from "@mui/material";
import React from "react";
import { PlayerStatGroup } from "../../model/statsTypes/stats";

export default function ShowStatsComparisonFromLeague() {

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', mt: 10 }}>
            <h1>Comparativa de estadísticas de la liga</h1>
            <p>En esta sección se comparan las estadísticas de los jugadores de la liga.</p>
        </Box>
    );

}