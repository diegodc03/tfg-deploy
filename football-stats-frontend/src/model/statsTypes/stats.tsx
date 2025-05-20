

export type ChartType = "bar" | "radar" | "line" | "pie" | "doughnut";

// Representa una estadística que se mostrará en un gráfico
export type StatEntry = {
        title: string;        // Ej: "Pases completados", "Tiros a puerta"
        labels: string[];     // Ej: ["Madrid", "Barça", "Betis"]
        data: number[];       // Ej: [450, 500, 400]
        type?: ChartType;     // Opcional, por defecto será "bar"
    };
    
    // Si quieres comparar muchas estadísticas de un equipo/jugador
    export type PlayerStatGroup = {
        name: string;              // Nombre del jugador o equipo
        stats: StatEntry[];        // Todas las métricas que quieras mostrar
    };