# ENDPOINT?PARAM=KEY&PARAM=KEY.....

import requests
MY_LAT = 36.7201600
MY_LONG = -4.4203400
myparams={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0
}
data = requests.get(url="https://api.sunrise-sunset.org/json", params=myparams)
data = data.json()
print(data["results"]["sunrise"].split("T"))
print(data["results"]["sunset"].split("T"))