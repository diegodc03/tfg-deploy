# Filter para devolvr unicamente las columnas de cada tabla
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...constants.constants import stats_columns_team

# GET /api/filtersUnitaryPlayerMatchChart/


class FiltersColumnOfTableView(APIView):
    
    def get(self, request):
        
        table_request = request.query_params.get('table', "passes_player")
        
        if table_request is None:
            return Response({"error": "El parámetro 'table' es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        
        if table_request not in stats_columns_team:
            return Response({"error": f"La tabla '{table_request}' no es válida."}, status=status.HTTP_400_BAD_REQUEST)
        
        columns_tables = stats_columns_team[table_request]
        
        
        return Response(columns_tables, status=status.HTTP_200_OK)