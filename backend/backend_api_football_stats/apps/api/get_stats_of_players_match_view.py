# EN este fichero unicamente se van a devolver todas las tablas de las estadísticas 
# que tengemos, es decir, se van a recoger todos los modelos de datos de estadísticas
# y se van a devolver todos los datos de cada uno de los modelos


# Funciona

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import FootballMatch
from ..models import MatchStatistics

from ..constants.constants import model_map_serializer


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
        type_table_stats = request.query_params.get('type_table_stats', "stats_summary")
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
        
        
        errores = {}
        # Validar match_id (obligatorio)
        if not is_valid_int(match_id):
            errores['match_id'] = "El parámetro 'match_id' es obligatorio y debe ser un número."
            
        if type_table_stats:
            if not is_valid_str(type_table_stats):
                errores['type_table_stats'] = "El parámetro 'type_table_stats' debe ser un string válido."
            elif type_table_stats != "all" and type_table_stats not in model_map_serializer:
                errores['type_table_stats'] = "El parámetro 'type_table_stats' no es reconocido."
                
        if errores:
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {"errores": errores}
            
        else:
            
            football_match =  FootballMatch.objects.filter(match_id=int(match_id)).first()
            if not football_match:
                response_data = {"error": "No se encontró el partido."}
                response_status = status.HTTP_404_NOT_FOUND
            else: 
                
                # Si ese partido existe, ahora hay que recoger los jugadores que participaron en el partido
                # y filtrar por el id de la posición básica si se proporciona

                # También vamos a recoger el equipo al que pertenece el jugador
                league_id = football_match.Season
                team_id_local = football_match.Home
                team_id_visitor = football_match.Away
                
                



                match_stats_ids = MatchStatistics.objects.filter(match_id=int(match_id))
                if not match_stats_ids.exists():
                    response_data = {"error": "No hay jugadores para este partido cuando se filtra por tipo de jugador."}
                    response_status = status.HTTP_204_NO_CONTENT
                    
                else: 
                    
                    if type_table_stats is not None :
                        # Si se especifica un tipo de tabla, devolver solo esa tabla
                        
                        model_class, serializer_class = model_map_serializer[type_table_stats]
                        
                        stats_data = model_class.objects.filter(stat_id__in=match_stats_ids)
                        #response_data = {type_table_stats: stats_data}
                        response_data = serializer_class(stats_data, many=True).data
                        
                    else:
                        # Si no se especifica el tipo de tabla, devolver todas las tablas
                        stats_data = {}
                        for table_name, model in model_map_serializer.items():
                            model_class, serializer_class = model  
                            stats = model_class.objects.filter(stat_id__in=match_stats_ids)
                            stats_data[table_name] = serializer_class(stats, many=True).data

                    response_status = status.HTTP_200_OK
                
        return Response(response_data, status=response_status)
            