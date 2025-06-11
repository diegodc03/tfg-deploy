
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
from ..models import AvgTournamentStats
from ..models import AvgTournamentStatsByBasicPositions
from ..models import AvgTournamentStatsBySpecificPositions
from ..models import Leagues
# Endpoint que va a llevar a cabo el envio de las estadisticas de los equipos de un partido
# GET /api/stats/getTeamsStats/?league_id=1&team_id=1
# GET /api/stats/getTeamsStats/?league_id=1


class GetStatsLeaguesComparison(APIView):
    
    def get(self, request):
        
        league_name = request.query_params.get('team_name', None)
        type_of_stats = request.query_params.get('type_of_stats', None)
        
        response_data = {}
        response_status = status.HTTP_400_BAD_REQUEST
        
        errors = {}
        
        if not league_name or not isinstance(league_name, str):
            errors['team_id'] = "El parámetro 'league_name' debe ser un str y debe existir."
        
        if not type_of_stats or type_of_stats not in stats_columns_team:
            errors['type_of_stats'] = "El parámetro 'type_of_stats' es obligatorio y debe ser 'basic' o 'advanced'."
            
        if errors:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errors": errors}
            
        else:
                
            print(league_name)
            league = Leagues.objects.filter(name=league_name).first()
            if not league:
                response_data = {"error": "No se encontró el equipo con el nombre proporcionado."}
                return Response(response_data, status=response_status)
            else:
                
                tournamets = Tournament.objects.filter(league_id=league)
                
                if not tournamets:
                    response_data = {"error": "No se encontraron torneos para la liga proporcionada."}
                    
                else: 
                    
                    tournament_list = list(tournamets)
                    
                    # iteramos todos los torneos de cada liga
                    for tournament in tournament_list:                        
                        print("tournament list loop", tournament)
                        
                        if tournament.season_tournament is None:
                            response_data = {"error": "El torneo no tiene una temporada asociada."}
                            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
                        
                        avg_tournaments_stats = AvgTournamentStats.objects.filter(league_id=int(tournament.tournament_id)).values_list(
                            "starter_status", *stats_columns_team[type_of_stats],
                        )
                    
                    
                        if not avg_tournaments_stats :
                            response_data = {"error": "No se encontraron estadísticas para este torneo."}
                        else:
                            
                            param_list = list(avg_tournaments_stats)
                            
                            dict_keys = ["starter_status"] + list(stats_columns_team[type_of_stats])

                            response_elements = []
                            for players_stats in param_list:
                                
                                players_stats = list(players_stats)
                                
                                players_stats_dict = dict(zip(dict_keys, players_stats))
                                response_elements.append(players_stats_dict)
                            print("response_elements", response_elements)
                            print("tournament.season_tournament.season_year", tournament.season_tournament.season_year)
                            response_data[tournament.season_tournament.season_year] = response_elements
                        
                    if response_data is None:
                        response_data = {"error": "No se encontraron estadísticas para este torneo."}
                        response_status = status.HTTP_404_NOT_FOUND
                    else:
                        response_status = status.HTTP_200_OK

                
                
        return Response(response_data, status=response_status)