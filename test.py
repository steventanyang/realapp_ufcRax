import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "http://ufcstats.com/fight-details/23a604f460289271"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#method
method_parent = soup.find('i', class_="b-fight-details__text-item_first")
method = method_parent.find_all('i')

if len(method) > 1:
    m = method[1].get_text(strip=True)
    print(m)
else:
    method = "Second method tag not found"


#winner, loser
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
    
    else : 
        print("wl error")

print("winner: " + winner)
print("loser: " + loser)
