import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 42.697708 # Your latitude
MY_LONG = 23.321867 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def is_iss_close():
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <=5:
       return True
    else:
        return False

def is_dark():
    if hour_now < sunrise or hour_now > sunset:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "EET",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

while True:
    time.sleep(60)
    if is_dark() and is_iss_close():
        connection = smtplib.SMTP("stmp.gmail.com")
        connection.starttls()
        connection.login("testemail", "testpassword")
        connection.sendmail(
            from_addr="testemail",
            to_addrs="testemail",
            msg="Subject:Look up!\n\nThe ISS  is above your head!"
        )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



