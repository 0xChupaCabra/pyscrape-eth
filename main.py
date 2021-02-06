from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from boltons import iterutils
import csv
import time

site= "https://etherscan.io/token/generic-tokenholders2?a=0x622f2962ae78e8686ecc1e30cf2f9a6e5ac35626&s=0&p="

tablerows = []

pagen = 0
while pagen <= 10000:
    pagen += 1
    site= "https://etherscan.io/token/generic-tokenholders2?a=0x622f2962ae78e8686ecc1e30cf2f9a6e5ac35626&s=0&p="+str(pagen)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    table = soup.findAll("table")
    rows = table[0].findChildren(['th', 'tr'])
    time.sleep(2)
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            rows_2 = []
            value = cell.string
            if value == 'There are no matching entries':
                break
            else:
                tablerows.append(value)
                

newlist = iterutils.chunked(tablerows, 6)
print(newlist)

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newlist)
