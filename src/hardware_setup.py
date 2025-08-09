# hardware_setup.py
import RPi.GPIO as GPIO
import LCD1602 as LCD
import PCF8591 as ADC
from config import *

# Ignore warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def initialize_hardware():
    # Initialize LCD
    LCD.init(0x27, 1)

    # Setup ADC
    ADC.setup(0x48)

    # Setup buzzer
    GPIO.setup(buzzer_pin, GPIO.OUT)

    # Setup push buttons
    GPIO.setup(download_pb_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(operator_pb_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Setup LEDs
    GPIO.setup(warning_led_pin, GPIO.OUT)
    GPIO.setup(entrygate_led_pin, GPIO.OUT)
    GPIO.setup(weight_led_pin, GPIO.OUT)

    # Setup ultrasonic sensor pins
    GPIO.setup(echo_pin, GPIO.IN)
    GPIO.setup(trig_pin, GPIO.OUT)
