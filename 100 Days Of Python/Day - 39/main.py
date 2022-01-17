from data_manager import DataManager
from flight_search import FlightSearch
code_list = []
hello  = DataManager()
cities = hello.searchcity()
for city in cities:
    flight = FlightSearch(city)
    code_list.append(flight.get_iata())
hello.update_data(code_list)
flight.search_flights(code_list[3])
