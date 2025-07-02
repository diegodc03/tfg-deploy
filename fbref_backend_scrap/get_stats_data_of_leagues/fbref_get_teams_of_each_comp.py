

from bs4 import BeautifulSoup as soup
import requests
from pyspark.sql.functions import col

from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import get_teams_in_competition
from Esquemas.spark_schema import get_team_schema
from utils.write_dataframe_to_mysql_file import write_dataframe_to_mysql
from pyspark.sql.types import StructType, StringType



def insert_team_in_competition_on_database(spark, jdbc_url, db_properties, teams, league, season, league_id):
    
    returning_value = spark.createDataFrame([], StructType([]))                                 
    
    print("Inserting teams in competition")
    team_schema = get_team_schema()
    try:
        teams_of_tournament = get_teams_in_competition(spark, jdbc_url, db_properties, league_id)
        teams_to_insert = spark.createDataFrame([], team_schema)

        for team in teams:
            if teams_of_tournament.filter(col("team_name") == team).count() == 0:
                new_team_df = spark.createDataFrame([(team, league_id)], team_schema)
                teams_to_insert = teams_to_insert.union(new_team_df)

        insert_count = teams_to_insert.count()

        if insert_count > 0:
            write_dataframe_to_mysql(teams_to_insert, jdbc_url, db_properties, "team")
            print(f"{insert_count} team(s) inserted into the competition.")
            returning_value = teams_to_insert
        
        else:
            print("No new teams to insert.")
            result_schema = StructType().add("team_name", StringType())
            returning_value = spark.createDataFrame([("No new teams",)], result_schema)

    except Exception as e:
        print(f"Error al insertar los equipos en la competición: {e}")
        returning_value = spark.createDataFrame([], team_schema)
        
    return returning_value





def get_teams_of_competition(spark, jdbc_url, db_properties, league_name, tournament_fbref_id, season, league_id):


    returning_value = spark.createDataFrame([], StructType([]))
    
    var_key_link = f"https://fbref.com/en/comps/{tournament_fbref_id}/{season}/stats/{season}-{league_name}-Stats"
    print(var_key_link)
    html = requests.get(var_key_link).text
    try:
        # Crear el objeto BeautifulSoup
        parse = soup(html, 'html.parser')
        div_select = parse.find('div', id='div_stats_squads_standard_for')

        # Encontrar todos los elementos <th> con class="left" y data-stat="team"
        team_elements = div_select.find_all('th', class_='left', attrs={'data-stat': 'team'})

        teams = []
        for team in team_elements:
            team_name = team.find('a').text  # Extraer el texto del enlace
            teams.append((team_name))
        
        league_name = league_name.replace('-', ' ')
        df = insert_team_in_competition_on_database(spark, jdbc_url, db_properties, teams, league_name, season, league_id)
        if df.rdd.isEmpty():
            print(f"Error al insertar los equipos en la competición {league_name}")
        else:
            print(f"Equipos de la competición {league_name} insertados correctamente")
            returning_value = df
            
    except Exception as e:
        print(f"Error al obtener los equipos de la competición: {e}")
        returning_value = spark.createDataFrame([], StructType([]))


    print('Teams of competition collected...')
    return returning_value

