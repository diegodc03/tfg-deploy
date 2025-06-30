import realMadridImg from "../../images/real_madrid.jpg";
import seatingAthClubBilbaoImg from "../../images/stadiums/asientosAthleticClubBilbao.jpg";
import athleticClubBilbaoImg from "../../images/stadiums/athleticClubbilbao.jpg";
import realMadridSeatingImg from "../../images/stadiums/bernabeu.jpg";
import campNouImg from "../../images/stadiums/campNou.jpg";
import wandaMetropolitanoImg from "../../images/stadiums/Bandera_atm.jpg";
import { stadiumName, teamNames } from "./StadiumName";


export interface StadiumColorConfig {
    teamName?: string;
    name: string;
    backGcolor?: string;
    backGButtons?: string;
    textColor: string;
    cardColor?: string; // Color tenue para tarjetas
    image: string;
    whiteCuadrangle?: boolean;

}

export const colorsAsociatedToStadium: StadiumColorConfig[] = [
    {
        teamName: teamNames.REAL_MADRID,
        name: stadiumName.SANTIAGO_BERNABEU,
        backGcolor: "#1976d2", // Azul claro
        backGButtons: "#0752e7", // Azul
        textColor: "#FFFFFF", // Blanco
        cardColor: "#40b9ff", // Azul claro tenue
        image: realMadridImg,
        whiteCuadrangle: true
    },
    {
        teamName: teamNames.FC_BARCELONA,
        name: stadiumName.CAMP_NOU,
        backGcolor: "#7190cd",
        backGButtons: "#5c81ca",
        cardColor: "#5f94e4", // Azul claro tenue
        textColor: "#000000",
        image: campNouImg, 
    },
    {
        teamName: teamNames.ATLETICO_MADRID,
        name: stadiumName.WANDA_METROPOLITANO,
        backGcolor: "#a10000", // Rojo oscuro, más institucional
        backGButtons: "#7a0000", // Rojo más profundo para botones
        cardColor: "#953737", // Rojo tenue para tarjetas
        textColor: "#FFFFFF", // Blanco
        image: wandaMetropolitanoImg,
    },
    {
        teamName: teamNames.ATHLETIC_CLUB,
        name:   stadiumName.SAN_MAMES,
        backGcolor: "#c71e1d", // Rojo Athletic Club Bilbao
        backGButtons: "#8e1b1a", // Rojo más oscuro para botones
        cardColor: "#cd4f4f", // Rojo tenue para tarjetas
        textColor: "#FFFFFF", // Blanco
        image: seatingAthClubBilbaoImg,
    },
    {
        teamName: teamNames.ATHLETIC_CLUB,
        name: stadiumName.SAN_MAMES,
        backGcolor: "#c71e1d",
        backGButtons: "#8e1b1a",
        cardColor: "#cd4f4f", // Rojo tenue para tarjetas
        textColor: "#FFFFFF",
        image: athleticClubBilbaoImg,
    },
    {
        teamName: teamNames.REAL_MADRID,
        name: stadiumName.SANTIAGO_BERNABEU,
        backGcolor: "#1976d2", // Azul claro
        backGButtons: "#0752e7", // Azul
        textColor: "#FFFFFF", // Blanco
        cardColor: "#40b9ff", // Azul claro tenue
        image: realMadridSeatingImg, 
        whiteCuadrangle: true
    },
];