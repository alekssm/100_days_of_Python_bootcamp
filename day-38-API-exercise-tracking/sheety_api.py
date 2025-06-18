import requests
from datetime import datetime
from config import SHEETY_USERNAME, SHEETY_PASS, SHEETY_ENDPOINT

def log_exercise(exercise):
    today = datetime.today().strftime('%d/%m/%Y')
    time_now = datetime.now().strftime('%H:%M:%S')

    data = {
        "sheet1": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=data, auth=(SHEETY_USERNAME, SHEETY_PASS))
    response.raise_for_status()
    return response.json()