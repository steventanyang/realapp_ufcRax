import requests
import pandas as pd
from bs4 import BeautifulSoup

fights = pd.read_csv('ufc_fighter_data.csv')
fighters = {}

c = 0
for index, row in fights.iterrows():
    url = row['fighter_url']

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #name
    name_raw = soup.find('span', class_='b-content__title-highlight')
    name = name_raw.text.strip()

    #record
    record = soup.find('span', class_='b-content__title-record')

    record_text = record.get_text() 
    record_parts = record_text.replace("Record: ", "").split('-')

    wins = int(record_parts[0])
    losses = int(record_parts[1])

    fighters[name] = {
        'name': name,
        'wins': wins,
        'losses': losses
    }
    c += 1
    print(c)

final = []

counter = 0
for name, fighter in fighters.items() :
    final.append({'name': name, 'wins': fighter['wins'], 'losses': fighter['losses']})
    counter += 1
    print(str(counter) + " " + name)

df = pd.DataFrame(final)
df.to_csv(f'fighter_data.csv', index=False)





    