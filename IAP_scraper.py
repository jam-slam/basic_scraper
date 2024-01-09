import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
 
#Remove hashes below if you want to read URLs from a CSV    
#df = pd.read_csv('.csv') 
#app_store_urls = df.values.tolist()
#print(app_store_urls)

app_store_urls = ['https://apps.apple.com/us/app/beat-maker-go-make-music/id1141835258',
              'https://apps.apple.com/us/app/deezer-music-podcast-player/id292738169']
 
iap_list = []
for urls in app_store_urls:
    asp = requests.get(urls)
    asp_parsed = BeautifulSoup(asp.content, "html.parser")
    iap_list = []
    for iaps in asp_parsed.find_all("li", class_="list-with-numbers__item"):
        iap_list.append(IAP.get_text())
        list_1 = [a.strip("\n") for a in IAP_list]
        clean_iap_list = [b.split("\n") for b in list_1]
        clean_iap_list.insert(0,url)
    iap_final.append(clean_IAP_list)
 
#Use for test, delete later
print(iap_final)

df = pd.DataFrame(iap_final)

#Save to CSV
df.to_csv('IAP.csv')
