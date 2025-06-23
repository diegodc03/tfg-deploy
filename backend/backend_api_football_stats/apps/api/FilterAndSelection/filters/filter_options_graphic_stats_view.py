from rest_framework.response import Response
from rest_framework.views import APIView
from ....models import ESTADISTICAS_INTERESANTES


class MatchStatsScoreView(APIView):
    
    def get(self, request):
        # Tenemos que mostrar en este get las opciones de los graficos a elegir de las stats
        return Response(ESTADISTICAS_INTERESANTES, status=200)
        