

class Flights:
    def __init__(self):
        pass

    def cheapest_flight(self, json_data_flights, sheety_data):
        lowest_price = 10000000
        count = 0
        departure = []
        arrival = []
        message = ""
        data = json_data_flights['data']
        out_date = []
        arrival_time = []
        departure_time = []

        for rec in data:
            price = float(rec['price']['grandTotal'])
            if lowest_price > price:
                lowest_price = price

                for stops in rec['itineraries'][0]['segments']:
                    departure.append(stops['departure']['iataCode'])  # ISB [ISB,GYD]
                    arrival.append(stops['arrival']['iataCode'])  # GYD [GYD,CDG]
                    out_date.append(stops["departure"]["at"].split("T")[0])  # [2024-08-18]
                    departure_time.append(stops["departure"]["at"].split("T")[1])  # [2:00]
                    arrival_time.append(stops["arrival"]["at"].split("T")[1])  # [5:30:00]
                    message += f"Your flight is scheduled to depart from '{departure[count]}' on {out_date[count]}, and will arrive on '{arrival[count]}' the same day.The departure is set for {departure_time[count]}, with an estimated arrival at {arrival_time[count]}.\n"
                    arrival_compare = arrival[count]
                    count += 1

            for data in sheety_data:
                if lowest_price < data['lowestPrice']:
                    print(message)
                    break
