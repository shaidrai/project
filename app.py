import numpy as np
import pandas as pd
import os

from flask import Flask, request, render_template, send_from_directory
import os
from flask import flash , redirect, url_for
from werkzeug.utils import secure_filename





app = Flask(__name__)


UPLOAD_FOLDER = r'C:\Users\Administrator\Desktop\uploads'
ALLOWED_EXTENSIONS = {'sav','csv','jpg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def my_form():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return (('No selected file'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            email = request.form['email']
            password = request.form['password']
            massage = request.form['message']
            name_of_file = str(filename)
            list_of_fields = [email,massage,name_of_file]
            d_table = {'Fields': ['Email', 'Description', 'File name'], 'Values': list_of_fields}

            dt = pd.DataFrame(d_table)

            html_table =    .to_html()

            return html_table
        else:
            return('File is not allowed')








if __name__ == "__main__":
    app.run(port=4555, debug=True)
