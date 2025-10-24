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


start = ("TW170BL").upper()
end = ("SW1A1AA").upper()

if not validation.is_valid_postcode(start):
    print(f"Please enter a valid start postcode; {start} is not valid.")
elif not validation.is_valid_postcode(end):
    print(f"Please enter a valid end postcode; {end} is not valid.")
else:
    data = requests.get(url=f"https://api.tfl.gov.uk/Journey/JourneyResults/{start}/to/{end}").json()
    legs = data["journeys"][0]["legs"]
    summaries = [leg["instruction"]["summary"] for leg in legs ]
    print(summaries)
