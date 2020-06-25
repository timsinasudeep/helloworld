from flask import Flask
from dotenv import load_dotenv
from flask import redirect,render_template,request,url_for
from models import TaskModel

from db import db


app= Flask(__name__)
load_dotenv (".env",verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTINGS")

@app.route('/')

def home():
    tasks=TaskModel.find_all()
    return render_template('index.html',tasks=tasks)
    
@app.route('/create-tasks',methods=['POST'])

def create():
    new_tasks =TaskModel(title=request.form['title'])
    new_tasks.save_to_db()
    return redirect(url_for('home'))

@app.route('/done/<id>')

def done(id):
    task = TaskModel.find_by_id(id)
    task.done =not(task.done)
    task.save_to_db()
    return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    task = TaskModel.find_by_id(id)
    task.delete_from_db()
    return redirect(url_for('home'))

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ =="__main__":
    db.init_app(app)
    app.run(port=5000)