# https://www.alphavantage.co/documentation/#time-series-data

import requests

def get_stock(ticker):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + ticker + "&interval=5min&apikey=demo"
    r = requests.get(url)
    data = r.json()

    return data