from flask import Flask, request, flash, redirect, url_for
from flask import render_template
#import flask_wtf

from flask_wtf import FlaskForm
from wtforms import SelectField
#from wtforms import StringField

from werkzeug.utils import secure_filename
import os
import requests
from djitellopy import Tello
import sys

sys.path.insert(1, "/var/www/html/Product-Design-and-Implementation/drone")

import pathfinder


UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = {'ico', 'jpg', 'png', 'jpeg', 'pdf', 'gif'}
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
# @app.route("/", methods=["GET","POST"]) 

class kuljetusForm(FlaskForm):
    #SelectField
    language = SelectField(u'Testing form', choices=[('cpp','C++'), ('py', 'Python')])

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parser(x):
    #for y in x:
    #    print(y)
    #pathfinder.dain(30,58)
    pathfinder.dain(x[1],x[2])

    #tello = Tello()
    #tello.connect()
    #tello.takeoff()
    #print(x)
    #tello.takeoff()
    #if (x == 'takeoff'):
    #    tello.takeoff()
    #if (b'emergency' in x):
    #    tello.emergency()


@app.route("/", methods=["GET", "POST"])
def index():
    form = kuljetusForm()
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
    return render_template("index.html", form=form)


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
        paikka.append(30)
        paikka.append(58)
        paikka[0] = 'takeoff'
        #print(paikka[0])
        #print(paikka[1])
        parser(paikka)
        # pathfinder(paikka[1])
    elif paikka[0] == 'B':
        paikka.append(17)
        paikka.append(28)
        parser(paikka)
    return render_template("index.html")

# Palvelimen käynnistys :
# sudo systemctl restart nginx , jos muokannut nginx asetuksia
# productdesign kansiossa venv päälle
# html kansion sisällä gunicorn --workers 5 wsgi:app
# screen päälle ja Ctrl+A+C, vaihda ikkuna = Ctrl+A+A
# sitten drone kansioon ja python tello.py 8080 
#
