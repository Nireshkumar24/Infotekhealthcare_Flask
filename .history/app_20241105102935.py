from flask import Flask, url_for, render_template, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Infotek.sqlite3'
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    message = db.Column(db.Text, nullable=True)
    
with app.app_context():
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Form submitted successfully")
        try:
            first_name = request.form.get('FirstName')
            last_name = request.form.get('LastName')
            company_name = request.form.get('companyname')
            email = request.form.get('email')
            phone = request.form.get('Phone')
            message = request.form.get('message')

            # Save the data to the database
            new_message = ContactMessage(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                email=email,
                phone=phone,
                message=message
            )
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('contact'))
        except Exception as e:
            db.session.rollback()

    return render_template('contact.html')


@app.route('/carrer')
def carrer():
    return render_template('carrer.html')

if __name__ == '__main__':
    app.run(debug=True)
