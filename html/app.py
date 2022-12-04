from flask import Flask, request
from flask import render_template
import requests

app = Flask(__name__)

# @app.route("/", methods=["GET","POST"]) 

@app.route("/", methods=["POST", "GET"])
def index():
    #if request.method == "POST":
    #    print("ASDASDASDASDASDASDASDAS")
    #    payload = {'c':'takeoff'}
    #    requests.post('http://193.167.101.43:8080/', json=payload)
    return render_template("index.html")

@app.route("/script", methods=["GET","POST"])
def script():
    print("/script toimii")
    payload = {'c':'takeoff'}
    requests.post('http://193.167.101.43:8080/', json=payload)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("projektista.html")
