from stocks import stock_data
from news import news_articles
import requests
from twilio.rest import Client


def calculate_percentage(yesterday, day_before):
    diff = abs(float(yesterday) - float(day_before))
    percent = round(diff / float(day_before) * 100)
    return percent


stocks_data_list = [value for (key, value) in stock_data.items()]

print(stocks_data_list)
yesterday_closing_price = stocks_data_list[0]['4. close']
day_before_yesterday_closing_price = stocks_data_list[1]['4. close']

percentage = calculate_percentage(yesterday_closing_price, day_before_yesterday_closing_price)

if percentage >= 2:
    print('Get News')
