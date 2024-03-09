import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "http://ufcstats.com/fight-details/3b020d4914b44fc8"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
