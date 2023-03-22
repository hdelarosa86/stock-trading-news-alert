import requests
import os
STOCK = 'TSLA'
ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = os.environ['ALPHAVANTAGE_API_KEY']

stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': API_KEY
}

response = requests.get(ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
