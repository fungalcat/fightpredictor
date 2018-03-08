import requests
from bs4 import BeautifulSoup

source = requests.get('http://www.fightmetric.com/event-details/7929be8290289a47').text

soup = BeautifulSoup(source, 'lxml')

body = soup.find('tbody')
flag=0
fights=[[],[]]

#testing
all_stats=[]
links = body.find_all('a',class_='b-link b-link_style_black')
for link in links:
	source2 = requests.get(link['href']).text
	soup2 = BeautifulSoup(source2, 'lxml')
	container = soup2.find('div',class_='b-list__info-box b-list__info-box_style_small-width js-guide')
	stats=[]
	container = soup2.find_all('li',class_='b-list__box-list-item b-list__box-list-item_type_block')
	for thing in container:
		stats.append(thing.text[27:].strip())
	stats.pop(9)
	print(stats)
	all_stats.append(stats)



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
