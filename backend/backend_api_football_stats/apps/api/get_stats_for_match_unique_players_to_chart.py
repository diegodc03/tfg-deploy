from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import PositionCategoryRelationBasicSpecific
from ..models import PositionMatchPlayerRelation

from ..models import FootballMatch
from ..models import MatchStatistics


from ..constants.constants import stats_columns, stats_columns_player, model_map



# GET /api/statsPlayersMatchToChart/?match_id=1&basic_position=1&type_table_stats=1

class GetStatsPlayersToChartView(APIView):

    def get(self, request):
    
        def is_valid_int(value):
            return value is not None and value.isdigit()
        def is_valid_str(value):
            return isinstance(value, str) and value.strip() != ''
    
        
        # match_id
        match_id = request.query_params.get('match_id', None)
        # basic_position
        basic_position_id = request.query_params.get('basic_position', None)
        # type_table_stats
        type_table_stats = request.query_params.get('type_table_stats', 'passes_player_pct')
        
        response_data = None
        response_status = status.HTTP_400_BAD_REQUEST
          
          
        errores = {}
        # Validar match_id (obligatorio)
        if not is_valid_int(match_id):
            errores['match_id'] = "El parámetro 'match_id' es obligatorio y debe ser un número."
        
         # Validar basic_position_id si fue enviado
        if basic_position_id and not is_valid_int(basic_position_id):
            errores['basic_position_id'] = "El parámetro 'basic_position_id' debe ser un número."
            
        
        if not is_valid_str(type_table_stats):
            errores['type_table_stats'] = "El parámetro 'type_table_stats' debe ser un string válido."
        elif type_table_stats not in stats_columns_player:
            errores['type_table_stats'] = "El parámetro 'type_table_stats' no es reconocido."

        # Si hay errores, devolverlos
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

                match_stats = MatchStatistics.objects.filter(match_id=int(match_id))
                if not match_stats.exists():
                    response_data = {"error": "No hay jugadores para este partido cuando se filtra por tipo de jugador."}
                    response_status = status.HTTP_204_NO_CONTENT
                    
                else: 

                    if basic_position_id:
                        
                        print(f"Basic Position ID: {basic_position_id}")
                        # Tengo que coger en base a la posicion básica, todas las posiciones específicas
                        specific_positions = PositionCategoryRelationBasicSpecific.objects.filter(category_id=int(basic_position_id))
                        specific_positions_ids = [pos.specific_position_id for pos in specific_positions]

                        jugadores_filtrados = PositionMatchPlayerRelation.objects.filter(
                            match_id=football_match,
                            position_id__in=specific_positions_ids
                        ).values_list('player_id', flat=True)

                        match_stats = match_stats.filter(player_id__in=jugadores_filtrados)
                  

                    
                    if type_table_stats not in stats_columns_player:
                        response_data = {"error": "El parámetro 'type_table_stats' no es reconocido."}
                        response_status = status.HTTP_400_BAD_REQUEST
                            
                    else:

                        data_columns = {}
                                
                        final_data = []
                        # Obtener el modelo correspondiente a la tabla
                        
                        tables = stats_columns_player[type_table_stats]["tables"]
                        columns = stats_columns_player[type_table_stats]["columns"]
                        
                        # Yo aqui tengo un loop que va a recorrer cada tabla con sus columnas, lo que voy a hacer es ahora añadirlo a un diccionario
                        for table in tables:
                            # Obtenemos el modelo
                            model = model_map.get(table)
                            if not model:
                                response_data = {"error": "El modelo no está mapeado."}
                                response_status = status.HTTP_400_BAD_REQUEST
                            else:
                                estadistics = model.objects.filter(stat_id__in=match_stats)
                                
                                for stat in estadistics:
                                    player_name = stat.player_id.player_name if stat.player_id else "Desconocido"
                                    player_id = stat.player_id.player_id if stat.player_id else None
                                    data_columns[player_name] = []
                                    
                                    for column in columns:
                                        value = getattr(stat, column, None)
                                        if value is not None:
                                            data_columns[player_name].append({
                                                "player_id": player_id,
                                                "column": column,
                                                "value": value
                                            })
                                
                                # Transformar a formato de salida agrupado por columna
                                final_data = [
                                    {
                                        "jugador": player,
                                        "values": stats
                                    } for player, stats in data_columns.items()
                                ]

                                response_data = final_data
                                response_status = status.HTTP_200_OK

        
        return Response(response_data, status=response_status)

        
        