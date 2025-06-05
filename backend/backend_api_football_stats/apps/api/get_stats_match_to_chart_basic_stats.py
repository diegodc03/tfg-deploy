from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.basic_position_category import BasicPositionCategory

from ..models import TeamPlayer

from ..models import PositionCategoryRelationBasicSpecific
from ..models import PositionMatchPlayerRelation

from ..models import FootballMatch
from ..models import MatchStatistics

from ..constants.constants import stats_columns_player, model_map



# GET /api/charts/statsPlayersMatchToChart/?match_id=1&basic_position=1&type_table_stats=1

class GetStatsMatchToChartBasicStatsView(APIView):

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
                
                season_id = football_match.Season
                # Si ese partido existe, ahora hay que recoger los jugadores que participaron en el partido
                # y filtrar por el id de la posición básica si se proporciona

                match_stats = MatchStatistics.objects.filter(match_id=int(match_id))
                if not match_stats.exists():
                    response_data = {"error": "No hay jugadores para este partido cuando se filtra por tipo de jugador."}
                    response_status = status.HTTP_204_NO_CONTENT
                    
                else: 

                    # Filtros opcionales
                    if basic_position_id:
                        
                        # Tengo que coger en base a la posicion básica, todas las posiciones específicas
                        specific_positions = PositionCategoryRelationBasicSpecific.objects.filter(category_id=int(basic_position_id)).values_list('position_id', flat=True)
                        specific_positions_ids = list(specific_positions)

                        jugadores_filtrados = PositionMatchPlayerRelation.objects.filter(
                            match_id=football_match,
                            position_id__in=specific_positions_ids
                        ).values_list('player_id', flat=True)

                        match_stats = match_stats.filter(player_id__in=jugadores_filtrados)
                  
                       
                       
                    tables = stats_columns_player[type_table_stats]["tables"]
                    columns = stats_columns_player[type_table_stats]["columns"]

                    final_data = []
                    # Obtener el modelo correspondiente a la tabla
                    
                    for table in tables:
                        
                        model = model_map.get(table)
                        
                        if not model:
                            response_data = {"error": f"La tabla '{table}' no está mapeada."}
                            response_status = status.HTTP_400_BAD_REQUEST
                            break
                    
                        else:
                            
                            player_statistics = model.objects.filter(stat_id__in=match_stats)
                    
                            data_por_columna = {col: [] for col in columns}

                            # Array de ids ya añadidos para evitar duplicados
                            ids_ya_aniadidos = set()
                            
                            # Recorremos las estadísticas, van a ir pasando por cada columna
                            # y se van a ir guardando en un diccionario
                            for stat in player_statistics:
                                jugador_nombre = stat.player_id.player_name if stat.player_id else "Desconocido"
                                jugador_id = stat.player_id.player_id if stat.player_id else None

                                ids_ya_aniadidos.add(jugador_id)
                            
                                for columna in columns:
                                    
                                    valor = getattr(stat, columna, None)
                                    data_por_columna[columna].append({
                                        "player_id": jugador_id,
                                        "player_name": jugador_nombre,
                                        "value": valor
                                    })

                            # Transformar a formato de salida agrupado por columna
                            final_data = [
                                {
                                    "stat": columna,
                                    "values": jugadores
                                } for columna, jugadores in data_por_columna.items()
                            ]
                            
                            # Se va a añadir tanto el nombre del equipo y si es local o visitante
                            # y también el tipo de jugador básico
                            for data in final_data:
                                for value in data['values']:
                                    player_id = value['player_id']
                                    
                                    # Se tiene que hacer una consulta a la base de datos para ver el nombre e id del equipo
                                    is_home = TeamPlayer.objects.filter(player_id=player_id, team_id=football_match.Home).exists()
                                    
                                    if is_home:
                                        value['team_name'] = football_match.Home.team_name
                                        value['is_home'] = True
                                    else:
                                        value['team_name'] = football_match.Away.team_name
                                        value['is_home'] = False
                                    
                                    # También hay que hacer una peticion a las posiciones basicas de un jugador
                                    specific_positions  = PositionMatchPlayerRelation.objects.filter(
                                        match_id=match_id, player_id=player_id).values_list('position_id', flat=True)
                                    
                                    specific_positions = list(specific_positions)
                                    print(f"Specific Positions: {specific_positions[0]}")
                                    
                                    specific_position = specific_positions[0] if specific_positions else None
                                    
                                    if specific_position:
                                        basic_position = PositionCategoryRelationBasicSpecific.objects.filter(
                                            position_id=specific_position
                                        ).values_list('category_id', flat=True)
                                        
                                        basic_position = list(basic_position)
                                        basic_position = basic_position[0] if basic_position else None
                                        
                                        if basic_position:
                                            basic_position_element = BasicPositionCategory.objects.filter(
                                            category_id=basic_position
                                            ).first()
                                            if basic_position_element:
                                                value['basic_position'] = basic_position_element.category_name
                                                value['basic_position_id'] = basic_position_element.category_id
                                            else:
                                                value['basic_position'] = "Desconocido"
                                        else:
                                            value['basic_position'] = "neutral"
                                    else:
                                        value['basic_position'] = "neutral"
                        
                            response_data = final_data
                            response_status = status.HTTP_200_OK

        
        return Response(response_data, status=response_status)

        
        