from flask import Flask, request, flash, redirect, url_for
from flask import render_template

from werkzeug.utils import secure_filename
import os
import requests

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = {'ico', 'jpg', 'png', 'jpeg', 'pdf', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# @app.route("/", methods=["GET","POST"]) 

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            return redirect(request.url)
    return render_template("index.html")


@app.route("/script", methods=["GET","POST"])
def script():
    if request.method == 'POST':
        print('Post /script')
        payload = {'c' : 'takeoff'}
        requests.post('http://193.167.101.43:8080/', json=payload)
        return redirect(request.url)
    #print("/script toimii")
    #payload = {'c':'takeoff'}
    #requests.post('http://193.167.101.43:8080/', json=payload)
    return render_template("index.html")

@app.route("/emergency", methods=["GET","POST"])
def emergency():
    payload = {'c':'emergency'}
    requests.post('http://193.167.101.43:8080/', json=payload)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("projektista.html")

@app.route("/group")
def group():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'murmu.png')
    return render_template("group.html", mursu_image = full_filename)

@app.route("/tilaus", methods=["GET","POST"])
def tilaus():
    paikka = request.form.getlist('options')
    print(paikka[0])
    if paikka[0] == 'A':
        paikka.append((2,5))
        print(paikka[1])
        # pathfinder(paikka[1])
    return render_template("index.html")

# Palvelimen käynnistys :
# sudo systemctl restart nginx , jos muokannut nginx asetuksia
# html kansion sisällä sudo gunicorn --workers 5 wsgi:app
# screen päälle ja Ctrl+A+C, vaihda ikkuna = Ctrl+A+A
# sitten drone kansioon ja python tello.py 8080 
#
