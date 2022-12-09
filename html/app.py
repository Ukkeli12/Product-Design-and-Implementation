from flask import Flask, request, flash, redirect, url_for
from flask import render_template

from werkzeug.utils import secure_filename

import numpy
from stl import mesh

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

@app.route('/object.stl')
def stl_gen(n=1):
    # tetrahedron mesh
    data = numpy.zeros(4, dtype=mesh.Mesh.dtype)
    b1,b2,b3,t = (1,0,1),(0,0,-0.75),(-1,0,1),(0,1,0)
    data['vectors'][0] = numpy.array([b1,b2,b3])
    data['vectors'][1] = numpy.array([b1,b2,t])
    data['vectors'][2] = numpy.array([b2,b3,t])
    data['vectors'][3] = numpy.array([b3,b1,t])
    object_mesh = mesh.Mesh(data, remove_empty_areas=False)

    # numpy-stl does a poor job of being "API" ready.. 
    # needs a generic string-ready .write method
    # (great opportunity for an open source contribution!)
    # for now we use a file-like object, BytesIO, to fake it out
    output = BytesIO()    
    object_mesh._write_ascii(output,"object.stl")
    response = make_response(output.getvalue())
    return response


# Palvelimen käynnistys :
# sudo systemctl restart nginx , jos muokannut nginx asetuksia
# html kansion sisällä sudo gunicorn --workers 5 wsgi:app
# screen päälle ja Ctrl+A+C, vaihda ikkuna = Ctrl+A+A
# sitten drone kansioon ja python tello.py 8080 
#
