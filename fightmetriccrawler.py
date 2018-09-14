import requests
from bs4 import BeautifulSoup
import time
from random import randint
import csv

f =open('fighters1.csv','a',newline='')

for i in range(2,6):
	#events page
	source = requests.get('http://www.fightmetric.com/statistics/events/completed?page='+str(i)).text

	soup = BeautifulSoup(source, 'lxml')

	writer=csv.writer(f)
	#list of events
	links = soup.find_all('a',class_='b-link b-link_style_black')

	#pops upcoming event
	if i == 1:
		links = links[0:]
	for link in links:
		#individual event
		source2 = requests.get(link['href']).text
		soup2 = BeautifulSoup(source2, 'lxml')
		links2 = soup2.find_all('a',class_='b-link b-link_style_black')
		#list of fighters
		time.sleep(2)
		for link2 in links2:
			#individual fighter
			source3 = requests.get(link2['href']).text
			soup3 = BeautifulSoup(source3, 'lxml')
			stats=[]
			#gets name
			name = soup3.find('span', class_='b-content__title-highlight').text
			record = soup3.find('span', class_='b-content__title-record').text
			stats.append(name.strip())
			stats.append(record.strip())
			container3 = soup3.find_all('li',class_='b-list__box-list-item b-list__box-list-item_type_block')
			for thing in container3:
				stats.append(thing.text[27:].strip())
			stats.pop(9)
			print(stats)
			writer.writerow(stats)
			time.sleep(randint(1,5))
	time.sleep(3)

f.close()


