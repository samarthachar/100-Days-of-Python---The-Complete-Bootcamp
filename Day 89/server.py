from flask import Flask, render_template, abort, request, url_for, redirect
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

@app.route('/todo/<todo_name>')
def todo(todo_name):
    todos = ['list']
    if todo_name in todos:
        return render_template('todo.html', name = todo_name, data=data)
    else:
        abort(404)

@app.route('/todo/<todo_name>/add-todo', methods=["POST"])
def add_todo(todo_name):
    title = request.form.get('title')
    description = request.form.get('description')
    global data
    data[title] = description
    return redirect(url_for('todo', todo_name=todo_name))

data = {}

if __name__ == "__main__":
    app.run(debug=False)