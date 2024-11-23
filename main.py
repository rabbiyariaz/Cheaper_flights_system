import requests
from flight_iata_data import IATA_DATA
from flightSearch import FlightSearch
from flights import Flights
from datetime import datetime, timedelta
import os

cities_id = 2
my_flight = Flights()
data_manager = IATA_DATA()
destination_cities_list = data_manager.get_data_from_sheety()
flight_data = FlightSearch(my_flight)

presentday = datetime.now()
departure = presentday + timedelta(1)
return_date = presentday + timedelta(30)

cities_list = []
for destination_city in destination_cities_list:
    iata_city_code = flight_data.get_iata_code(destination_city['city'])
    cities_list.append(iata_city_code)
    data_manager.data_to_sheety(iata_city_code, cities_id)
    cities_id += 1

cities_list = ['PAR', 'BRN', 'SEL', 'ROM', 'KHI']
flights = flight_data.flight_information(cities_list, departure, return_date)
