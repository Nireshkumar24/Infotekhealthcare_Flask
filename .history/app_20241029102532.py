from flask import Flask,url_for,render_template,request
from flask_migrate import Migrate


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
