from stocks import stock_data
from news import news_articles
from twilio.rest import Client
import os

STOCK_SYMBOL = 'TSLA'


def calculate_percentage(yesterday, day_before):
    diff = float(yesterday) - float(day_before)
    percent = round(diff / float(day_before) * 100)
    return percent


stocks_data_list = [value for (key, value) in stock_data.items()]

print(news_articles)
yesterday_closing_price = stocks_data_list[0]['4. close']
day_before_yesterday_closing_price = stocks_data_list[1]['4. close']

percentage = calculate_percentage(yesterday_closing_price, day_before_yesterday_closing_price)
up_or_down = None
if percentage > 0:
    up_or_down = '🔺'
else:
    up_or_down = '🔻'

if percentage > 4:
    top_three_articles = news_articles[:3]

    for article in top_three_articles:
        msg = f'{STOCK_SYMBOL}: {up_or_down}{abs(percentage)}%\n' \
              f'Headline: {article["title"]}\n' \
              f'Brief: {article["content"]}'
        print(msg)
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg,
            from_=os.environ['FROM_NUM'],
            to=os.environ['TO_NUM'],
        )
        print(message.sid)
