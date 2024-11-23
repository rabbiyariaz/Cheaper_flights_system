import requests
import os
from dotenv import load_dotenv

load_dotenv()


class IATA_DATA:
    def __init__(self):
        self.headers_token_sheety = {
            "Authorization": os.getenv('content_type')
        }

    def get_data_from_sheety(self):
        response = requests.get(os.getenv('url_sheety'), headers=self.headers_token_sheety)
        print(response.text)
        json_response = response.json()
        data_from_sheety = json_response['sheet1']

        return data_from_sheety

    def data_to_sheety(self, code, id):
        iata_data_to_sheety = {
            "sheet1": {
                "iataCode": code
            }
        }
        sheety_response_data = requests.put(f"{os.getenv('url_sheety')}/{id}", json=iata_data_to_sheety,
                                            headers=self.headers_token_sheety)
