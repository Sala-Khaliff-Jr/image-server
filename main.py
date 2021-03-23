"""Program to start a web server for image-server
"""
from flask import Flask, render_template, request, url_for, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload/success')
def upload_success():
    return render_template('upload_success.html')

@app.route('/error')
def error():
    return render_template('Cannot perform the action')


@app.route('/upload', methods=['POST'])
def upload_file():
    user = 'sala'
    allowed_extensions = []
    uploaded_file = request.files['uploaded_file']
    if uploaded_file.filename != '':
        if not os.path.exists(f'images/{user}'):
            redirect(url_for('error'))
            # create folder when creating user
        else:
            uploaded_file.save(
                os.path.join(f'images/{user}', secure_filename(uploaded_file.filename))
            )
    return redirect(url_for('upload_success'))
