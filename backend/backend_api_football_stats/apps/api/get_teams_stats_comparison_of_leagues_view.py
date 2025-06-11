
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers_dto.avg_teams_stats_serializers import AngAvgTeamsStatsByBasicPositionsSerializer
from ..constants.constants import stats_columns_team
from ..models import FootballMatch
from ..models import MatchStatistics
from ..models import AvgTeamsStats
from ..models.team import Team
from ..models import Tournament
from ..models import Season
# Endpoint que va a llevar a cabo el envio de las estadisticas de los equipos de un partido
# GET /api/stats/getTeamsStats/?league_id=1&team_id=1
# GET /api/stats/getTeamsStats/?league_id=1


class GetStatsTeamsComparisonOfLeaguesView(APIView):
    
    def get(self, request):
        
        team_name = request.query_params.get('team_name', None)
        type_of_stats = request.query_params.get('type_of_stats', None)
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        errors = {}
        
        if not team_name or not isinstance(team_name, str):
            errors['team_id'] = "El parámetro 'team_name' debe ser un str."
        
        if not type_of_stats or type_of_stats not in stats_columns_team:
            errors['type_of_stats'] = "El parámetro 'type_of_stats' es obligatorio y debe ser 'basic' o 'advanced'."
            
        if errors:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errors": errors}
            
        else:
                
            
                
            teams = Team.objects.filter(team_name=team_name)
            if not teams:
                response_data = {"error": "No se encontró el equipo con el nombre proporcionado."}
                return Response(response_data, status=response_status)
            else:
                
                teams_list = list(teams)
                
                teams_response = {}
                
                teams_ids = []
                for team in teams_list:
                        teams_ids.append(team.team_id)
                        print(team.team_id)
                
                
                for team_id in teams_ids:

                    avg_teams_stats = AvgTeamsStats.objects.filter(team_id=int(team_id)).values_list(
                            "league_id", "team_id", "starter_status", *stats_columns_team[type_of_stats],
                        )
                    
                    if not avg_teams_stats:
                        response_data = {"error": "No se encontraron estadísticas para este equipo."}
                    else:
                        
                        
                        param_list = list(avg_teams_stats)
                        print(param_list)
                        
                        dict_keys = ["league_year", "team_name", "starter_status"] + list(stats_columns_team[type_of_stats])
                        response_elements = []
                        for players_stats in param_list:
                            
                            league_entity = Tournament.objects.filter(tournament_id=players_stats[0]).first()
                            
                            if not league_entity:
                                response_data = {"error": "No se encontró la liga con el ID proporcionado."}
                                return Response(response_data, status=response_status)
                            else: 
                                
                                players_stats = list(players_stats)
                                players_stats[0] = league_entity.nombre_liga
                                players_stats[1] = team.team_name

                            players_stats_dict = dict(zip(dict_keys, players_stats))
                            response_elements.append(players_stats_dict)

                        teams_response[league_entity.season_tournament.season_year] = response_elements
                        
                response_data = teams_response
                response_status = status.HTTP_200_OK
                    
        return Response(response_data, status=response_status)