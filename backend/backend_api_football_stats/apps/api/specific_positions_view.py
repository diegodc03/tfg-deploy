from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import SpecificsPositionsByCategory
from ..serializers_dto.serializers import SpecificPositionSerializer

class SpecificPositionsView(APIView):

    def get(self, request):
        
        specific_positions = SpecificsPositionsByCategory.objects.all()
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        if not specific_positions:
            response_data = {"Datos": "No se encontraron posiciones especificas"}
            response_status = status.HTTP_204_NO_CONTENT
        
        else:
            serializer = SpecificPositionSerializer(specific_positions, many=True)
            response_data = serializer.data
            
        return Response(response_data, status=response_status)