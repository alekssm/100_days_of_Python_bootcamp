import requests

OWM_Endopoint = ""
api_key = ""

parameters = {
    "lat": 42.696491,
    "lon": 23.326010,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endopoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

is_raining = False
#Getting id codes by dict keys in the Json data
weather_by_hour = weather_data["list"]
for item in weather_by_hour:
    condition_code = int(item["weather"][0]["id"])
    if condition_code < 700:
        is_raining = True

if is_raining:
    print("Bring an umbrella!")

