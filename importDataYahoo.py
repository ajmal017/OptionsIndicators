## Fetching data from yahoo finance

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timezone


## convert to function
def convertTimeStamp(date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    return int(dt.replace(tzinfo=timezone.utc).timestamp())


## inputs are symbol and date
# output will be a list of 2 dataframes.. for put & call respectively

def getOptionsData(ticker = 'AAPL' , expDate = None):
    optionsURL = 'https://finance.yahoo.com/quote/' + ticker + '/options?p=' + ticker

    # if date is none.. return the most recent options data.. else filter for date
    if expDate != None:
        expDate  = convertTimeStamp(expDate)
        optionsURL = optionsURL + '&date=' + str(expDate)


    optionsPage = urlopen(optionsURL)
    htmldata = BeautifulSoup(optionsPage)

    ## Trying to fetch the html data
    temp = htmldata.find("table")

    headings = [th.get_text() for th in temp.find("tr").find_all("th")]

    datasets = pd.DataFrame()
    for row in temp.find_all("tr")[1:]:
        dataset = pd.Series(td.get_text() for td in row.find_all("td"))
        datasets = datasets.append(dataset, ignore_index=True)

    datasets.columns = ['ContractName', 'LastTradeDate', 'Strike', 'LastPrice', 'Bid', 'Ask', 'Change', 'PctChange',
                        'Volume', 'OpenInterest', 'ImpliedVolatility']
    return datasets





