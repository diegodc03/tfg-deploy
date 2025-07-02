

import sys
import time
from urllib.error import HTTPError
from add_enumeration_contant_data.add_different_tables_to_db import insert_reference_data
from get_stats_data_of_leagues.fbref_scrap import get_5_leagues
from get_all_stats_to_score_players.get_stats import get_score_of_5_leagues
from get_average_stats.fbref_get_average_stats import get_average_of_5_leagues
from get_average_stats.score_teams_in_tournament import get_teams_average_of_5_leagues
from config.spark_configuration import create_spark_session, jdbc_url, db_properties
from Esquemas.spark_schema import get_type_position_schema, get_event_shots_schema, get_body_part_schema, get_outcome_schema, get_basic_positions_schema
from utils.constants import type_shots, body_parts, outcomes, type_positions, basic_positions





def main():

    spark = create_spark_session()
    print('Starting...') 
    print('Welcome to the FBref data collection tool!')
    print("")
    print("")

    while True:

        print("1. Quieres introducir tipos de pases, tipos de tiros, partes del cuerpo?")
        print("2. Quieres introducir a los jugadores?")
        print("3. Quieres introducir los datos de media de los equipos?")
        print("4. Quieres puntuar los partidos de los jugadores?")
        print("5. Quieres ver los partidos de una liga?")
        print("6. Quieres hacer la puntuacion media de la liga por equipos?")
        print("7. Quieres salir?")
        election = input("Que quieres hacer?")

        if election == '1':

            if not insert_reference_data(spark, jdbc_url, db_properties, "event_shots", "event_shot_name", type_shots, get_event_shots_schema()).isEmpty():
                print("Datos introducidos correctamente")
            
            if not insert_reference_data(spark, jdbc_url, db_properties, "body_part", "body_part_name", body_parts, get_body_part_schema()).isEmpty():
                print("Datos introducidos correctamente")

            if not insert_reference_data(spark, jdbc_url, db_properties, "outcome_stats", "outcome_name", outcomes, get_outcome_schema()).isEmpty():
                print("Datos introducidos correctamente")

            if not insert_reference_data(spark, jdbc_url, db_properties, "position_on_the_field", "position_name", type_positions, get_type_position_schema()).isEmpty():
                print("Datos introducidos correctamente")    

            # Hacer este bien
            if not insert_reference_data(spark, jdbc_url, db_properties, "position_on_the_field", "position_name", basic_positions, get_basic_positions_schema()).isEmpty():
                print("Datos introducidos correctamente")    
            break

            # Añadir los que faltan



        elif election == '2':
            returning_value = get_5_leagues(spark, jdbc_url, db_properties)
            if returning_value.empty:
                print('No data to collect')
                sys.exit()
            break
        
        elif election == '3':
            returning_value = get_average_of_5_leagues(spark, jdbc_url, db_properties)
            if returning_value.isEmpty():
                print('Error al obtener los datos de la liga')
                sys.exit()
            break
        
        elif election == '4':
            returning_value = get_score_of_5_leagues(spark, jdbc_url, db_properties)
            if returning_value.isEmpty():
                print('No data to collect')
                sys.exit()
            break
        
        elif election == '5':
            get_teams_average_of_5_leagues(spark, jdbc_url, db_properties)
        
        elif election == '6':
            break




if __name__ == '__main__':
    try:
        main()
    except HTTPError:
        print('The website refused access, try again later')
        time.sleep(5)

