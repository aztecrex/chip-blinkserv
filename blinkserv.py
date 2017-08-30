import CHIP_IO.GPIO as GPIO
from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)

GPIO.setup("XIO-P0",GPIO.OUT)
GPIO.output("XIO-P0",GPIO.HIGH)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/led")
def led():
    if GPIO.input("XIO-P0"):
        return render_template('display.html', status="off")
    else:
        return render_template('display.html', status="on")

@app.route("/on")
def on():
    GPIO.output("XIO-P0",GPIO.LOW)
    return redirect(url_for('led'))

@app.route("/off")
def off():
    GPIO.output("XIO-P0",GPIO.HIGH)
    return redirect(url_for('led'))

