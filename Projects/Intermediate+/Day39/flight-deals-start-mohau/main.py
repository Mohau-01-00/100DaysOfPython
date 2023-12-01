from data_manager import DataManager
import pandas as pd

from flight_search import FlightSearch
import requests




flight_search=FlightSearch()




data_manager=DataManager()
sheet_data=data_manager.sheet_info()
sheety_endpoint=data_manager.end_point()   
sheety_put=data_manager.sheet_put()  

print(sheet_data)

for  dic_row in sheet_data:
    iatcode=dic_row['iataCode']
    city=dic_row['city']

    sheet_inputs = {
    "price": {
      
        "iataCode": flight_search.iata_code()

    }
 }
    print(iatcode)
    sheety_post= requests.put(url=sheety_put, json=sheet_inputs)

    if iatcode =="":
        d=iatcode.replace("",str(sheety_post))
       

        
       

# 5. In main.py check if sheet_data contains any values for the "iataCode" key. If not, 
# then the IATA Codes column is empty in the Google Sheet. In this case, pass each city name 
# in sheet_data one-by-one to the FlightSearch class. For now, the FlightSearch class can respond with
# "TESTING" instead of a real IATA code. You should use the response from the FlightSearch class to update the sheet_data dictionary.





#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.