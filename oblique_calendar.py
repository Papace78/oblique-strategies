import pandas as pd
import time
import requests

from bs4 import BeautifulSoup

url = 'https://stoney.sb.org/eno/oblique.html'

strategies = pd.DataFrame()

iteration = 0
while len(strategies) < 365 and iteration < 1200:
    iteration +=1

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    strategies = pd.concat([strategies , \
            pd.DataFrame({"Oblique_strategies": [soup.find(name='h3').string]})],\
            ignore_index = True).drop_duplicates()

    time.sleep(3)


strategies.to_csv('csv/oblique_strategies_calendar.csv')
