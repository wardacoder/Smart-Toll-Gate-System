# flask_server.py
from flask import Flask, send_file
from sensors import readspeed
from datetime import datetime
from config import *

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return 'Welcome to the Smart Toll Gate system'

@myapp.route('/Fees')
def DisplayFees():
    return "Car fees = 15 Dhs | Motorbike fees 10 Dhs | Truck fees 20 Dhs"

@myapp.route('/Vehicle_Information')
def vehicle_info():
    timestamp = datetime.now().isoformat()
    speed = readspeed()
    if speed > 20:
        return f"Speed  = {speed}km/Hr. Slow Down!!"
    else:
        return f"Speed  = {speed}km/Hr"

@myapp.route('/Open_Gate/<mode>')
def Open_Gate(mode):
    return 'The Gate is Open' if mode == "open" else 'The Gate is closed' if mode == "close" else 'Enter open or close'

@myapp.route('/Vehicle_Capture/<capture>')
def vehicle_capture(capture):
    if capture == "photo":
        return send_file('/home/pi/Desktop/Vehiclepic.jpg', mimetype="image/jpeg")
    elif capture == "video":
        return send_file('/home/pi/Desktop/video.h264', mimetype="video/h264")
    else:
        return "Enter photo or video"
