

from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
from utils.constants import var_integers, var_floats, var_pct, var_strings






##############################################################################
# limpia el dataframe de posibles valores incorrectos que puedan dar luegar a error
#
# df: dataframe a limpiar
#
# return: dataframe limpio
#
##############################################################################
def clean_dataframe(df):
    try:
        df_cleaned = pd.DataFrame()

        for column in df.columns:
            if column in var_integers:
                df_cleaned[column] = df[column].fillna(0).apply(integer_check).astype(int)
            elif column in var_floats:
                df_cleaned[column] = df[column].fillna(0.0).apply(float_check).astype(float)
            elif column in var_pct:
                df_cleaned[column] = df[column].fillna(0.0).apply(pct_check).astype(float)
            elif column in var_strings:
                df_cleaned[column] = df[column].fillna("").apply(string_check)

        return df_cleaned
    
    except Exception as e:
        print(f"Error limpiando el DataFrame: {e}")



def integer_check(value):
    try:
        if str(value).lower() in ["nan", ""]:
            return 0
        return int(value)
    except (ValueError, TypeError):
        return 0

def float_check(value):
    try:
        if str(value).lower() in ["nan", ""]:
            return 0.0
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def pct_check(value):
    try:
        if str(value).lower() in ["nan", ""]:
            return 0.0
        value = float(value)
        if value < 0.0 or value > 100.0:
            return max(0.0, min(value, 100.0))
        return value
    except (ValueError, TypeError):
        return 0.0

def string_check(value):    
    if str(value).lower() in ["nan", ""]:
        return "unknown"
    else:
        return str(value)

def check_value(value, column):
    if column in var_integers:
        value = integer_check(value)
        return max(value, 0)
    elif column in var_floats:
        value = float_check(value)
        return max(value, 0.0)
    elif column in var_pct:
        return pct_check(value)
    else:
        return string_check(value)






##############################################################################
# recoge el tipo de estadisticas que hay en el partido, de esto depende la correcta recogida de los datos
#
# link: link del partido
#
# return: 1 si hay switcher, 2 si no hay switcher
#
##############################################################################
def get_switcher(html):
    # Obtener el HTML
    elements_on_switcher = []
    html_soap = soup(html, 'html.parser')
    
    switcher_div = html_soap.find('div', class_='filter switcher')
    if not switcher_div:
        print("No se encontró el contenedor 'filter switcher'")
        return False
    
    div_links = switcher_div.find_all('div')

    for div in div_links:
        elements_on_switcher.append(div.text)

    return elements_on_switcher


##############################################################################
# recoge el tipo de estadisticas que hay en el partido, de esto depende la correcta recogida de los datos
#
# link: link del partido
#
# return: 1 si hay switcher, 2 si no hay switcher
#
##############################################################################
def get_over_header_data(html):
    html_soap = soup(html, 'html.parser')
    elements_on_over_header = []
    over_header_tr = html_soap.find('tr', class_='over_header')

    if not over_header_tr:
        print("No se encontró el contenedor 'over_header'")
        return

    th_links = over_header_tr.find_all('th')

    for div in th_links:
        elements_on_over_header.append(div.text)

    return elements_on_over_header

def get_type_of_stats(link):
    html = requests.get(link).text
    elements_switcher = get_switcher(html)  # Se obtiene si hay switcher o no, sabiendo los elementos que hay, se puede decidir si se hacen x tablas
    
    if elements_switcher:
        elements_switcher = {index: element for index, element in enumerate(elements_switcher)}
        return 1
    else:
        return 2