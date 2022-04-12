import requests
import datetime as dt
import smtplib
import time

MY_LAT = 25.442190 
MY_LONG = 81.840919 
MY_EMAIL = 'my@example.com'
MYPASSWORD = 'mypassword'
RECIEVER_EMAIL = 'email@email.com'
SENDER_EMAIL = 'sender@example.com'

data = requests.get(url="http://api.open-notify.org/iss-now.json")
data.raise_for_status()
data = data.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
response = response.json()
sunrise = int(response["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()

if iss_latitude-5<= MY_LAT <= iss_latitude+5 and iss_longitude-5<= MY_LONG<=iss_longitude+5:
    if time_now.hour > sunset and time_now.hour<sunrise:
        while True:
            time.sleep(60)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MYPASSWORD)
                connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=RECIEVER_EMAIL,msg="Subject:ISS is here!!\n\nCome out for ISS!!")




