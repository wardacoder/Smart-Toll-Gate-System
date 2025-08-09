# alerts.py
import time
import RPi.GPIO as GPIO
from config import *

# setting buzzer to produce a PWM signal with a frequency of 200 Hz 
buzz = GPIO.PWM(buzzer_pin, 200)

def start_buzzer(duty=30):
    buzz.start(duty)

def stop_buzzer():
    buzz.ChangeDutyCycle(0)

def change_buzzer_frequency(freq, duty=30):
    buzz.ChangeFrequency(freq)
    buzz.ChangeDutyCycle(duty)

def flash_led(pin, times=4, interval=1):
    for _ in range(times):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(interval)
