from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()
    gender = data["gender"]

    response = requests.get(f"https://api.agify.io?name={name}")
    data = response.json()
    age = data["age"]

    name = name.title()
    return render_template("index.html", name = name, gender = gender, age = age)

if __name__ == "__main__":
    app.run(debug=True)

