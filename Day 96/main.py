import requests
from flask import Flask
from ukpostcodeutils import validation

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
    return postcode, f"{postcode[:-3]} {postcode[-3:]}"




start =format_postcode(input("TW170BL"))
end = format_postcode(input("SW1A1AA"))

if not validation.is_valid_postcode(start[0]):
    print(f"Please enter a valid start postcode; {start[1]} is not valid.")
elif not validation.is_valid_postcode(end[0]):
    print(f"Please enter a valid end postcode; {end[1]} is not valid.")
else:
    print(start[1])
    print(end[1])
    data = requests.get(url=f"https://api.tfl.gov.uk/Journey/JourneyResults/{start[1]}/to/{end[1]}").json()
    print(data)
    legs = data["journeys"][0]["legs"]
    summaries = [leg["instruction"]["summary"] for leg in legs ]
    print(summaries)
