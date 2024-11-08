from flask import Flask,url_for,render_template,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

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
