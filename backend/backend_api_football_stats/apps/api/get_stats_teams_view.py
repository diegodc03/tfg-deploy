
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers_dto.avg_teams_stats_serializers import AngAvgTeamsStatsByBasicPositionsSerializer

from ..models import FootballMatch
from ..models import MatchStatistics

from ..constants.constants import model_map_serializer
from ..models import AvgTeamsStats


# Endpoint que va a llevar a cabo el envio de las estadisticas de los equipos de un partido
# GET /api/stats/getTeamsStats/?league_id=1&team_id=1
# GET /api/stats/getTeamsStats/?league_id=1


class GetStatsTeamsUnitaryView(APIView):
    
    def get(self, request):
        
        league_id = request.query_params.get('league_id', None)
        team_id = request.query_params.get('team_id', None)
        type_of_stats = request.query_params.get('type_of_stats', None)
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        if not league_id or not league_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' es obligatorio y debe ser un número."}
        else:
            
            if team_id and not team_id.isdigit():
                response_data = {"error": "El parámetro 'team_id' debe ser un número."}
            
            else:
                
                if team_id:
                    avg_teams_stats = AvgTeamsStats.objects.filter(team_id=int(team_id), league_id=int(league_id)).first()
                    
                else:
                    avg_teams_stats = AvgTeamsStats.objects.filter(league_id=int(league_id)).first()
            
                
                if not avg_teams_stats:
                    response_data = {"error": "No se encontraron estadísticas para este equipo."}
                else:
                    
                    response = AngAvgTeamsStatsByBasicPositionsSerializer(avg_teams_stats, many=False)
                    
                    response_data = response.data
                    response_status = status.HTTP_200_OK
                    
        return Response(response_data, status=response_status)