import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "3LE7DWFICHJG5R0N"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "a0dec2f37b91431f9f3ba1546973e468"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY

}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percentage_difference = (difference / float(yesterday_closing_price)) * 100
if percentage_difference > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    response = requests.get(url=NEWS_ENDPOINT, params = news_parameters)
    articles = response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        print(article)


