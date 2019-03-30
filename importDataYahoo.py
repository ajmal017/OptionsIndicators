## Fetching data from yahoo finance

from urllib.request import urlopen
from bs4 import BeautifulSoup

optionsURL = 'https://finance.yahoo.com/quote/TSLA/options?p=TSLA'
optionsPage = urlopen(optionsURL)
htmldata = BeautifulSoup(optionsPage)

## trying to fetch the html data
temp = htmldata.find("table")