from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", data = data)

@app.route('/post/<blog_id>')
def get_blog(blog_id):
    current_blog = None
    for blog in data:
        if str(blog["id"]) == blog_id:
            current_blog = blog
            break
    return render_template("post.html", blog=current_blog)

if __name__ == "__main__":
    app.run(debug=True)
