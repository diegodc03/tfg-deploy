
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers_dto.serializers import MatchPlayersScoreSerializer

from ..models.match_players_score import MatchPlayerScore

from ..models import MatchStatistics




# Endpoint que va a llevar a cabo el envio de todas las tablas del partido
# Tendra una opción de solo enviar una tabla o todas las tablas



class GetStatsScoreFilteredPlayerView(APIView):
    
    def get(self, request):
    
        def is_valid_int(value):
            return value is not None and value.isdigit()
        def is_valid_str(value):
            return isinstance(value, str) and value.strip() != ''
    
        match_id = request.query_params.get('match_id', None)
        player_id = request.query_params.get('player_id', None)
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        errores = {}
        
        # Validar match_id (obligatorio)
        if not match_id or not is_valid_int(match_id):
            errores['match_id'] = "El parámetro 'match_id' es obligatorio y debe ser un número."
        if not player_id or not is_valid_int(player_id):
            errores['player_id'] = "El parámetro 'player_id' debe ser un número."
            
        if errores:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errores": errores}
            
        else:
            
            # Aqui se va a buscar el partido, se filtrará luego el match_statistics uqe tiene el player_id junto al match_id
            player_stat = MatchStatistics.objects.filter(
                match_id__match_id=int(match_id),
                player_id__player_id=int(player_id)
            ).first()
            
            if not player_stat:
                response_data = {"error": "No se encontraron estadísticas para este jugador en el partido."}
                response_status = status.HTTP_404_NOT_FOUND
            
            else:
                
                # Lo siguiente es recoger las puntuaciones del jugador
                scores = MatchPlayerScore.objects.filter(
                    match_player_id__estadistica_id=player_stat.estadistica_id
                )
                
                if not scores.exists():
                    response_data = {"error": "No se encontraron puntuaciones para este jugador en el partido."}
                    response_status = status.HTTP_404_NOT_FOUND
                else:
                    # Serializar los datos de las puntuaciones
                    serializer = MatchPlayersScoreSerializer(scores, many=True)
                    response_data = serializer.data
                    response_status = status.HTTP_200_OK
                    print("scores", scores)

        return Response(response_data, status=response_status)
                
                