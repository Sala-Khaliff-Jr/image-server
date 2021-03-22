from flask import Flask
import os 

CURENT_FOLDER = os.getcwd()
UPLOAD_FOLDER = CURENT_FOLDER+'images'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER