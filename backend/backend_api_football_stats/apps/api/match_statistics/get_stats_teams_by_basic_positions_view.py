
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...models import FootballMatch
from ...models import MatchStatistics

from ...constants.constants import model_map_serializer



# Endpoint que va a llevar a cabo el envio de las estadisticas de los equipos de un partido
# GET /api/getTeamsStats/?league_id?basic_position=1
# GET /api/getStatsTeamS/?league_id=1&team_id=1?basic_position=1



class GetStatsTeamsUnitaryBasicView(APIView):
    
    def get(self, request):
        
        match_id = request.query_params.get('match_id', None)

        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        if not match_id or not match_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' es obligatorio y debe ser un número."}
    
        else:
            football_match = FootballMatch.objects.filter(match_id=int(match_id)).first()
            if not football_match:
                response_data = {"error": "No se encontró el partido."}
            else:
                match_statistics = MatchStatistics.objects.filter(football_match=football_match)
                
                if not match_statistics:
                    response_data = {"error": "No se encontraron estadísticas para este partido."}
                else:
                    serializer = model_map_serializer['MatchStatisticsSerializer'](match_statistics, many=True)
                    response_data = serializer.data
                    response_status = status.HTTP_200_OK
        
        