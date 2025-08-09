# thingspeak.py
import urllib.request
from config import *

def upload_speed(speed):
    urllib.request.urlopen(f"https://api.thingspeak.com/update?api_key={WRITE_KEY}&field4={speed}")

def upload_weight_speed(weight, speed):
    urllib.request.urlopen(f"https://api.thingspeak.com/update?api_key={WRITE_KEY}&field2={weight}&field4={speed}")

def download_field(field):
    url = f"https://api.thingspeak.com/channels/{Ch_ID}/fields/{field}.csv?results={No_of_readings}"
    data = urllib.request.urlopen(url).read().decode('ascii')
    return ",".join(data.split("\n"))
