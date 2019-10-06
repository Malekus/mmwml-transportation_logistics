import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

file = open("parking.txt", "r", encoding='utf8')
parkings = file.read()
file.close()

parkings = parkings.replace("\xa0", "").replace("€", "").replace("m²", "").split("\n")

data = []
for parking in parkings:
    temp = list(map(lambda x: x.strip(), parking.split(";")))
    data.append([np.float(temp[0]),np.int(temp[1]),temp[2]])
    
data = pd.DataFrame(data=data, columns=['area', 'price', 'city'])

def getCity(data):
    return data['city'].unique()

def getDataByCity(city, data=data):    
    return data[data['city'] == city]

def _reg_linear(x, y):
    reg = LinearRegression()
    reg.fit([[i] for i in x], y)
    return reg

def _reg_predict(reg, x):
    return reg.predict([[i] for i in x])



app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/connected", methods = ['GET'])
def connected():
    return render_template('connected.html')

@app.route("/signup", methods = ['GET'])
def signup():
    return render_template('signup.html')

@app.route("/signin", methods = ['GET'])
def signin():
    return render_template('signin.html')



@app.route("/cities")
def cities():
    return {"data": list(getCity(data))}

@app.route("/prediction/<city>/<area>")
def prediction(city, area):
    cityData = getDataByCity(city)
    reg = _reg_linear(cityData["area"], cityData["price"])
    result = reg.predict([[int(area)]])
    return {"data": round(result[0], 2)}

app.run()
