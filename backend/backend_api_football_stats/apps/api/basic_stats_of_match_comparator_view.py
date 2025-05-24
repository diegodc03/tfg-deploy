
# Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..constants.constants import stats_mapping
from backend_api_football_stats.apps.serializers_dto.serializers import BasicMatchStatsSerializer, GeneralComparatorMatchStatsSerializer

from ..models import GeneralComparatorMatchStats


class BasicStatsOfMatchComparatorView(APIView):
    
    def get(self, request):
    
        match_id = request.query_params.get('match_id', None)
        
        response_data = None
        response_status = status.HTTP_200_OK
        
        # No existen filtros, devuelve todas las ligas
        if not match_id or not match_id.isdigit():
            response_data = {"error": "El parámetro 'match_id' debe ser un número."}
            response_status = status.HTTP_400_BAD_REQUEST
        
        
        else:
            
            gen_stats = GeneralComparatorMatchStats.objects.filter(match_id=match_id).first()
            
                
            if not gen_stats:
                response_data = {"Datos": "Not found stats for this match_id, eso es"}
                response_status = status.HTTP_204_NO_CONTENT
                
            else:
                match_stats_dict = build_match_stats_dict(gen_stats)
                #serializer = BasicMatchStatsSerializer(match_stats_dict)
                response_data = match_stats_dict


            
        return Response(response_data, status=response_status)
    
    
def build_match_stats_dict(instance):
    """
    Recibe una instancia de GeneralComparatorMatchStats y devuelve
    un diccionario listo para serializar con BasicMatchStatsSerializer.
    """
    result = {
        "match_id": instance.match_id.match_id  # o .pk si no usas id directamente
    }

    for stat_name, is_pct in stats_mapping.items():
        local_field = f"local_{stat_name}"
        visitor_field = f"visitor_{stat_name}"
        
        local_value = getattr(instance, local_field, None)
        visitor_value = getattr(instance, visitor_field, None)

        # Solo agrega si ambos valores existen (opcional: puedes cambiar esta lógica)
        if local_value is not None and visitor_value is not None:
            result[stat_name] = {
                "local": local_value,
                "visitor": visitor_value,
                "type_stat_pct": is_pct.get("type_stat_pct")
            }

    return result