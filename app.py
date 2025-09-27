from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'er7gh93478htuinfs9g834'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, description, amount,data):
        self.description = description
        self.amount = amount
        self.date = data

@app.route("/")
def index():
    return render_template ('home.html')



if __name__ == '__main__':
    app.run(debug=True)