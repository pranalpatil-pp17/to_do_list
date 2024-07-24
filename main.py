from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import urllib.parse

app = Flask(__name__)

# encoded_password = urllib.parse.quote_plus("Pranal@17)pp")

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now().date())

    __tablename__ = 'todo_table'

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'
        # return super().__repr__()


with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'POST':
            title_inserted = request.form['title']
            description = request.form['desc']

            todo = Todo(title=title_inserted, desc=description)
            db.session.add(todo)
            db.session.commit()

        allTodo = Todo.query.all()

        return render_template('index.html', var=allTodo)

    except Exception as e:
        import traceback
        traceback.print_exc()
        db.session.rollback()
        return "An error occurred while inserting data."


@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title_inserted = request.form['title']
        description = request.form['desc']

        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title_inserted
        todo.desc = description
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
