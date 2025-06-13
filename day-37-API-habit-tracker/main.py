import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_API_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_API_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_POST_A_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/graph1"


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_config = {
    "id": "graph1",
    "name": "Training graph",
    "unit": "intensity",
    "type": "int",
    "color": "shibafu",
}


current_date_str = datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": current_date_str,
    "quantity": input("How much weight did you lift today?"),
}



#Creating the graph
#response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)



#Posting a pixel
#response = requests.post(url=PIXELA_POST_A_PIXEL_ENDPOINT, json=pixel_config, headers=headers)

new_pixel_data = {
    "quantity": "2",
}
#Updating a pixel
#response = requests.put(url=f"{PIXELA_POST_A_PIXEL_ENDPOINT}/{current_date_str}", json=new_pixel_data, headers=headers)
#print(response.text)

#Deleting a pixel
response = requests.delete(url=f"{PIXELA_POST_A_PIXEL_ENDPOINT}/{current_date_str}", json=new_pixel_data, headers=headers)
print(response.text)