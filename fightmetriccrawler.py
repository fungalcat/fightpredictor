import requests
from bs4 import BeautifulSoup
import time
from random import randint
#events page
source = requests.get('http://www.fightmetric.com/statistics/events/completed').text

soup = BeautifulSoup(source, 'lxml')


all_stats=[]
#list of events
links = soup.find_all('a',class_='b-link b-link_style_black')
for link in links:
	#individual event
	source2 = requests.get(link['href']).text
	soup2 = BeautifulSoup(source2, 'lxml')
	links2 = soup2.find_all('a',class_='b-link b-link_style_black')
	#list of fighters
	for link2 in links2:
		#individual fighter
		source3 = requests.get(link2['href']).text
		soup3 = BeautifulSoup(source3, 'lxml')
		stats=[]
		container3 = soup3.find_all('li',class_='b-list__box-list-item b-list__box-list-item_type_block')
		for thing in container3:
			stats.append(thing.text[27:].strip())
		stats.pop(9)
		print(stats)
		all_stats.append(stats)
		time.sleep(randint(5,15))
	time.sleep(randint(5,15))



#finds all the fighters, third loop is to skip random a tags
# for a in body.find_all('a')[1:]:
	
# 	fighter = a.text.strip()
# 	f_data =[]
# 	if flag==0:
# 		fights[flag].append(fighter)
# 		flag = 1
# 	elif flag==1:
# 		fights[flag].append(fighter)
# 		flag = 2
# 	else:
# 		flag=0

# print(fights)
