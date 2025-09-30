from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
app = Flask(__name__)

app.config['SECRET_KEY'] = 'er7gh93478htuinfs9g834'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, description, amount,category ,date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

@app.route("/")
def index():
    all_data = Expense.query.all()
    return render_template ('home.html' , expenses = all_data)

@app.route('/add_expense', methods = ['POST'])
def add_expense():
    if request.method == "POST":
        description = request.form['description']
        amount = request.form['amount']
        category = request.form["category"]
        date_str = request.form['date']

        missing_fields = []
        if not description:
            missing_fields.append("Description")
        if not amount:
            missing_fields.append("Amount")
        if not date_str:
            missing_fields.append("Date")

        if missing_fields:
            flash(f"Please fill out the following: {', '.join(missing_fields)}", "error")
            return redirect(url_for('index'))
        
        try:
            amount = float(amount)
        except ValueError:
            flash(( "Amount must be a number","error"))
            return redirect(url_for('index'))
        
        if date_str:
            try: 
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                flash("Invalid date format","error")
                date_obj = date.today()
        else:
           date_obj = date.today()

            

        my_data = Expense(description, amount, category, date_obj)
        db.session.add(my_data)
        db.session.commit()
        flash("Expense successfully added!")

        return redirect(url_for('index'))

@app.route('/transactions')
def show_transactions():
    all_data =  Expense.query.all()
    return render_template('transactions.html', expenses = all_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
