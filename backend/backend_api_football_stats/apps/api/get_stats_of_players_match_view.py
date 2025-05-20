# EN este fichero unicamente se van a devolver todas las tablas de las estadísticas 
# que tengemos, es decir, se van a recoger todos los modelos de datos de estadísticas
# y se van a devolver todos los datos de cada uno de los modelos


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..Constants.constants import model_map

# Endpoint que va a llevar a cabo el envio de todas las tablas del partido
# Tendra una opción de solo enviar una tabla o todas las tablas

# GET /api/getStatsOfMatch/?match_id=1&type_table_stats=stats_summary


class GetStatsOfPlayersMatchView(APIView):
    
    def get(self, request):
    
        def is_valid_int(value):
            return value is not None and value.isdigit()

        def is_valid_str(value):
            return isinstance(value, str) and value.strip() != ''
    
        
        # match_id
        match_id = request.query_params.get('match_id', None)
        # basic_position
        #basic_position_id = request.query_params.get('basic_position', 'stats_summary')
        # type_table_stats
        type_table_stats = request.query_params.get('type_table_stats', None)
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        errores = {}
        # Validar match_id (obligatorio)
        if not is_valid_int(match_id):
            errores['match_id'] = "El parámetro 'match_id' es obligatorio y debe ser un número."
            
        if type_table_stats:
            if not is_valid_str(type_table_stats):
                errores['type_table_stats'] = "El parámetro 'type_table_stats' debe ser un string válido."
            elif type_table_stats != "all" and type_table_stats not in model_map:
                errores['type_table_stats'] = "El parámetro 'type_table_stats' no es reconocido."
                
        if errores:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errores": errores}
            
        else:
            
            if type_table_stats != None :
                
                # Si se especifica un tipo de tabla, devolver solo esa tabla
                model = model_map[type_table_stats]
                stats_data = list(model.objects.filter(match_id=match_id).values())
                response_data = {type_table_stats: stats_data}
                response_status = status.HTTP_200_OK
                
                
            else:
                # Si no se especifica el tipo de tabla, devolver todas las tablas
                stats_data = {}
                for table_name, model in model_map.items():
                    stats_data[table_name] = list(model.objects.filter(match_id=match_id).values())
                response_data = stats_data
                response_status = status.HTTP_200_OK
                
        return Response(response_data, status=response_status)
            