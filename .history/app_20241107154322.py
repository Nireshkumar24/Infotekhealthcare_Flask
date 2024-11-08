from flask import Flask, url_for, render_template, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Infotek.sqlite3'
app.secret_key = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465  # Port for TLS
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'nireshkumarniresh007@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'Niresh@2001'  # Your email password
app.config['MAIL_USE_SSL']=True
mail = Mail(app)
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
            
            msg = Message("New Contact Form Submission",
                          recipients=["nireshkumarniresh@gmail.com"])
            msg.body = f"""
            New contact form submission:

            First Name: {first_name}
            Last Name: {last_name}
            Company Name: {company_name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
            mail.send(msg)
            db.session.add(new_message)
            db.session.commit()
            flash('Your message has been sent successfully!', 'success')
            # msg = Message("New Contact Form Submission",
            #               recipients=["nireshkumarniresh@gmail.com"])
            # msg.body = f"""
            # New contact form submission:

            # First Name: {first_name}
            # Last Name: {last_name}
            # Company Name: {company_name}
            # Email: {email}
            # Phone: {phone}
            # Message: {message}
            # """
            # mail.send(msg)
            
            return redirect(url_for('index'))
        except Exception as e:
            
            db.session.rollback()
            flash('There was an error sending your message. Please try again.', 'error')

    return render_template('contact.html')


@app.route('/carrer')
def carrer():
    return render_template('carrer.html')

if __name__ == '__main__':
    app.run(debug=True)
