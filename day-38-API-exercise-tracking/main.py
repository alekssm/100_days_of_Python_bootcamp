import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

GENDER = "Male"
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 30

NUTRITIONIX_ID = os.environ.get("Nutritionix_ID")
NUTRITIONIX_API_KEY = os.environ.get("Nutritionix_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASS = os.environ.get("SHEETY_PASS")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

sheety_auth = (SHEETY_USERNAME, SHEETY_PASS)

exercise_input = input("What have you done in your workout today? ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)


today = datetime.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%H:%M:%S')

for exercise in result["exercises"]:
    new_data = {
        "sheet1": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }

    sheety_response = requests.post(SHEETY_ENDPOINT, json=new_data, auth=sheety_auth)
    print(sheety_response.json())