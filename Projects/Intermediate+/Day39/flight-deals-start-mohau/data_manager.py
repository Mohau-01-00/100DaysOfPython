import requests

class DataManager:

    def __init__(self) -> None:
        self.parameters={

        }
        self.sheet_endpoint="https://api.sheety.co/f1f682079ce550c59a4d511f280cf30e/flightDeals/prices"
        self.sheet_put="https://api.sheety.co/f1f682079ce550c59a4d511f280cf30e/flightDeals/prices/2"

    def end_point(self):
        

        return self.sheet_endpoint


    def sheet_info(self):

        response=requests.get(url=self.sheet_endpoint,json=self.parameters)
        response.raise_for_status()
        data = response.json()
        sheet=data['prices']
        return sheet
    def sheet_put(self):
        return self.sheet_put


data_manager=DataManager()
data_manager.sheet_info()




    #This class is responsible for talking to the Google Sheet.
    