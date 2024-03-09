import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "http://ufcstats.com/fight-details/b8b9a8e504d51ba5"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

method_parent = soup.find('i', class_="b-fight-details__text-item_first")
method = method_parent.find_all('i')

if len(method) > 1:
    m = method[1].get_text(strip=True)
    print(m)
else:
    method = "Second method tag not found"


