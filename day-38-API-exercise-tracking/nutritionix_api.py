import requests
from config import NUTRITIONIX_ID, NUTRITIONIX_API_KEY, NUTRITIONIX_ENDPOINT

def fetch_exercises(query, gender, weight_kg, height_cm, age):
    headers = {
        "x-app-id": NUTRITIONIX_ID,
        "x-app-key": NUTRITIONIX_API_KEY
    }

    params = {
        "query": query,
        "gender": gender,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age
    }

    response = requests.post(NUTRITIONIX_ENDPOINT, json=params, headers=headers)
    response.raise_for_status()
    return response.json()["exercises"]