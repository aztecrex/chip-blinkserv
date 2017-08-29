import CHIP_IO.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

GPIO.setup("XIO-P0",GPIO.OUT)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/on")
def on():
    GPIO.output("XIO-P0",GPIO.LOW)
    return ""

@app.route("/off")
def off():
    GPIO.output("XIO-P0",GPIO.HIGH)
    return ""



