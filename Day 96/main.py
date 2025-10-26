import requests
from flask import Flask
# app  = Flask(__name__)
#
# @app.route("/")
# def api():
#     pass
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

def format_postcode(postcode):
    if " " in postcode:
        postcode = postcode.replace(" ","")
    postcode =  postcode.upper().strip()
    return  f"{postcode[:-3]} {postcode[-3:]}"

def latandlong(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode.replace(" ","")}"
    data = requests.get(url=url).json()
    try:
        if data['error']:
            return False
    except:
        pass
    lat = data["result"]["latitude"]
    long = data["result"]["longitude"]
    return lat,long


start = format_postcode(input("Enter start destination: "))
end = format_postcode(input("Enter end destination: "))


start = latandlong(start)
end = latandlong(end)

# Enter start destination: E8 3DY
# Enter end destination: SE16 7TX



if not start:
    print(f"Please enter a valid start postcode")
elif not end:
    print(f"Please enter a valid end postcode")
else:

    url=f"https://api.tfl.gov.uk/Journey/JourneyResults/{start[0]},{start[1]}/to/{end[0]},{end[1]}"
    data = requests.get(url=url).json()

    if "journeys" not in data:
        print("No journey found for your inputs.")
        exit()

    legs = data["journeys"][0]["legs"]
    summaries = [leg["instruction"]["summary"] for leg in legs ]
    print(summaries)

