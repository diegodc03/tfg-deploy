# apps/api/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import Tournament
from ..serializers_dto.serializers import TournamentSerializer


class TournamentView(APIView):

    def get(self, request):
        
        tournaments = Tournament.objects.all()
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        if not tournaments:
            response_data = {"Vacio": "No se encontraron torneos"}
            response_status = status.HTTP_204_NO_CONTENT
        else:
            
            serializer = TournamentSerializer(tournaments, many=True) 
            response_data = serializer.data
            
        return Response(response_data, status=response_status)