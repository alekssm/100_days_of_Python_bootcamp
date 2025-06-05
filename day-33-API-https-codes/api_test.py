import requests

MY_LAT = 42.697708
MY_LNG = 23.321867

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": "EET"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
