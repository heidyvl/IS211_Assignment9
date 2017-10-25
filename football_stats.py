from bs4 import BeautifulSoup
import urllib2
import csv
import sys


page = urllib2.urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns').read()
soup = BeautifulSoup(page, 'html.parser')

f = csv.writer(open("football.csv", "w"))
f.writerow(["Player", "POS", "Team", "Total Touchdowns"]) 
trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    try: 
        player = str(tds[0].get_text()) 
        pos = str(tds[1].get_text())
        team = str(tds[2].get_text())
        td = int(tds[7].get_text()) + int(tds[10].get_text())

    except:
        continue 

    f.writerow ([player, pos, team, td])
