from flask import Flask, url_for, render_template, request, redirect
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
    phone = db.Column(db.String(15), nullable=True)
    message = db.Column(db.Text, nullable=True)

# Create all tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Form Submitted!")  # Debug statement
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

        try:
            db.session.add(new_message)
            db.session.commit()
            print("Data saved successfully!")  # Debug statement
        except Exception as e:
            print(f"Error occurred: {e}")  # Print error if occurs
            return render_template('contact.html', error="An error occurred while saving the message.")

        return redirect(url_for('index'))  # Redirect to index

    return render_template('contact.html')  # Render the contact page for GET requests


if __name__ == '__main__':
    app.run(debug=True)