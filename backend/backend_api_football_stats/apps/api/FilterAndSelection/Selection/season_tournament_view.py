# apps/api/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ....models import Tournament
from ....models import Season
from ....serializers_dto.serializers import SeasonTournamentSerializer, SeasonTournamentOnlySeasonYearSerializer


class SeasonTournamentView(APIView):

    def get(self, request): 
        
        view_type = request.query_params.get('view_type', 'season_tournament')
        
        # Inicializar la respuesta predeterminada
        response_data = None
        response_status = status.HTTP_200_OK
        
        if view_type == 'season_only_season_year':
            
            tournaments = Tournament.objects.select_related('season_tournament').all()
            
            if not tournaments:
                response_data = {"Datos": "No se encontraron torneos"}
                response_status = status.HTTP_204_NO_CONTENT
            else:
                serializer = SeasonTournamentOnlySeasonYearSerializer(tournaments, many=True)
                response_data = serializer.data
        
        else:
            # Si no se proporciona un view_type válido, se puede devolver un error o un valor predeterminado
            tournaments = Tournament.objects.select_related('season_tournament').all()
            if not tournaments:
                response_data = {"Datos": "No se encontraron torneos"}
                response_status = status.HTTP_204_NO_CONTENT
            else:
                serializer = SeasonTournamentSerializer(tournaments, many=True)
                response_data = serializer.data
                
        return Response(response_data, status=response_status)
        
    
        
    
