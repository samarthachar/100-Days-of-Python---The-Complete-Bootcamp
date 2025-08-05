import requests
from datetime import datetime

USERNAME = "shadowsharingantest"
TOKEN = "testshadowsharingan"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"



user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name": "Productive Work Graph",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}


# response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

current_date = datetime.now()

pixel_params = {
    "date": current_date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you work productively today? ")
}


response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

put_pixel_endpoint = f"{post_pixel_endpoint}/20250804"


put_pixel_params = {
    "quantity": "3.00"
}

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = put_pixel_endpoint

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)


