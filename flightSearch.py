import requests
import os
from dotenv import load_dotenv
from flights import Flights

load_dotenv()

location_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
url_token = 'https://test.api.amadeus.com/v1/security/oauth2/token'
url_flight_offers = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


class FlightSearch:
    def __init__(self, myFlight: Flights):
        self.myFlight = myFlight
        self.key = os.getenv('API_Key')
        self.secret = os.getenv('API_Secret')


        self.headers_token = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.token_data = self.get_authorization_token()

        self.headers_flight_offers = {
            'Authorization': f'Bearer {self.token_data["access_token"]}'
        }


    def get_iata_code(self, city):
        params_city = {
            "keyword": city.upper()
        }


        city_iata_response = requests.get(location_url,
                                          params=params_city,
                                          headers=self.headers_flight_offers)


        city_iata_code = city_iata_response.json()['data'][0]['iataCode']
        return city_iata_code

    def get_authorization_token(self):
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.key,  # Replace with your client ID
            'client_secret': self.secret  # Replace with your client secret
        }

        response_token = requests.post(url_token, data=payload, headers=self.headers_token)
        token_data = response_token.json()

        return token_data

    def flight_information(self, cities, departure, returnDate):
        for city in cities:
            params = {
                'originLocationCode': 'ISB',
                'destinationLocationCode': city,
                'departureDate': departure.strftime('%Y-%m-%d'),
                'returnDate': returnDate.strftime('%Y-%m-%d'),
                'adults': 1,
                'max': 10
            }

            response_flight_offers = requests.get(url_flight_offers, params=params, headers=self.headers_flight_offers)

            # Check for errors
            if response_flight_offers.status_code != 200:
                print(f"Error: {response_flight_offers.status_code} - {response_flight_offers.text}")
            else:
                # Print the flight offers result

                self.myFlight.cheapest_flight(response_flight_offers.json(), city)
