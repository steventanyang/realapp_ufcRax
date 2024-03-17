import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv('../ufc_fight_stat_data.csv')
df_sorted = df.sort_values(by='fight_url', ascending=True)
df_unique = df_sorted.drop_duplicates(subset='fight_url', keep='first')
df_final = df_unique.drop(df.columns.difference(['fight_url']), axis=1)


df_final.to_csv('sorted_fights.csv', index=False)



