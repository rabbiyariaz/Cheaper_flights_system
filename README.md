# Cheaper_flights_system
This project is a flight price tracking system that integrates the Amadeus Flight API and Sheety API. 
It retrieves flight information for specific destinations, identifies the cheapest flights, and updates the IATA codes and flight details in the Sheety database.
## Features
### 1.City IATA Code Retrieval:
Automatically fetches the IATA codes for cities using Amadeus APIs.
Updates the Sheety database with retrieved IATA codes.
### 2.Flight Offer Search:
Fetches available flights between a given origin and multiple destinations.
Extracts flight details, including departure and arrival times, and calculates the lowest price.
### 3.Cheapest Flight Notification:
Compares flight prices to those in the Sheety database.
Notifies when a cheaper flight is found.
## Set up the Environment
Create a .env file in the root directory with the following:
API_Key=your_amadeus_api_key
API_Secret=your_amadeus_api_secret
url_sheety=your_sheety_url
content_type=Bearer your_sheety_api_token

## Modules
### 1. Flights
Handles logic for identifying the cheapest flights and formatting flight details for output.
### 2. IATA_DATA
Interacts with Sheety API to fetch and update IATA code data.
Provides city data from the Sheety spreadsheet.
### 3. FlightSearch
Manages interaction with Amadeus API for:
Retrieving IATA codes.
Searching for flight offers.
Managing authorization tokens.

## Workflow
Fetch destination cities from Sheety.
Retrieve IATA codes for each city using Amadeus API.
Update Sheety with the retrieved IATA codes.
Search for flights between a fixed origin (ISB) and the destination cities.
Identify the cheapest flight for each destination and compare it to existing data in Sheety.
Output details for any flights cheaper than the stored price.


