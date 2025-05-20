

import React from 'react';
import { useEffect, useState } from 'react';
import { ScoreAPI } from '../model/ScoreAPI';
import { FootballMatchFieldViewAPI } from '../model/FootballMatchFieldViewAPI';


export const FootballField = ({players}: {players: ScoreAPI[]}) => {

    const [startingPlayers, setStartingPlayers] = useState<FootballMatchFieldViewAPI[]>([]);
    const [substitutes, setSubstitutes] = useState<FootballMatchFieldViewAPI[]>([]);
    

    useEffect(() => {
        const start: FootballMatchFieldViewAPI[] = [];
        const substitute: FootballMatchFieldViewAPI[] = [];

        players.map((player) => {
            if (player.match_player_id.minutes > 90) {
                start.push({
                    name: player.match_player_id.player_id.player_name,
                    position: player.basic_position_id.category_name,
                    specific_position: player.specific_position_id.specific_position_name,
                    game_mode: player.game_mode_id.game_mode_name,
                    rating: player.score,
                });
            } else {
                substitute.push({
                    name: player.match_player_id.player_id.player_name,
                    position: player.basic_position_id.category_name,
                    specific_position: player.specific_position_id.specific_position_name,
                    game_mode: player.game_mode_id.game_mode_name,
                    rating: player.score,
                });
            }
    
        });

        setStartingPlayers(start);
        setSubstitutes(substitute);



    },    [players]);

    
    return (

    <div className="flex flex-col items-center gap-4 p-4 font-sans">
        {/* Campo de fútbol */}
        <div className="w-full max-w-[600px] aspect-[2/3] bg-green-700 border-4 border-white rounded-lg relative flex flex-col justify-between p-4">
            {/* Dividimos en 4 líneas */}
            {[...Array(4)].map((_, idx) => (
                <div
                key={idx}
                className="flex justify-center gap-4 w-full border-t border-white py-2"
                >
                {startingPlayers
                    .filter((_, i) => i % 4 === idx) // Simple reparto para el ejemplo
                    .map((player, i) => (
                    <div
                        key={i}
                        className="bg-white text-green-800 text-xs rounded-lg px-2 py-1 text-center shadow"
                    >
                        <div className="font-bold">{player.name}</div>
                        <div>{player.position}</div>
                        <div>⭐ {player.rating}</div>
                    </div>
                    ))}
                </div>
            ))}
        </div>
  
        {/* Suplentes */}
        <div className="w-full max-w-[600px]">
            <h3 className="text-white text-sm mb-2">Suplentes que han jugado:</h3>
            <div className="flex flex-wrap gap-2">
                {substitutes.map((player, i) => (
                <div
                    key={i}
                    className="bg-gray-300 text-gray-800 text-xs rounded px-2 py-1"
                >
                    <div className="font-bold">{player.name}</div>
                    <div>{player.position}</div>
                    <div>⭐ {player.rating}</div>
                </div>
                ))}
            </div>
            </div>
        </div>
    );



}
