# config.py
# ===============================
# Configuration constants for Smart Toll Gate System
# ===============================

# ThingSpeak details
WRITE_KEY = "B840552VU4JUOV8K"
Ch_ID = "2328945"
Speed_Field = 4
Weight_Field = 2
No_of_readings = 10
element_number = 5

# RFID tags
truckcode = '5400652FA3'
carcode = '46003BA4AD'
motorbikecode = '010FB3C21B'

# GPIO pins
buzzer_pin = 4
download_pb_pin = 16
operator_pb_pin = 17
warning_led_pin = 13
entrygate_led_pin = 12
weight_led_pin = 5
echo_pin = 27
trig_pin = 10

# Serial port
SERIAL_PORT = '/dev/ttyS0'
