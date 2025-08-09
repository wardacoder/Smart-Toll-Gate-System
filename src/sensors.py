# sensors.py
import time
import DHT11
import PCF8591 as ADC
import RPi.GPIO as GPIO
from config import *

# function to read humidity and temperature 
def readTempHum():   
    result = ""
    while (not result):
        result = DHT11.readDht11(18)
        if result:
            humidity, temperature = result
    return result

# function to measure the distance in cm using the ultrasonic sensor
def distance():
    GPIO.output(trig_pin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trig_pin, 1)
    time.sleep(0.000001)
    GPIO.output(trig_pin, 0)
    while GPIO.input(echo_pin) == 0:
        pass
    time1 = time.time()
    while GPIO.input(echo_pin) == 1:
        pass
    time2 = time.time()
    return (time2 - time1) * 1000000 / 58

# function to read the speed of the vehicle from a potentiometer
def readspeed():
    ADC_units = ADC.read(1)
    ADC_volts = (ADC_units*3.3)/256
    speed = (ADC_units/255)*200
    vehicle_speed = int(speed)
    return vehicle_speed

# function to read the weight of a truck
def readWeight():
    ADC_units = ADC.read(2)
    ADC.write(ADC_units)
    ADC_volts = (ADC_units*3.3)/256
    weight = (ADC_units/255)*8000
    vehicle_weight = int(weight)
    return vehicle_weight
