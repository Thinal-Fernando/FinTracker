from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dashboard import create_dashboard
app = Flask(__name__)

app.config['SECRET_KEY'] = 'er7gh93478htuinfs9g834'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, description, amount,date):
        self.description = description
        self.amount = float(amount)
        self.date = datetime.strptime(date, "%Y-%m-%d")

@app.route("/")
def index():
    all_data = Expense.query.all()
    return render_template ('home.html' , expenses = all_data)

@app.route('/add_expense', methods = ['POST'])
def add_expense():
    if request.method == "POST":
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']

        my_data = Expense(description, amount, date)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))

create_dashboard(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
