




import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';


/**
 * 
 * Este componente se va a encargar de mostrar las tablas de las diferentes estadísticas de los jugadores en un partido
 * La intencion es poder filtrar por cada una de las tablas de estadísticas pero tambien poder mostrar todas las statísticas
 * Por último se va a filtrar también por  posicion básica del jugador 
 * 
 * 
 * @returns JSX.Element
 * @description This component is used to show the stats from teams.
 */



export default function ShowStatsOfPlayersOnMatch() {


    const {match_id} = useParams();
    

    


    return (
        <div>
            <h1>Show Stats From Teams</h1>
        </div>
    );
}