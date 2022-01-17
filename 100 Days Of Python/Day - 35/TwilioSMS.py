from twilio.rest import Client
import requests
url= "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "#"
API_KEY = "#"
auth_token= "#"
client = Client(account_sid, auth_token)
data={
    "lat": 22.435801,
    "lon": 76.846313,
    "appid": API_KEY
}
data = requests.get(url=url,params=data)
data = data.json()
data = data["hourly"][:13]
value = False
for weather_data in data:
    if weather_data["weather"][0]['id']<700:
        value = True

if value:
    message = client.messages \
        .create(
                body="It's going to rain today, Umbrella lekar aana ☔",
                from_='#',
                to='#'
            )

else:
    message = client.messages \
    .create(
            body="Aasmaan saaf hai, Maje karo ☀️",
            from_='#',
            to='#'
        )
print(message.status)