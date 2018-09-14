import csv

f =open('fights.csv','a',newline='')
writer=csv.writer(f)

with open('fighters.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print (', '.join(row))