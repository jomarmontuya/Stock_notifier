import requests
from twilio.rest import Client


# Inititate Constant
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query?"
TIME_SERIES = "GLOBAL_QUOTE"
NEWS_API_ENDPOINT = "http://newsapi.org/v2/everything?"


class Stock:
    def __init__(self, apikey, stock_symbol):
        """Argument Must Include Alphavantage API KEY"""
        self.stock_data = None
        self.stock_resp = None
        self.stock_params = {
            "function": TIME_SERIES,
            "symbol": stock_symbol,
            "apikey": apikey,
            "datatype": "json"
        }

    def get_data(self):
        self.stock_resp = requests.get(STOCK_API_ENDPOINT, params=self.stock_params)
        self.stock_resp.raise_for_status()
        self.stock_data = self.stock_resp.json()
        return self.stock_data

    def get_news(self, news_api_key, company):
        """ Must have news api key as argument """
        news_params = {
            "q": company,
            "apiKey": news_api_key
        }

        news_resp = requests.get(NEWS_API_ENDPOINT, params=news_params)
        news_resp.raise_for_status()
        news_data = news_resp.json()
        return news_data


class SMS:
    def __init__(self, account_sid, account_token):
        self.client = Client(account_sid, account_token)

    def send(self, from_phone, to_phone, msg):
        """From Phone number , To Phone number , Message"""
        message = self.client.messages \
            .create(
            body=msg,
            from_=from_phone,
            to=to_phone
        )
        print(message.status)
