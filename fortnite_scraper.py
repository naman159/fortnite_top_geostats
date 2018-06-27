#Data Scraped from Fortnitetracker.com

import requests
from bs4 import BeautifulSoup
import csv

filename = 'fortnite500.csv'
f = open(filename, 'w', encoding = "utf-8")
headers = "Rank, Name, Platform, Country, Wins, Games\n"
f.write(headers)

for i in range(5):
	myurl = 'https://fortnitetracker.com/leaderboards/pc/Top1?mode=all&page='+str(i+1)

	r = requests.get(myurl)
	soup = BeautifulSoup(r.content,'html.parser')

	containers = soup.find_all("tr",{"trn-table__row trn-lb-entry trn-lb-entry--top3"})

	for container in containers:
		#SR No.
		sr = container.td.contents[0]
		#Name
		name = container.a.contents[0]
		#Platform
		pfstr = str(container.span.contents[0])
		if(pfstr == '<i class="ion-social-windows"></i>'):
			platform = 'Windows'
		elif(pfstr == '<i class="ion-playstation"></i>'):
			platform = 'PlayStation'
		else:
			platform = 'XBox'
		#Country
		country = str(container.img)[98:100]
		#Wins&Games
		ab = container.find_all("td",{"class":"trn-lb-entry__stat trn-text--right"})
		wins = ab[0].contents[0]
		games = ab[1].contents[0]

		f.write(sr + "," + name + "," + platform + "," + country + "," + wins.replace(',','') + "," + games + "\n")


	containers = soup.find_all("tr",{"class":"trn-table__row trn-lb-entry "})

	for container in containers:
		#SR No.
		sr = container.td.contents[0]
		#Name
		name = container.a.contents[0]
		#Platform
		pfstr = str(container.span.contents[0])
		if(pfstr == '<i class="ion-social-windows"></i>'):
			platform = 'Windows'
		elif(pfstr == '<i class="ion-playstation"></i>'):
			platform = 'PlayStation'
		else:
			platform = 'XBox'
		#Country
		country = str(container.img)[98:100]
		#Wins&Games
		ab = container.find_all("td",{"class":"trn-lb-entry__stat trn-text--right"})
		wins = ab[0].contents[0]
		games = ab[1].contents[0]

		f.write(sr + "," + name + "," + platform + "," + country + "," + wins.replace(',','') + "," + games + "\n")

f.close()
