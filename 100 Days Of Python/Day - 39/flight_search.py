import requests
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,city):
        self.city = city
        Url="https://tequila-api.kiwi.com/locations/query"
        self.header={
            "apikey": os.environ.get("API_KEY")
        }
        self.params={
            "term": f"{self.city}",
            "location_types": "city"
        }
        self.response = requests.get(url=Url,params=self.params,headers = self.header).json()


    def get_iata(self):
        self.iata_code = self.response["locations"][0]["code"]
        return self.iata_code
        pass

    def search_flights(self,city):
        self.dest = city
        search_url = "https://tequila-api.kiwi.com/v2/search"
        data={
            "fly_from": "DEL",
            "fly_to": f"{self.dest}",
            "date_from": "04/12/2021",
            "date_to": "04/6/2022"
        }
        search_result = requests.get(url=search_url,params=data,headers=self.header)
        with open("data.txt","w") as f:
            f.write(search_result.text)
