import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os



GENDER="male"
WEIGHT_KG="84"
HEIGHT="180.9"
AGE="36"


APP_ID=os.getenv("APP_ID")
APP_KEY=os.getenv("APP_KEY")
SHEETY_API_KEY=os.getenv("SHEETY_API_KEY")


exercise_input=input("Tell which exercise you did today?: ")

headers={

    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type": "application/json"
}
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()


#-----------------------------------------------------------------------------------



SHEET_ENDPOINT=os.getenv("SHEET_ENDPOINT")


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_header={

    
    "Authorization": SHEETY_API_KEY
   
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs,headers=sheety_header)

    print(sheet_response.text)



