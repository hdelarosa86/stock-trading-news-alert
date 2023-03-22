import requests
import os

ENDPOINT = 'https://newsapi.org/v2/everything'
API_KEY = os.environ['NEWS_API_KEY']
COMPANY_NAME = 'Tesla Inc'

news_params = {
    'q':COMPANY_NAME,
    'apiKey': API_KEY,
}

response = requests.get(ENDPOINT, params=news_params)
response.raise_for_status()
news_articles = response.json()['articles']
