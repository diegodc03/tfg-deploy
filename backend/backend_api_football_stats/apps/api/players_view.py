from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import FootballMatch
from ..models import MatchStatistics
from ..models import Player

class PlayersView(APIView):

    
    def get(self, request):
        
        match_id = request.query_params.get('match_id', None)
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        if match_id is None or not match_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' es obligatorio y debe ser un número."}
            
        else:
            
            football_match = FootballMatch.objects.filter(match_id=int(match_id)).first()
            
            if not football_match:
                response_data = {"error": "No se encontró el partido."}
            else:
                # Aquí puedes agregar la lógica para obtener los jugadores del partido
                # Por ejemplo, si tienes un modelo Player relacionado con FootballMatch
                match_statistics = MatchStatistics.objects.filter(match_id__match_id=int(match_id))
                if not match_statistics:
                    response_data = {"error": "No se encontraron estadísticas para este partido."}
                else:
                    
                    # Teniendo las stats, ahora unicamente hay que hacer un for de cada jugador, meter el nombre con el id y luego la puntuacion para el tipo de jugador
                    players_data = {}
                    
                    for player_stat in match_statistics:
                        player_id = player_stat.player_id.player_id
                        
                        if player_id not in players_data:

                            player = Player.objects.filter(player_id=player_id).first()
                            if player:
                                players_data[player.player_id] = {
                                    'name': player.player_name,
                                }
                    
                    response_data = [
                        {
                            "player_id": player_id,
                            "name": player_data['name'],
                        }
                        for player_id, player_data in players_data.items()
                    ]
                    
                    
                    response_status = status.HTTP_200_OK                                
        return Response(response_data, status=response_status)
                
                            
         
        
        
