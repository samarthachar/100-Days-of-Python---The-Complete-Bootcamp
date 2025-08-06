#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

response = requests.get(url="https://api.sheety.co/b015b6a3e9c4aa92b59a4f62939c4cca/flightDeals/prices")

data = response.json()
sheet_data = data["prices"]
print(sheet_data)