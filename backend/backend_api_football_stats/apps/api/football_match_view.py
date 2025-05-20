


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status




from ..models import FootballMatch
from ..serializers_dto.serializers import FootballMatchSerializer, FootballMatchWithIdsSerializer


class FootballMatchView(APIView):
    
    
    def get(self, request):

        # Si hay parámetros de query, aplica filtros
        week = request.query_params.get('week', None)
        league_id = request.query_params.get('league_id', None)
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        matches = FootballMatch.objects.all()
        
        if not matches:
            response_data = {"error": "No se encontraron partidos"}
            response_status = status.HTTP_404_NOT_FOUND
        
        else:
        
            if not week and not league_id:
                
                serializer = FootballMatchSerializer(matches, many=True)
                response_data = serializer.data
            
            else:
                # Validación de parámetros
                if week and not week.isdigit():
                    response_data = {"error": "El parámetro 'week' debe ser un número."}
                    response_status = status.HTTP_400_BAD_REQUEST
                    
                elif league_id and not league_id.isdigit():
                    response_data = {"error": "El parámetro 'league_id' debe ser un número."}
                    response_status = status.HTTP_400_BAD_REQUEST
                    
                else:
                    if week:
                        matches = matches.filter(Wk=week)
                    if league_id:
                        matches = matches.filter(Season=league_id)

                    if not matches.exists():
                        response_data = {"error": "No se encontraron partidos con los filtros proporcionados."}
                        response_status = status.HTTP_204_NO_CONTENT
                    else:
                        serializer = FootballMatchSerializer(matches, many=True)
                        response_data = serializer.data

        return Response(response_data, status=response_status)