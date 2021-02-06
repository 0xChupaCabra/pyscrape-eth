from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from boltons import iterutils
import csv
import time

site= "https://etherscan.io/token/generic-tokenholders2?a=0x622f2962ae78e8686ecc1e30cf2f9a6e5ac35626&s=0&p="

tablerows = []
a = True
pagen = 0
while a == True:
    pagen += 1
    site= "https://etherscan.io/token/generic-tokenholders2?a=0x622f2962ae78e8686ecc1e30cf2f9a6e5ac35626&s=0&p="+str(pagen)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "lxml")
    table = soup.findAll("table")
    rows = table[0].findChildren(['th', 'tr'])
    print("fetching page" + str(pagen))
    time.sleep(2)
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            rows_2 = []
            value = cell.string
            if value == 'There are no matching entries':
                a = False
                break
            else:
                tablerows.append(value)

newlist = iterutils.chunked(tablerows, 6)

for x in newlist:
    del x[-3:]
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(newlist)
