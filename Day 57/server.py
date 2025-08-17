import requests
from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route('/')
def home():
    rand_num = random.randint(1,10)
    return render_template("index.html", rand_num = rand_num, year = datetime.datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)