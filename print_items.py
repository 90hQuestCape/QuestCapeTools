from bs4 import BeautifulSoup
import os

for filename in os.listdir('guides'):
    print '------' + filename + '------'
    with open('guides/' + filename) as f:
        raw = f.read()

    try:
        soup = BeautifulSoup(raw, "html.parser")

        table = soup.findAll("table", {"class": "questdetails"})[0]
        tds = table.findAll("td", {"class": "questdetails-info"})

        print "Items Required", tds[5].get_text()
    except Exception:
        print "Failed :("       
