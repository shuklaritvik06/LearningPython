import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities=[]
        self.url=os.environ.get('URL')
        self.response = requests.get(url=self.url).json()
    def searchcity(self):
        for i in self.response["prices"]:
            self.cities.append(i["city"])
        return self.cities
    def update_data(self,codes):
        j=2 
        for i in codes:
            put_url = f"{self.url}/{j}"
            data = {
                "price":{
                    "iataCode": i
                }
            }
            requests.put(url = put_url,json=data)
            j+=1
            