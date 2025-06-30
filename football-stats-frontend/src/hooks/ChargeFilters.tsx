// src/hooks/useChargeAllFilters.ts
import { useEffect, useState } from 'react';
import { ERROR_MESSAGES } from '../model/constants/errorConstants';
import { STORAGE_KEYS } from '../model/constants/StorageKeys';
import { API_ENDPOINTS } from '../model/constants/UrlConstants';

    // useChargeAllFilters.ts

export const useChargeAllFilters = () => {
    const [showError, setShowError] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchAndStoreAllFilters = async () => {
            console.log("Cargando todos los filtros...");
            setIsLoading(true);
        try {
            await Promise.all([
            fetchAndStore(API_ENDPOINTS.ALL_SEASONS, STORAGE_KEYS.seasons),
            fetchAndStore(API_ENDPOINTS.ALL_LEAGUES, STORAGE_KEYS.leagues),
            fetchAndStore(API_ENDPOINTS.ALL_SEASON_TOURNAMENTS, STORAGE_KEYS.season_tournaments),
            fetchAndStore(API_ENDPOINTS.ALL_BASIC_POSITIONS, STORAGE_KEYS.basicPositions),
            fetchAndStore(API_ENDPOINTS.ALL_SPECIFIC_POSITIONS, STORAGE_KEYS.specificPositions),
            fetchAndStore(API_ENDPOINTS.ALL_GAME_MODES, STORAGE_KEYS.gameModes),
            ]);
        } catch (error) {
            setErrorMessage(ERROR_MESSAGES.NOT_FOUND_FILTERS);
            setShowError(true);
        } finally {
            console.log("Todos los filtros cargados.");
            setIsLoading(false);
        }
        };

        fetchAndStoreAllFilters();
    }, []);

    const fetchAndStore = async (url: string, storageKey: string) => {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Error fetching from ${url}`);
        const data = await response.json();
        localStorage.setItem(storageKey, JSON.stringify(data));
    };

    return { showError, setShowError, errorMessage, isLoading };
};
