import { useEffect } from "react";
import { MatchAPI } from "../model/MatchAPI";




const STORAGE_KEYS = {
  results: 'unique_results',
  teams: 'unique_teams',
  weeks: 'unique_weeks'
};


export const chargeAllFilters = () => {




    useEffect(() => {
        const fetchAndStoreFilters = async () => {
            try {
                const response = await fetch("http://localhost:7654/matches");
                const matches: MatchAPI[] = await response.json();

                const { results, teams, weeks } = extractAllUniqueFilters(matches);
                saveToStorage('unique_results', results);
                saveToStorage('unique_teams', teams);
                saveToStorage('unique_weeks', weeks);
            } catch (error) {
            console.error("Error al cargar filtros:", error);
            }
        };

        fetchAndStoreFilters();
        }, []);



    const saveToStorage = (key: string, data: string[]) => {
        localStorage.setItem(key, JSON.stringify(data));
    };



    interface UniqueFilters {
        results: string[];
        teams: string[];
        weeks: string[];
    }

    const extractAllUniqueFilters = (matches: MatchAPI[]): UniqueFilters => {
    const resultSet = new Set<string>();
    const teamSet = new Set<string>();
    const weekSet = new Set<string>();

    matches.forEach(match => {
        resultSet.add(match.Score);
        teamSet.add(match.Home.team_name);
        teamSet.add(match.Away.team_name);
        weekSet.add(match.Wk.toString());
    });

    return {
        results: Array.from(resultSet),
        teams: Array.from(teamSet),
        weeks: Array.from(weekSet),
    };
    };



}






