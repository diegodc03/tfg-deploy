# apps/api/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ....models import Season
from ....serializers_dto.serializers import SeasonSerializer


class SeasonView(APIView):

    def get(self, request):
        
        seasons = Season.objects.all()
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        if not seasons:
            response_data = {"Datos": "No se encontraron temporadas"}
            response_status = status.HTTP_204_NO_CONTENT
        
        else:
            serializer = SeasonSerializer(seasons, many=True)
            response_data = serializer.data
            
        return Response(response_data, status=response_status)