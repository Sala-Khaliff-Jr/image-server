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

@app.route('/upload', methods=['POST'])
def upload_file():
    allowed_extensions 
    uploaded_file = request.files['uploaded_file']
    print(uploaded_file.__dict__)
    if uploaded_file.filename != '':
        uploaded_file.save(
            os.path.join('images/', secure_filename(uploaded_file.filename))
        )
    return redirect(url_for('upload_success'))


# uploaded_file
#     {'name': 'uploaded_file',
#      'stream': <tempfile.SpooledTemporaryFile object at 0x7fd292af8e80>, 
#     filename': 'ai_5_logo_alone.png', 
#         'headers': Headers(
#             [('Content-Disposition', 
#             'form-data; name="uploaded_file";  filename="ai_5_logo_alone.png"'), 
#             ('Content-Type', 'image/png')]
#         )
#     }

