import requests
import pandas as pd
from bs4 import BeautifulSoup

fights = pd.read_csv('ufc_fight_stat_data.csv')

for index, row in fights.iterrows():
    url = row['fight_url']
    print(url)


    
    