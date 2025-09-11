from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import secrets


from forms import LogInForm, SignUpForm

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    form = LogInForm()
    return render_template('login.html', form = form)

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form = form)

if __name__ == "__main__":
    app.run()