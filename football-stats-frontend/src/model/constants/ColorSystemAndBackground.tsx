import realMadridImg from "../../images/real_madrid.jpg";
import seatingAthClubBilbaoImg from "../../images/stadiums/asientosAthleticClubBilbao.jpg";
import athleticClubBilbaoImg from "../../images/stadiums/athleticClubbilbao.jpg";
import realMadridSeatingImg from "../../images/stadiums/bernabeu.jpg";
import campNouImg from "../../images/stadiums/campNou.jpg";
import wandaMetropolitanoImg from "../../images/stadiums/Bandera_atm.jpg";



export interface StadiumColorConfig {
    name: string;
    backGcolor?: string;
    backGButtons?: string;
    textColor: string;
    image: string;
    whiteCuadrangle?: boolean;

}

export const colorsAsociatedToStadium: StadiumColorConfig[] = [
    {
        name: "Estadio Santiago Bernabéu",
        backGcolor: "#1976d2", // Azul claro
        backGButtons: "#0752e7", // Azul
        textColor: "#FFFFFF", // Blanco
        image: realMadridImg,
        whiteCuadrangle: true
    },
    {
        name: "Estadio Camp Nou",
        backGcolor: "#7190cd",
        backGButtons: "#5c81ca",
        textColor: "#000000",
        image: campNouImg, 
    },
    {
        name: "Estadio Wanda Metropolitano",
        backGcolor: "#a10000", // Rojo oscuro, más institucional
        backGButtons: "#7a0000", // Rojo más profundo para botones
        textColor: "#FFFFFF", // Blanco
        image: wandaMetropolitanoImg,
    },
    {
        name: "Estadio San Mamés",
        backGcolor: "#c71e1d", // Rojo Athletic Club Bilbao
        backGButtons: "#8e1b1a", // Rojo más oscuro para botones
        textColor: "#FFFFFF", // Blanco
        image: seatingAthClubBilbaoImg,
    },
    {
        name: "Estadio San Mamés",
        backGcolor: "#c71e1d",
        backGButtons: "#8e1b1a",
        textColor: "#FFFFFF",
        image: athleticClubBilbaoImg,
    },
    {
        name: "Estadio Santiago Bernabéu",
        backGcolor: "#1976d2", // Azul claro
        backGButtons: "#0752e7", // Azul
        textColor: "#FFFFFF", // Blanco
        image: realMadridSeatingImg, 
        whiteCuadrangle: true
    },
];