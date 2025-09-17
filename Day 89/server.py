from flask import Flask, render_template, abort, request, url_for, redirect, jsonify
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
    todos = ['Your Todos']
    if todo_name in todos:
        return render_template('todo.html', name = todo_name, data=data)
    else:
        abort(404)

@app.route('/todo/<todo_name>/add-todo', methods=["POST"])
def add_todo(todo_name):
    global data, id_no
    title = request.form.get('title')
    description = request.form.get('description')
    task_id = f"task{id_no}"
    id_no += 1
    data[task_id] = (title, description, False)
    return redirect(url_for('todo', todo_name=todo_name))


@app.route("/<todo_name>/check-tick", methods=["POST"])
def check_tick(todo_name):
    json = request.get_json()
    checked_ids = json['checked_ids']
    for unchecked_id in data.keys():
        if unchecked_id not in checked_ids:
            title, description, _ = data[unchecked_id]
            data[unchecked_id] = (title, description, False)
    for checked_id in checked_ids:
        title, description, _ = data[checked_id]
        data[checked_id] = (title, description, True)
    return redirect(url_for('todo', todo_name=todo_name))

@app.route("/<todo_name>/delete-todo/<todo_id>")
def delete_todo(todo_name, todo_id):
    global data
    data.pop(todo_id, None)
    return redirect(url_for('todo', todo_name=todo_name))
data = {}
id_no = 0

if __name__ == "__main__":
    app.run(debug=True)