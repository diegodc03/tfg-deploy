

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from ....models import FootballMatch
from ....serializers_dto.serializers import  FootballMatchAllDataSerializer


class BasicVisualizeOfMatchView(APIView):
    
    
    def get(self, request):
        

        match_id = request.query_params.get('match_id', None)
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        # No existen filtros, devuelve todas las ligas
        if not match_id or not match_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' debe ser un número."}
            response_status = status.HTTP_400_BAD_REQUEST
        
        else:
                    
            # Si hay parámetros de filtrado
            football_match = FootballMatch.objects.filter(match_id=match_id).first()
            
            if not football_match:
                response_data = {"Datos": "No se encontraron partidos con los filtros proporcionados."}
                response_status = status.HTTP_204_NO_CONTENT
            else:
                # Si se encuentra el partido, devuelve los datos
                serializer = FootballMatchAllDataSerializer(football_match)
                response_data = serializer.data
            
        return Response(response_data, status=response_status)