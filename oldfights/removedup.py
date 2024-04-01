import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


fights = pd.read_csv('all_fights.csv')
fights_cleaned = fights.drop_duplicates(subset=['fight_url'])

sorted = fights_cleaned.sort_values(by="fight_url", ascending=False)

sorted.to_csv("all_fights.csv", index=False)