import requests
url = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
data={
    "lat": 22.435801,
    "lon": 76.846313,
    "appid": API_KEY
}
data = requests.post(url=url,params=data)
data = data.json()
data = data["hourly"][:13]
for weather_data in data:
    if weather_data["weather"][0]['id']<700:
        print("Bring an Umbrella")
    else:
        print("It's clear today!")