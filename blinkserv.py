import CHIP_IO.GPIO as GPIO
from flask import Flask
from flask import render_template, redirect, url_for, Response

app = Flask(__name__)

GPIO.setup("XIO-P0",GPIO.OUT)
GPIO.output("XIO-P0",GPIO.HIGH)

def ledTurnOn():
    GPIO.output("XIO-P0",GPIO.LOW)

def ledTurnOff():
    GPIO.output("XIO-P0",GPIO.HIGH)

def ledIsOn():
    return not GPIO.input("XIO-P0")
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/led")
def led():
    return render_template('led.html')

@app.route("/api/led")
def apiLedStatus():
    rep = render_template('led.json', status=ledIsOn())
    return Response(rep, mimetype='application/json')

@app.route("/api/led/on", methods=['POST'])
def apiLedOn():
    ledTurnOn()
    rep = render_template('led.json', status=True)
    return Response(rep, mimetype='application/json')

@app.route("/api/led/off", methods=['POST'])
def apiLedOff():
    ledTurnOff()
    rep = render_template('led.json', status=False)
    return Response(rep, mimetype='application/json')

