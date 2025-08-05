import requests
from datetime import datetime
import os


APP_ID="6872a86a"
APP_KEY="2f6dba6b98db2a7eb79db6fb8e143c54"
AUTHORISATION="Bearer cld03hjdfls%dsglkndgj50*dslsdkgnfvlmsdnlgknrejfkdgnvdmvlblrdiuut9y3oerihfjsen"

nlp_for_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"




exercise = input("Tell us what exercises you did: ")
params = {
    "query": exercise ,
    "weight_kg":42,
    "height_cm":174,
    "age":13,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=nlp_for_exercise_endpoint, json=params, headers=headers)
result = response.json()
sheety_endpoint = "https://api.sheety.co/273fc76b9f6cbfed381314931a9ba115/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": AUTHORISATION,

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

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)