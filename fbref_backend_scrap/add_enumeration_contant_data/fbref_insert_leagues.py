



from fbref_backend_scrap.utils.function_type_of_competitions import get_possible_leagues
from functions_to_stract_of_dataBase.querys_of_match_stats_and_football_matchs_and_teams import check_season_exists, check_tournament_exists
from functions_to_stract_of_dataBase.querys_score_match import get_season_tournament_id
from fbref_backend_scrap.Esquemas.spark_schema import get_season_schema, get_tournament_schema
from fbref_backend_scrap.utils.write_dataframe_to_mysql_file import write_dataframe_to_mysql


def insert_league_competition_on_database(spark, url, db_properties):
    
    possible_leagues = get_possible_leagues()
    data = put_in_dic_list(possible_leagues)

    all_seasons = []
    all_tournaments = []

    for league in data:
        for season in league['seasons']:
            season_dict = {'season_year': season}
            
            if season_dict not in all_seasons:
                all_seasons.append(season_dict)

        #Insertar las ligas y sus temporadas correspondientes
        for season in league['seasons']:
            all_tournaments.append({
                'nombre_liga': league['name'],
                'season_tournament_id': 0,
                'type_of_competition': league['type'],
                'tournament_fbref_id': league['id'], 
                'season_year': season
            })

    insert_seasons(all_seasons, spark,  url, db_properties)
    insert_tournaments(all_tournaments, spark, url, db_properties)

    
def insert_seasons(seasons, spark, jdbc_url, db_properties):

    season_schema = get_season_schema()
    season_df_to_insert = spark.createDataFrame([], season_schema)

    # Comprobar e insertar solo las temporadas que no existen
    for season in seasons:
        if check_season_exists(season['season_year'], spark, jdbc_url, db_properties) == 0:
            season_df_to_insert = season_df_to_insert.union(spark.createDataFrame([season], season_schema))
    
    if season_df_to_insert.count() > 0:
        write_dataframe_to_mysql(season_df_to_insert, jdbc_url, db_properties, "season")

    
    

def insert_tournaments(tournaments, spark, jdbc_url, db_properties):
    tournament_schema = get_tournament_schema()

    tournament_df_to_insert = spark.createDataFrame([], tournament_schema)
    for tournament in tournaments:
        if check_tournament_exists(tournament['nombre_liga'], tournament['season_tournament_id'], spark, jdbc_url, db_properties) == 0:
            season_id = get_season_tournament_id(tournament['season_year'], spark, jdbc_url, db_properties)
            tournament['season_tournament_id'] = season_id
            #Eliminar season year
            del tournament['season_year']

            tournament_df_to_insert = tournament_df_to_insert.union(spark.createDataFrame([tournament], tournament_schema))
    
    if tournament_df_to_insert.count() > 0:
        write_dataframe_to_mysql(tournament_df_to_insert, jdbc_url, db_properties, "tournament")



def put_in_dic_list(possible_leagues):
    data = [
        {
            'name': name,
            'id': details['id'],
            'slug': details['slug'],
            'seasons': list(details['seasons']),  # Convertir set a lista
            'type': details['type']
        }
        for name, details in possible_leagues.items()
    ]
    return data