import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.
def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return time_now >= sunset or time_now <= sunrise



def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="shadow.sharingan.test@gmail.com", password="ggng regn zbqw ngsg")
        connection.sendmail(
            from_addr="shadow.sharingan.test@gmail.com",
            to_addrs="shadow.sharingan.test@gmail.com",
            msg="Subject: LOOK UP\n\nHello, the ISS is currently above you. Please look up."
        )


while True:
    time.sleep(60)
    if is_dark() and position():
        send_email()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



