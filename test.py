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

# print(striker)
# print(strike_diff)


# rounds
rounds = ""
parent_round = soup.find('p', class_="b-fight-details__text")
round_i_tags = parent_round.find_all('i', class_="b-fight-details__text-item")
for i in round_i_tags :
    if i.find('i', class_="b-fight-details__label").get_text(strip=True) == "Time format:" :
        rounds = i.get_text(strip=True)

n = rounds.split(':')[1]
final = n[:1]

# print(rounds)
# print(final)

#method
method_parent = soup.find('i', class_="b-fight-details__text-item_first")
method = method_parent.find_all('i')

if len(method) > 1:
    m = method[1].get_text(strip=True)
    # print(m)
else:
    m = "Second method tag not found"

# KO/TKO , Submission , Decision - Unanimous , Decision - Majority , Decision - Split , No Contest 

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


print("more strikes: " + striker)
print("strik_diff: " + str(strike_diff))

print("rounds: " + final)

print("method: " + m)

print("winner: " + winner)
print("loser: " + loser)

result = {}
# KO/TKO , Submission , Decision - Unanimous , Decision - Majority , Decision - Split , No Contest 
if winner in result :
    if m == "KO/TKO" :
        result[winner]["KO/TKO"] += 100
    elif m == "Submission" :
        result[winner]["Submission"] += 90
    elif m == "Decision - Unanimous" :
        result[winner]["Unanimous Decision"] += 80
    elif m == "Decision - Majority" :
        result[winner]["Majority Decision"] += 75
    elif m == "Decision - Split" :
        result[winner]["Split Decision"] += 70
    elif m == "No Contest" :
        result[winner]["No Contest"] += 50

    if rounds == '5':
        result[winner]["5roundBonus"] += 25
        print("5 rounder")

    if winner == striker :
        result[winner]["StrikeBonus"] += strike_diff


else :
    result[winner] = {
        "KO/TKO": 0,
        "Submission": 0,
        "Unanimous Decision": 0,
        "Majority Decision": 0,
        "Split Decision": 0,
        "No Contest": 0,
        "Losses": 0,
        "StrikeBonus": 0,
        "5roundBonus": 0
    }

    if m == "KO/TKO":
        result[winner]["KO/TKO"] += 100
    elif m == "Submission":
        result[winner]["Submission"] += 90
    elif m == "Decision - Unanimous":
        result[winner]["Unanimous Decision"] += 80
    elif m == "Decision - Majority":
        result[winner]["Majority Decision"] += 75
    elif m == "Decision - Split":
        result[winner]["Split Decision"] += 70
    elif m == "No Contest":
        result[winner]["No Contest"] += 50

    if rounds == '5':
        result[winner]["5roundBonus"] += 25
        print("5 rounder")

    if winner == striker :
        result[winner]["StrikeBonus"] += strike_diff

    

if loser in result :
    result[loser]["Losses"] += 25

    if rounds == '5':
        result[loser]["5roundBonus"] += 25
        print("5 rounder")

    if loser == striker :
        result[loser]["StrikeBonus"] += strike_diff

else :
    result[loser] = {
        "KO/TKO": 0,
        "Submission": 0,
        "Unanimous Decision": 0,
        "Majority Decision": 0,
        "Split Decision": 0,
        "No Contest": 0,
        "Losses": 25,
        "StrikeBonus": 0,
        "5roundBonus": 0
    }

    if rounds == '5':
        result[loser]["5roundBonus"] += 25
        print("5 rounder")

    if loser == striker :
        result[loser]["StrikeBonus"] += strike_diff



