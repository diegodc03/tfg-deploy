
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...models import Tournament
from ...models import AvgTournamentStats
from ...models import Leagues
# Endpoint que va a llevar a cabo el envio de las estadisticas de los equipos de un partido
# GET /api/stats/getTeamsStats/?league_id=1&team_id=1
# GET /api/stats/getTeamsStats/?league_id=1

# http://localhost:8000/api/stats/tournaments/get-stats-by-leagues/?league_name=La%20Liga&type_of_stats=passes_team_pct
class GetUnitaryStatTournamentComparisonOfLeaguesView(APIView):
    
    def get(self, request):
        
        league_name = request.query_params.get('league_name', "La Liga")
        type_of_stats = request.query_params.get('type_of_stats', "passes")
        
        response_data = {}
        response_status = status.HTTP_400_BAD_REQUEST
        
        errors = {}
        
        if not league_name or not isinstance(league_name, str):
            errors['league_name'] = "El parámetro 'league_name' debe ser un str y debe existir."
        
        if not type_of_stats:
            errors['type_of_stats'] = "El parámetro 'type_of_stats' es obligatorio y debe ser 'basic' o 'advanced'."
            
        if errors:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errors": errors}
            
        else:
                
            league = Leagues.objects.filter(name=league_name).first()
            if not league:
                response_data = {"error": "No se encontró la liga con el nombre proporcionado."}
                return Response(response_data, status=response_status)
            else:
                
                tournamets = Tournament.objects.filter(league_id=league)
                
                if not tournamets:
                    response_data = {"error": "No se encontraron torneos para la liga proporcionada."}
                    
                else: 
                    response_elements = []
                    tournament_list = list(tournamets)
                    # iteramos todos los torneos de cada liga
                    for tournament in tournament_list:                        
                        print("tournament list loop", tournament)
                        
                        if tournament.season_tournament is None:
                            response_data = {"error": "El torneo no tiene una temporada asociada."}
                            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
                        
                        avg_tournaments_stats = AvgTournamentStats.objects.filter(league_id=int(tournament.tournament_id)).values_list(
                            "starter_status", type_of_stats
                        )
                    
                    
                        if not avg_tournaments_stats :
                            response_data = {"error": "No se encontraron estadísticas para este torneo."}
                        else:

                            
                            for players_stats in avg_tournaments_stats:
                                
                                entry = {
                                    "league_year": tournament.season_tournament.season_year,
                                    "starter_status": players_stats[0],
                                    "value": round(float(players_stats[1]), 4) if players_stats[1] is not None else 0.0,
                                }

                                response_elements.append(entry)
                                response_data = response_elements
                                response_status = status.HTTP_200_OK
                        
                   

                
                
        return Response(response_data, status=response_status)