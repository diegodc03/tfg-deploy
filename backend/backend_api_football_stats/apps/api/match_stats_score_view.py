from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend_api_football_stats.apps.serializers_dto.serializers import MatchPlayersScoreSerializer

from ..models import MatchPlayerScore


#GET /api/match-stats-score/?match_id=1
#GET /api/match-stats-score/?match_id=1&basic_position=1
#GET /api/match-stats-score/?match_id=1&specific_position=1
#GET /api/match-stats-score/?match_id=1&game_mode=1

#GET /api/match-stats-score/?match_id=1&basic_position=1&specific_position=1
#GET /api/match-stats-score/?match_id=1&basic_position=1&game_mode=1
#GET /api/match-stats-score/?match_id=1&specific_position=1&game_mode=1

#GET /api/match-stats-score/?match_id=1&basic_position=1&specific_position=1&game_mode=1

class MatchStatsScoreView(APIView):
    
    def get(self, request):
    
        # match_id
        match_id = request.query_params.get('match_id', None)
        # basic_position
        basic_position_id = request.query_params.get('basic_position', None)
        # specific_position
        specific_position_id = request.query_params.get('specific_position', None)
        # game_mode
        game_mode_id = request.query_params.get('game_mode', None)
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        parametros = {
            'basic_position_id': basic_position_id,
            'specific_position_id': specific_position_id,
            'game_mode_id': game_mode_id,
        }
        
        print(f"Parametros: {parametros}")
        
        # No existen filtros, devuelve todas las ligas
        if not match_id or not match_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' debe ser un número."}
            response_status = status.HTTP_400_BAD_REQUEST
        
        else:    
            
            for key, value in parametros.items():
                if value and not value.isdigit():
                    response_data = {"error": f"El parámetro '{key}' debe ser un número."}
                    response_status = status.HTTP_400_BAD_REQUEST
                    break
            
            match_stats = MatchPlayerScore.objects.filter(match_player_id__match_id__match_id=match_id)
            
            for key, value in parametros.items():
                if value:
                    if key in ['basic_position_id', 'specific_position_id', 'game_mode_id']:
                        value = int(value)
                        match_stats = match_stats.filter(**{key: value})
                
            if not match_stats:
                response_data = {"error": "Not found stats for this match_id"}
                response_status = status.HTTP_204_NO_CONTENT
                
            else:
                
                serializer = MatchPlayersScoreSerializer(match_stats, many=True)
                response_data = serializer.data
                
        return Response(response_data, status=response_status)