import requests
import pandas as pd
from bs4 import BeautifulSoup

fights = pd.read_csv('ufc_fighter_data.csv')
fighters = pd.read_csv('fighter_data.csv')

c = 0
for index, row in fights.iterrows():
    url = row['fight_url']

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    
    #finding winner
    names = soup.find('span', class_='b-fight-details__person')
    winner = ""
    for f in names :
        win_tag = f.find('i', class_='b-fight-details__person-status')
        if win_tag.get_text() == 'W' :

            winner_raw = f.find('a', class_="b-fight-details__person-link")
            winner = winner_raw.text.strip()
        
        elif win_tag.get_text(strip=True) == "NC" :
            winner = "none"

    #finding method 
    method_final = ""
    if not winner == "none" :
        method_parent = soup.find('i', class_="b-fight-details__text-item_first")
        method = method_parent.find_all('i')

        if len(method) > 1:
            method_final = method[1].get_text(strip=True)
            print(method_final)
        else:
            method = "Second method tag not found"

    else :
        method = "No Contest"

    #finding rounds
    rounds = ""

    #strike diff
    sig_strik_diff = ""
        

        
    






    