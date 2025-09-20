from flask import Flask, render_template, abort, request, url_for, redirect, jsonify
from flask_bootstrap import Bootstrap
import secrets
from flask import Flask, render_template,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select

from forms import LogInForm, SignUpForm

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
Bootstrap(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    ticked: Mapped[bool] = mapped_column(Boolean, nullable=False)


with app.app_context():
    db.create_all()




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
    data = {}
    tasks = db.session.query(Task).all()
    for task in tasks:
        data[task.id] = (task.title, task.description, task.ticked)
    if todo_name in todos:
        return render_template('todo.html', name=todo_name, data=data)
    else:
        abort(404)


@app.route('/todo/<todo_name>/add-todo', methods=["POST"])
def add_todo(todo_name):
    title = request.form.get('title')
    description = request.form.get('description')
    with app.app_context():
        new_task = Task(
            title=title,
            description=description,
            ticked=False
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('todo', todo_name=todo_name))


@app.route("/<todo_name>/check-tick", methods=["POST"])
def check_tick(todo_name):
    json = request.get_json()
    checked_ids = json['checked_ids']
    ids = db.session.query(Task.id).all()
    for unchecked_id in [id_tuple[0] for id_tuple in ids]:
        if unchecked_id not in checked_ids:
            task = db.session.execute(
                select(Task).where(Task.id == unchecked_id)
            ).scalar_one_or_none()
            task.ticked = False
            db.session.commit()
    for checked_id in checked_ids:
        task = db.session.execute(
            select(Task).where(Task.id == checked_id)
        ).scalar_one_or_none()
        task.ticked = True
        db.session.commit()
    return redirect(url_for('todo', todo_name=todo_name))

@app.route("/<todo_name>/delete-todo/<todo_id>")
def delete_todo(todo_name, todo_id):
    task = db.session.get(Task, todo_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('todo', todo_name=todo_name))

if __name__ == "__main__":
    app.run(debug=True)