from flask import Flask, request, render_template
import smtplib
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    email = request.form['email']
    password = request.form['password']
    if email == "shai@gmail.com" and password == "shai":
        return "you are king"
    else:
        return "you are gay"






app.run(debug=True, port=4555)