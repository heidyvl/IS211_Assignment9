from bs4 import BeautifulSoup
import urllib2
import csv
import sys


page = urllib2.urlopen('https://finance.yahoo.com/quote/AAPL/history?ltr=1').read()

soup = BeautifulSoup(page, 'html.parser')

f = csv.writer(open("close_price.csv", "w"))

trs = soup.find_all('tr')

for tr in trs:

    spans = tr.find_all('span')
    try: 
        date = str(spans[0].get_text())
        closing = str(spans[4].get_text())
        
    except:
        continue 

    f.writerow ([date, closing])
