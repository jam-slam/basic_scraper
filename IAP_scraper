import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
 
#Remove hashes below if you want to read URLs from a CSV    
#df = pd.read_csv('.csv') 
#URL_list = df.values.tolist()
#print(URL_list)

#Use this to test print out - remove '_2' to read from the orignal list above)
URL_list_2 = ['https://apps.apple.com/us/app/beat-maker-go-make-music/id1141835258',
              'https://apps.apple.com/us/app/deezer-music-podcast-player/id292738169']
 
IAP_overall = []
for url in URL_list_2:
    asp = requests.get(url)
    asp_parsed = BeautifulSoup(asp.content, "html.parser")
    IAP_list = []
    for IAP in asp_parsed.find_all("li", class_="list-with-numbers__item"):
        IAP_list.append(IAP.get_text())
        list_1 = [a.strip("\n") for a in IAP_list]
        clean_IAP_list = [b.split("\n") for b in list_1]
        clean_IAP_list.insert(0,url)
    IAP_overall.append(clean_IAP_list)
 
#Use for test, delete later
print(IAP_overall)

df = pd.DataFrame(IAP_overall)

#Save to CSV
df.to_csv('IAP.csv')
