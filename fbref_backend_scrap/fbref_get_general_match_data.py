




##############################################################################
# recoge los datos generales de un partido, es el computo total de cada equipo
#
# link: link del partido
#
# return: dataframe con los datos generales del partido
#
##############################################################################

import pandas as pd
import requests
from bs4 import BeautifulSoup as soup




def get_general_match_data(link):
    print('Getting general match data...')
    html = requests.get(link).text
    beatySoup = soup(html, 'html.parser')
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()

    MANDATORY_COLUMNS = ['Possession', 'Passing Accuracy', 'Shots on Target', 'Saves', 'Cards']
    CARDS = "Cards"
    
    stats = {}
    dict_teams = {}
    try:
        teams_stats = beatySoup.find('div', id='team_stats')
        if not teams_stats:
            print("No se encontró el contenedor 'team_stats'")
            return pd.DataFrame(), pd.DataFrame()
        else: 
            tr_stats = teams_stats.find_all('tr')
            th_teams = tr_stats[0].find_all('th')

            for i in range(1, len(tr_stats), 2):
                array_teams = []
                
                th_stat = tr_stats[i].find('th')
                if not th_stat:
                    continue

                stat_name = th_stat.text.strip()
                print(f"Stat name: {stat_name}")
        
                if CARDS in stat_name:
                    td_values = tr_stats[i+1].find_all('td')
                    if len(td_values) == 2:
                        team1_cards = len(td_values[0].find_all('span', class_='yellow_card'))
                        team2_cards = len(td_values[1].find_all('span', class_='yellow_card'))
                        team1_red_cards = len(td_values[0].find_all('span', class_='red_card'))
                        team2_red_cards = len(td_values[1].find_all('span', class_='red_card'))
                        team1_yellow_red_cards = len(td_values[0].find_all('span', class_='yellow_red_card'))
                        team2_yellow_red_cards = len(td_values[1].find_all('span', class_='yellow_red_card'))
                        team1_cards += team1_red_cards + team1_yellow_red_cards
                        team2_cards += team2_red_cards + team2_yellow_red_cards
                        if team1_cards:
                            array_teams.append(team1_cards)
                        else:
                            array_teams.append('0')
                        if team2_cards:
                            array_teams.append(team2_cards)
                        else:
                            array_teams.append('0')
                        dict_teams[stat_name] = array_teams
            
                else:
                    td_values = tr_stats[i+1].find_all('td')

                    if len(td_values) == 2:
                        strong_value1 = td_values[0].find_all('strong')
                        strong_value2 = td_values[1].find_all('strong')
                        if strong_value1:
                            array_teams.append(strong_value1[0].text.strip())
                        if strong_value2:
                            array_teams.append(strong_value2[0].text.strip())

                        dict_teams[stat_name] = array_teams
           
            # Check if all mandatory columns are present
            if len(dict_teams) < len(MANDATORY_COLUMNS):
                dict_teams_formated = {}
                for column in MANDATORY_COLUMNS:
                    if column not in dict_teams.keys():
                        dict_teams_formated[column] = ["0.0%", "0.0%"]
                    else:
                        dict_teams_formated[column] = dict_teams[column]
                dict_teams = dict_teams_formated
            
            df1 = check_dataframe_general_match_data(dict_teams, 0)

        teams_stats_extra = beatySoup.find('div', id='team_stats_extra')

        if not teams_stats_extra:
            print("No se encontró el contenedor 'team_stats_extra'")
        else:
            stat_blocks = teams_stats_extra.find_all('div')
            for block in stat_blocks:

                stats_per_block = block.find_all('div')

                for i in range(4, len(stats_per_block), 3):
                    array_values = []

                    stat_name = stats_per_block[i].text
                    local_stat = stats_per_block[i-1].text
                    visitor_stat = stats_per_block[i+1].text

                    array_values.append(local_stat)
                    array_values.append(visitor_stat)
                    stats[stat_name] = array_values
            df2 = check_dataframe_general_match_data(stats, 1)    

        print('General match data collected...')
        return df1, df2
    
    except Exception as e:
        print(f"Error al obtener los datos generales del partido: {e}")
        return pd.DataFrame(), pd.DataFrame()
    
    


##############################################################################
# limpia el dataframe de posibles valores incorrectos que puedan dar luegar a error limpia los valores de las estadisticas generales de un partido
#
# stats: estadisticas del partido
# type_of_value: tipo de valor
#
# return: dataframe limpio
#
##############################################################################
def check_dataframe_general_match_data(stats, type_of_value):
    # Pass to dataframe
    df = pd.DataFrame(stats).transpose().reset_index()
    df.columns = ['Statistic', 'local', 'visitor']

    if type_of_value == 0:
        df['local'] = clean_dataframe_general_match_data(df['local'])
        df['visitor'] = clean_dataframe_general_match_data(df['visitor'])  

    elif type_of_value == 1:
        df['local'] = clean_dataframe_general_match_data(df['local'])
        df['visitor'] = clean_dataframe_general_match_data(df['visitor'])

    return df




##############################################################################
# recoge los datos de los jugadores, introduce en la base de datos todas las estadisticas de los jugadores
#
# series: valor de una estadistica
#
# return: series con los valores limpios
#
##############################################################################
def clean_dataframe_general_match_data(series):
    def clean_value(value):
        value = str(value)
        if value == "" or value == "%":
            return 0.0
        if "%" in value:
            value = float(value.rstrip('%'))
            return min(max(value, 0), 100)
        try:
            return float(value)
        except ValueError:
            return 0.0  
    return series.apply(clean_value)


