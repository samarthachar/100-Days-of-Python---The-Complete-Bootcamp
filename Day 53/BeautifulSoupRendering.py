from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

property_cards = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

links = []
prices = []
addresses = []

for property_card in property_cards:
    links.append(property_card.select("div.StyledPropertyCardPhotoBody a")[0]["href"])

    prices.append(property_card.select("span.PropertyCardWrapper__StyledPriceLine")[0].text.replace("/mo", "").split("+")[0])

    addresses.append(property_card.select("address")[0].text.strip())


