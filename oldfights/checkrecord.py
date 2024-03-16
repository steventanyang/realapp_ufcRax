import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

fighters = pd.read_csv('../fighter_data.csv')

fights = pd.read_csv('test.csv')

for _, fighter in fights.iterrows() :
    
    name = fighter['name']
    matches = 0
    kos = int(fighter['KO/TKO'])/100 
    subs = int(fighter['Submission'])/90 
    unam = int(fighter['Unanimous Decision'])/80 
    maj = int(fighter['Majority Decision'])/75
    split = int(fighter['Split Decision'])/70
    no = int(fighter['No Contest'])/50
    losses = int(fighter['Losses'])/25
    
    print("losses: " + str(losses))

    matches = kos + subs + unam + maj + split + no + losses
    print(matches)