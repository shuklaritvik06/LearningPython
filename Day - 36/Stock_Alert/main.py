import requests
import os
from twilio.rest import Client
import random

def calc_pecent(yesterday_data,day_before_yest_data):
    yesterday_data = float(yesterday_data)
    day_before_yest_data = float(day_before_yest_data)
    data_percentage = float("{:.2f}".format((abs(yesterday_data-day_before_yest_data)*100)/yesterday_data))
    return data_percentage

datas= []
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype":"json",
    "apikey": os.environ.get("STOCK_API_KEY"),
}
news_params = {
    "apiKey": os.environ.get("NEWS_API_KEY"),
    "qInTitle": COMPANY_NAME
}
stock_data = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
news_data = requests.get(url="https://newsapi.org/v2/everything",params=news_params)
print(news_data.text)
data = stock_data.json()["Time Series (Daily)"]
for value in data.values():
    datas.append(value)
    
yesterday_data = float(datas[0]['4. close'])
day_before_yest_data = float(datas[1]['4. close'])
article_data = news_data.json()["articles"]
news = article_data[:3]
price_percentage = calc_pecent(yesterday_data,day_before_yest_data)
if yesterday_data < day_before_yest_data:
    stock_price = f"TSLA: 🔻{price_percentage}"
    index = random.randint(0,2)
    news_title = news[index]["title"]
    news_description = news[index]["description"]
    url = news[index]["url"]
    client = Client(os.environ.get("account_sid"),os.environ.get("auth_token"))
    message = client.messages \
                    .create(
                        body=f"{stock_price}\nHeadline: {news_title}\nBrief: {news_description}\nRead more: {url}",
                        from_='',
                        to=''
                    )


else:
    stock_price = f"TSLA: 🔺{price_percentage}"
    index = random.randint(0,2)
    client = Client(os.environ.get("account_sid"),os.environ.get("auth_token"))
    news_title = news[index]["title"]
    news_description = news[index]["description"]
    url = news[index]["url"]
    message = client.messages \
                    .create(
                        body=f"{stock_price}\nHeadline: {news_title}\nBrief: {news_description}\nRead more: {url}",
                        from_='',
                        to=''
                    )

print(message.status)
