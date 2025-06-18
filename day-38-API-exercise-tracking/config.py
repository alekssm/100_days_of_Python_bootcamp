import os
from dotenv import load_dotenv
load_dotenv()

NUTRITIONIX_ID = os.environ.get("Nutritionix_ID")
NUTRITIONIX_API_KEY = os.environ.get("Nutritionix_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASS = os.environ.get("SHEETY_PASS")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
