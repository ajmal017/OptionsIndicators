## Fetching data from yahoo finance

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

## convert to function
## inputs are symbol and date
# output will be a list of 2 dataframes.. for put & call respectively

optionsURL = 'https://finance.yahoo.com/quote/TSLA/options?p=TSLA'
optionsPage = urlopen(optionsURL)
htmldata = BeautifulSoup(optionsPage)

## trying to fetch the html data
temp = htmldata.find("table")

headings = [th.get_text() for th in temp.find("tr").find_all("th")]

datasets = pd.DataFrame()
for row in temp.find_all("tr")[1:]:
    dataset =pd.Series(td.get_text() for td in row.find_all("td"))
    print(dataset)
    datasets = datasets.append(dataset,ignore_index= True)

datasets.columns = ['ContractName','LastTradeDate','Strike','LastPrice','Bid','Ask','Change','PctChange',
                   'Volume'	,'OpenInterest','ImpliedVolatility']

