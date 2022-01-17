import requests
import datetime as dt
import os


Excercise_URL= "https://trackapi.nutritionix.com/v2/natural/exercise"
exc = input("What exercise have you done today: ")
exc_data={
 "query":exc,
 "gender":"male",
 "weight_kg": os.environ.get('WEIGHT'),
 "height_cm": os.environ.get('HEIGHT'),
 "age": os.environ.get('AGE')
}
exc_headers={
    "x-app-id": os.environ.get('APP_ID'),
    "x-app-key": os.environ.get('APP_KEY'),
    "Content-Type": "application/json"
}
exc_response=requests.post(Excercise_URL, json=exc_data, headers=exc_headers).json()

today =dt.datetime.today()
date = today.strftime("%Y-%m-%d")
time= today.strftime("%H:%M:%S")
for exercise in exc_response["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
nutri_response = requests.post(url=os.environ.get('SHEETY_ENDPOINT'),json=sheet_inputs)
