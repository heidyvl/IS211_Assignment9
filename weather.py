from bs4 import BeautifulSoup
import urllib2
import csv
import sys


page = urllib2.urlopen('http://www.wunderground.com/history/airport/KNYC/2015/1/4/MonthlyHistory.html').read()
highlist = []
soup = BeautifulSoup(page, 'html.parser')

f = csv.writer(open("weather.csv", "w"))
f.writerow(["Jan", "High", "Avg", "Low"])

trs = soup.find_all('tr')

for tr in trs:
    
    td = tr.find_all('td')
    
    span = tr.find_all('span')
    try: 
        date = str(td[0].get_text())
        
        high = int(span[0].get_text()[0:2])
        avg = str(span[1].get_text())
        low = str(span[2].get_text())

       
    except:
        continue 

    f.writerow([date, high, avg, low])
