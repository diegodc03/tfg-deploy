
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import Leagues
from ..serializers_dto.serializers import LeaguesSerializer

class LeaguesView(APIView):
    
    
    def get(self, request):
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        leagues = Leagues.objects.all()
        
        if not leagues:
            response_data = {"Datos": "No se encontraron temporadas"}
            response_status = status.HTTP_204_NO_CONTENT
        else:
            serializer = LeaguesSerializer(leagues, many=True)
            response_data = serializer.data

        return Response(response_data, status=response_status)