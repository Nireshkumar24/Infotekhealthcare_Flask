from flask import Flask,url_for,render_template,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Infotek.sqlite3'
db = SQLAlchemy(app)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=True)

db.create_all() 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medical_billing')
def medical_billing():
    return render_template('medical billing.html')

@app.route('/medical_coding')
def medical_coding():
    return render_template('medical coding.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/techdriven')
def techdriven():
    return render_template('techDriven.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/carrer')
def carrer():
    return render_template('carrer.html')

if __name__ == '__main__':
    app.run(debug=True)
