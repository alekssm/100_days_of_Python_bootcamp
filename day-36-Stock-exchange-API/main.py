import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
RECEIVER_NUMBER = os.environ.get("RECEIVER_NUMBER")

AV_endpoint = "https://www.alphavantage.co/query"
NEWS_endpoint = "https://newsapi.org/v2/everything"

NEWS_api_key = os.environ.get("NEWS_API_KEY")
AV_api_key = os.environ.get("AV_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

AV_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_api_key,
}

NEWS_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_api_key,
    "language": "en",
}

def get_difference(current, previous):
    if current == previous:
        return 0
    try:
        return round((abs(current - previous) / previous) * 100., 2)
    except ZeroDivisionError:
        return float('inf')


AV_response = requests.get(AV_endpoint, params=AV_parameters)
AV_response.raise_for_status()
stock_data = AV_response.json()["Time Series (Daily)"]
data_list = [value for key,value in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

the_day_before_data = data_list[1]
the_open_day_before_closing_price = float(the_day_before_data["4. close"])

daily_difference = get_difference(yesterday_closing_price, the_open_day_before_closing_price)
up_down = None
if yesterday_closing_price >= the_open_day_before_closing_price:
    up_down = "⬆️"
else:
    up_down = "⬇️"

if daily_difference >= 5:
    NEWS_response = requests.get(NEWS_endpoint, params=NEWS_parameters)
    NEWS_response.raise_for_status()
    news_articles = NEWS_response.json()["articles"][:3]
    formated_articles = [f"{STOCK}: {up_down}{daily_difference}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=RECEIVER_NUMBER,
        )

