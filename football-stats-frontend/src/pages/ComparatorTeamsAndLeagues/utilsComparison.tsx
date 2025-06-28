import { ChartAPI } from "../../model/ChartsAPI/ChartAPI";
import { ChartType, StatEntry } from "../../model/statsTypes/stats";

const chartType: ChartType = 'bar';


export const generateScoreValuesChart = (chartData: ChartAPI[], selectColumn: string): StatEntry => {
            
    let players_labels: Set<string> = new Set();
    let data: number[] = [];
    
    for (let i = 0; i < chartData.length; i++) {
        let valueStat = chartData[i].value

        data.push(valueStat);
        if (chartData[i].league_year && chartData[i].starter_status) {
            let label = `${chartData[i].league_year} - ${chartData[i].starter_status}`;
            players_labels.add(label);
        }
    }

    return {
        title: selectColumn ? `Estadísticas de ${selectColumn}` : 'Estadísticas de los jugadores',
        labels: Array.from(players_labels),
        data,
        type: chartType,
    };
}