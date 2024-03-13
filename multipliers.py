import requests
import pandas as pd
from bs4 import BeautifulSoup

data = pd.read_csv('final_values.csv')

data['Common'] = data.apply(lambda row: int(round(row["Value"] * 1.2)), axis=1)
data['Uncommon'] = data.apply(lambda row: int(round(row["Value"] * 1.4)), axis=1)
data['Rare'] = data.apply(lambda row: int(round(row["Value"] * 1.6)), axis=1)
data['Epic'] = data.apply(lambda row: int(round(row["Value"] * 2.0)), axis=1)
data['Legendary'] = data.apply(lambda row: int(round(row["Value"] * 2.5)), axis=1)
data['Mystic'] = data.apply(lambda row: int(round(row["Value"] * 4.0)), axis=1)
data['Iconic'] = data.apply(lambda row: int(round(row["Value"] * 6.0)), axis=1)

sorted = data.sort_values(by='Value', ascending=False)

sorted.to_csv('test.csv', index=False)
