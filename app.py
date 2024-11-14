from flask import Flask, url_for, render_template, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Infotek.sqlite3'
app.secret_key = '!@#$%^&*()'
# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'nireshkumarniresh@gmail.com'  # Use your Gmail email
app.config['MAIL_PASSWORD'] = 'gfru mkbe msjp kekr'  # Use your Gmail password or App Password
app.config['MAIL_DEFAULT_SENDER'] = 'nireshkumarniresh@gmail.com'

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
    
class CantactEmail(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(30),nullable=True)    
    
class AboutEmail(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(30),nullable=True)
    
class CarrerEmail(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(30),nullable=True)    
    
class IndexEmail(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(50),nullable=True)     
    
class medicalBilling_Email(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(50),nullable=True)     
    
class medicalCoding_Email(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(50),nullable=True)    
    
    
class Techdriven_Email(db.Model):
    id=db.Column(db.Integer,primary_key=True)    
    Email=db.Column(db.String(50),nullable=True)      
    
with app.app_context():
 db.create_all() 

@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = IndexEmail(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('index')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
        
    
    
     return render_template('index.html',active_page='home')


@app.route('/medical_billing',methods=['GET', 'POST'])
def medical_billing():
     if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = medicalBilling_Email(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('medical_billing')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
        
    
    
     return render_template('medical billing.html',active_page='medical_billing')



@app.route('/medical_coding',methods=['GET', 'POST'])
def medical_coding():
    
     if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = medicalCoding_Email(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('medical_coding')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
       
    
     return render_template('medical coding.html',active_page='medical_coding')

# @app.route('/about', methods=['GET', 'POST'])
# def about():
#     if request.method == 'POST':
#         email = request.form.get('email')
        
#         if email:
#             # Create an instance of the AboutEmail model and save to the database
#             new_email = AboutEmail(Email=email)
#             db.session.add(new_email)
#             db.session.commit()
           
#             msg = Message(
#                 subject="New Subscriber",
#                 recipients=["nireshkumarniresh@gmail.com"]
#             )
#             msg.body = f"""
#             A new user has subscribed to the newsletter:

#             Email: {email}
#             """
            
#             mail.send(msg)
            
#             # Flash a success message
#             flash("Thank you for subscribing!", "success")
#         else:
#             # Flash an error message if email is empty
#             flash("Please enter a valid email address.", "error")
        
#         return redirect(url_for('about')) 
    
#     return render_template('medical coding.html',active_page='medical_coding')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = AboutEmail(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('about')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
        

    # Render the page with the form and any flash messages
    return render_template('about.html', active_page='about')


@app.route('/techdriven',methods=['GET', 'POST'])
def techdriven():
      if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = Techdriven_Email(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('techdriven')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
        
    
      return render_template('techDriven.html',active_page='techdriven')

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
            
            db.session.add(new_message)
            db.session.commit()
            
            # Send email to info@infotekhealthcare.com with the form details
            msg = Message(
                subject="New Contact Form Submission",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            New contact form submission:

            First Name: {first_name}
            Last Name: {last_name}
            Company Name: {company_name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
            
            # Send the email
            mail.send(msg)
           
            flash('Form Submited successfully!', 'success')
            return redirect(url_for('contact'))
           

        except Exception as e:
            
            db.session.rollback()
            flash('There was an error. Please try again.', 'error')

    return render_template('contact.html',active_page='contact')


@app.route('/carrer',methods=['GET', 'POST'])
def carrer():
     if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = CarrerEmail(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('carrer'))
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
         

     return render_template('carrer.html',active_page='carrer')
 
 
@app.route('/contactemail',methods=['GET', 'POST'])
def contactemail():
     if request.method == 'POST':
        email = request.form.get('emailcontact')
        
        if email:
            # Create an instance of the AboutEmail model and save to the database
            new_email = CantactEmail(Email=email)
            db.session.add(new_email)
            db.session.commit()
           
            msg = Message(
                subject="New Subscriber",
                recipients=["info@infotekhealthcare.com"]
            )
            msg.body = f"""
            A new user has subscribed to the newsletter:

            Email: {email}
            """
            
            mail.send(msg)
            
            # Flash a success message
            flash("Thank you for Connecting!", "success")
            return redirect(url_for('contact')) 
        else:
            # Flash an error message if email is empty
            flash("Please enter a valid email address.", "error")
        
        
    
    

if __name__ == '__main__':
    app.run(debug=True)
