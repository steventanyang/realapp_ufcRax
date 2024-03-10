import requests
import pandas as pd
from bs4 import BeautifulSoup

fights = pd.read_csv('ufc_fight_stat_data.csv')
fighters = pd.read_csv('fighter_data.csv')

c = 0
for index, row in fights.iterrows():
    url = row['fight_url']

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    
    #finding winner and loser
    names = soup.find_all('div', class_='b-fight-details__person')
    winner = ""
    loser = ""

    for f in names :
        win_tag = f.find('i', class_='b-fight-details__person-status')

        if win_tag.get_text(strip=True) == 'W' :

            winner_raw = f.find('a', class_="b-fight-details__person-link")
            winner = winner_raw.text.strip()

        elif win_tag.get_text(strip=True) == 'L' :
            loser_raw = f.find('a', class_="b-fight-details__person-link")
            loser = loser_raw.text.strip()
        
        elif win_tag.get_text(strip=True) == "NC" :
            winner = "none"
            print("hit")
        
        else : 
            print("wl error")

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
    parent_round = soup.find('p', class_="b-fight-details__text")
    round_i_tags = parent_round.find_all('i', class_="b-fight-details__text-item")
    for i in round_i_tags :
        if i.find('i', class_="b-fight-details__label").get_text(strip=True) == "Time format:" :
            rounds = i.get_text(strip=True)

    rounds_split = rounds.split(':')[1]
    rounds_final = rounds_split[:1]

    # strikes
    strike_diff = 0
    parent_strike = soup.find('tbody', class_="b-fight-details__table-body")
    fighter_names_strike = parent_strike.find_all('a', class_="b-link_style_black")

    top = fighter_names_strike[0].get_text(strip=True)
    bottom = fighter_names_strike[1].get_text(strip=True)

    strike_num = parent_strike.find_all('td', class_="b-fight-details__table-col")
    # print(strike_num[2])

    top_strikes = strike_num[2].find_all('p', class_="b-fight-details__table-text")[0].get_text(strip=True)
    bottom_strikes = strike_num[2].find_all('p', class_="b-fight-details__table-text")[1].get_text(strip=True)

    top_s_final = top_strikes.split(" ")[0]
    bottom_s_final = bottom_strikes.split(" ")[0]

    strike_diff = abs(int(top_s_final) - int(bottom_s_final))


    if top_s_final > bottom_s_final :
        striker = top
    else :
        striker = bottom

    print(striker)
    print(strike_diff)
        

        
    






    