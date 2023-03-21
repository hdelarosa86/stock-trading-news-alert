import requests

ENDPOINT = 'https://newsapi.org/v2/everything'
API_KEY = '7af914166ad2419c8a63bef343e3fc50'
COMPANY_NAME = 'Tesla Inc'

news_params = {
    'q':COMPANY_NAME,
    'apiKey': API_KEY,
}

response = requests.get(ENDPOINT, params=news_params)
response.raise_for_status()
news_articles = response.json()['articles']
