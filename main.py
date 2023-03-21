from datetime import date, timedelta
import requests
from twilio.rest import Client

ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = 'PW5QDZUOXC7WH41Z'

params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'TSLA',
    'apikey': API_KEY
}

response = requests.get(ENDPOINT, params=params)
response.raise_for_status()
data = response.json()


def calculate_percentage(yesterday, day_before):
    diff = abs(float(yesterday) - float(day_before))
    percent = round(diff / float(day_before) * 100)
    return percent


today = date.today()

if today.weekday() == 0:
    prev_closing_day = today - timedelta(3)
    day_before_prev_closing_day = prev_closing_day - timedelta(days=1)
elif today.weekday() == 1:
    prev_closing_day = today - timedelta(1)
    day_before_prev_closing_day = prev_closing_day - timedelta(days=3)
else:
    prev_closing_day = today - timedelta(1)
    day_before_prev_closing_day = prev_closing_day - timedelta(days=1)

closing_price = data['Time Series (Daily)'][f'{prev_closing_day}']['4. close']
day_before_closing_price = data['Time Series (Daily)'][f'{day_before_prev_closing_day}']['4. close']

percentage = calculate_percentage(closing_price, day_before_closing_price)

if percentage >= 5:
    print('Get News')

# print(f'{prev_closing_day}')
# print(data['Time Series (Daily)'][f'{prev_closing_day}']['4. close'])
# print(data['Time Series (Daily)'][f'{day_before_prev_closing_day}'])
# print(today.weekday())
