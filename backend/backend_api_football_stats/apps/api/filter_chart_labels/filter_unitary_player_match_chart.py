# Filter para ver que mostrar en el forntend cuando hay que mostrar los filtros de los jugadores

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...constants.constants import filter_labels_unitary

# GET /api/filtersUnitaryPlayerMatchChart/


class FiltersUnitaryPlayerMatchChartView(APIView):
    
    def get(self, request):
        return Response(filter_labels_unitary, status=status.HTTP_200_OK)