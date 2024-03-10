import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "http://ufcstats.com/fight-details/b8b9a8e504d51ba5"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# strikes

strike_diff = 0
parent_strike = soup.find('tbody', class_="b-fight-details__table-body")
fighter_names_strike = parent_strike.find_all('a', class_="b-link_style_black")

top = fighter_names_strike[0].get_text(strip=True)
bottom = fighter_names_strike[1].get_text(strip=True)


#rounds

# rounds = ""
# parent_round = soup.find('p', class_="b-fight-details__text")
# round_i_tags = parent_round.find_all('i', class_="b-fight-details__text-item")
# for i in round_i_tags :
#     if i.find('i', class_="b-fight-details__label").get_text(strip=True) == "Time format:" :
#         rounds = i.get_text(strip=True)

# n = rounds.split(':')[1]
# final = n[:1]

# print(rounds)
# print(final)

# #method
# method_parent = soup.find('i', class_="b-fight-details__text-item_first")
# method = method_parent.find_all('i')

# if len(method) > 1:
#     m = method[1].get_text(strip=True)
#     print(m)
# else:
#     method = "Second method tag not found"


# #winner, loser
# names = soup.find_all('div', class_='b-fight-details__person')
# winner = ""
# loser = ""

# for f in names :
#     win_tag = f.find('i', class_='b-fight-details__person-status')

#     if win_tag.get_text(strip=True) == 'W' :

#         winner_raw = f.find('a', class_="b-fight-details__person-link")
#         winner = winner_raw.text.strip()

#     elif win_tag.get_text(strip=True) == 'L' :
#         loser_raw = f.find('a', class_="b-fight-details__person-link")
#         loser = loser_raw.text.strip()
    
#     elif win_tag.get_text(strip=True) == "NC" :
#         winner = "none"
    
#     else : 
#         print("wl error")

# print("winner: " + winner)
# print("loser: " + loser)
