
# Filter para devolvr unicamente las columnas de cada tabla
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...models import Team
from ...constants.constants import stats_columns_team



class GetTeamsOfLeagueView(APIView):
    
    def get(self, request):
        
        league_id = request.query_params.get('league_id')
        
        if not league_id:
            return Response({"error": "league_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            teams = Team.objects.filter(tournament_team_id=league_id).values_list("team_id", "team_name")
            teams_dict = {team[0]: team[1] for team in teams}  # Convert to dictionary

            return Response(teams_dict, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)