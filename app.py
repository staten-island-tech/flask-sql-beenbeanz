from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)  

with app.app_context():
    db.create_all()
@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
tasksList = []
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        task = request.form['task']
        desc = request.form['desc']
        newTask = Task(name=name, task=task, desc=desc)
        db.session.add(newTask)
        tasksList.append(newTask)
        db.session.commit()
        return render_template('tasks.html', tasksList=tasksList)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)

