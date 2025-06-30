// StadiumContext.tsx
import { createContext, useContext, useState } from 'react';

import { colorsAsociatedToStadium } from '../model/constants/ColorSystemAndBackground';

const StadiumContext = createContext(null);

export const StadiumProvider = ({ children }) => {
    const [electedStadium, setElectedStadium] = useState(0);
    const selected = colorsAsociatedToStadium[electedStadium];

    return (
        <StadiumContext.Provider value={{ electedStadium, setElectedStadium, selected }}>
        {children}
        </StadiumContext.Provider>
    );
};

export const useStadium = () => useContext(StadiumContext);
