import requests

API_KEY = "e6715e3d0be2051b20d840a223de64fd"
MY_LAT = -26.8000 #51.395962
MY_LONG = 168.6000 #-0.448930

def get_weather_info():
    weather_list = []
    for index in range(0,5):
        data_id = data["list"][index]["weather"][0]["id"]
        if data_id < 700:
            weather_list.append(index)


    return bool(weather_list), weather_list


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 5,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
is_raining = get_weather_info()
print_str = "Bring an umbrella, raining between: "
if is_raining[0]:
    for index in range(0, len(is_raining[1])):
        if is_raining[1][index] == 0:
            rain_time = "06:00 to 09:00"
        elif is_raining[1][index] == 1:
            rain_time = "09:00 to 12:00"
        elif is_raining[1][index] == 2:
            rain_time = "12:00 to 15:00"
        elif is_raining[1][index] == 3:
            rain_time = "15:00 to 18:00"
        elif is_raining[1][index] == 4:
            rain_time = "15:00 to 18:00"
        else:
            rain_time = None

        print_str += f"\n- {rain_time}"




