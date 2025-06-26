from bs4 import BeautifulSoup as soup
import requests



##############################################################################
# recoge los links de los partidos de la liga
#
# url: url de todos los partidos de una liga y temporada
# league: nombre de la liga
#
##############################################################################
def get_match_links(url, league): 
  
    print('Getting player data links...')
    # access and download content from url containing all fixture links    
    match_links = []
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        links = soup(html.content, "html.parser").find_all('a')
        # filter list to return only needed links
        key_words_good = ['/en/matches/', f'{league}']
        for l in links:
            href = l.get('href', '')
            if all(x in href for x in key_words_good):
                if 'https://fbref.com' + href not in match_links:                 
                    match_links.append('https://fbref.com' + href)
    except Exception as e:
        print(f"Error al obtener los links de los partidos: {e}")
        match_links = []
        return match_links
    print('Player data links collected...')
    return match_links


