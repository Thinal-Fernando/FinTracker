from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'er7gh93478htuinfs9g834'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template ('home.html')



if __name__ == '__main__':
    app.run(debug=True)