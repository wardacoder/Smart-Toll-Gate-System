# camera_module.py
from datetime import datetime
import time
from picamera import PiCamera

#using PiCamera() class an object called Mycamera is created 
Mycamera = PiCamera()

# function to click a picture with annotated date and time in ISO format 
def takePicture():
    Mycamera.sharpness = 30
    Mycamera.brightness = 50
    Mycamera.resolution = (640,480)
    timestamp = datetime.now().isoformat()
    photo_path="/home/pi/Desktop/Vehiclepic.jpg"
    Mycamera.start_preview()
    Mycamera.annotate_text = "Picture taken at time %s" % timestamp
    time.sleep(4)
    Mycamera.capture(photo_path)
    Mycamera.stop_preview()

# function to record a 5 second video with annotated date and time in ISO format 
def takeVideo():
    Mycamera.sharpness = 30
    Mycamera.brightness = 50
    Mycamera.resolution = (640,480)
    timestamp = datetime.now().isoformat()
    Mycamera.start_preview()
    Mycamera.annotate_text = "Video taken at time %s" % timestamp
    time.sleep(5)
    Mycamera.start_recording('/home/pi/Desktop/Vehiclevideo.h264')
    time.sleep(5)
    Mycamera.stop_recording()
    Mycamera.stop_preview()
