


// Representa una estadística que se mostrará en un gráfico
export type StatEntry = {
        player_id: number;        // Ej: 123
        player_name: string;     // Ej: "Karim Benzema"
        value: number;       // Ej: 500
        basic_position: string; // Ej: "delantero"
        basic_position_id: number; // Ej: 1
        is_home: boolean;       // Ej: true (si es el equipo local)
        team_name: string;      // Ej: "Real Madrid"

    };

    
// Si quieres comparar muchas estadísticas de un equipo/jugador
export type StatValues = {
    stat: string;              // Nombre de la estadística 
    values: StatEntry[];        // Array de los jugadores y sus estadísticas, esto es un array con cada jugador y su estadística
};

export type Stats = StatValues[];