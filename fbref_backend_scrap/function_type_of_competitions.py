
import numpy as np

def get_possible_leagues():
    """Dictionary with all the possible pages, leagues and season for the scraper.
    Also contains some exception to prevent errors such as a league or page that is not a part of the scraper.

    Args:
        league (str): League to scrape
        season (str): Season to scrape
        page (str): Page to scrape

    Raises:
        InvalidStrType: If a parameter is not a string
        InvalidLeagueException: If a league is not inside all the leagues possibles
        InvalidSeasonException: If a season is not inside all the seasons possibles

    Returns:
        dict: dictionary with the possible leagues
    """
    possible_leagues = {
            'Premier League': {
                'id': 9,
                'slug': 'Premier-League',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'league'
            },
            'La Liga': {
                'id': 12,
                'slug': 'La-Liga',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'league'
            },
            'Ligue 1': {
                'id': 13,
                'slug': 'Ligue-1',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'league'
            },
            'Bundesliga': {
                'id': 20,
                'slug': 'Bundesliga',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'league'
            },
            'Serie A': {
                'id': 11,
                'slug': 'Serie-A',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'league'
            },
            'Champions League': {
                'id': 8,
                'slug': 'Champions-League',
                'seasons': {
                    '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021'
                },
                'type': 'cup'
            }
            
        }

  
    
    return possible_leagues




