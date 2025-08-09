# main.py
from hardware_setup import initialize_hardware
from sensors import readTempHum, distance, readspeed, readWeight
from camera_module import takePicture, takeVideo
from rfid import ser, validate_rfid
from alerts import flash_led, start_buzzer, stop_buzzer, change_buzzer_frequency
from keypad_module import get_passcode
from thingspeak import upload_speed, upload_weight_speed, download_field
from config import *
import RPi.GPIO as GPIO
import LCD1602 as LCD
import time

def main():
    initialize_hardware()
    x = 0
    speed_values = []
    weight_values = []
    
    while True:
        humidity, temperature = readTempHum()
        if x == 0:
            print("Welcome to AUS Smart Parking Toll Gate\n")
            print(f"Current Temperature is:{temperature}C")
            print(f"Current Humidity is:{humidity}%\n")
            x += 1

        dist = distance() / 100
        if dist < 1:
            print("Vehicle approaching is less than 1 meter away\n")
            takePicture()
            vehicle_speed = readspeed()
            print(f"Vehicle speed = {vehicle_speed:0.2f} km/hr\n")
            
            if vehicle_speed > 20:
                print("Driver’s speed is greater than 20 km/hr\n")
                LCD.write(0,0, "Slow Down      ")
                LCD.write(0,1, "Drive below 20 ")
                takeVideo()
                time.sleep(2)
            else:
                LCD.write(0,0, "Thank you for   ")
                LCD.write(0,1, "driving safely  ")
            
            if dist < 0.5:
                print("Vehicle approaching is less than 0.5 meters away\n")
                LCD.write(0,0, "Validating     ")
                LCD.write(0,1, "Vehicle        ")
                time.sleep(3)
                ser.flushInput(); ser.flushOutput()
                data = ser.read(12)
                code = validate_rfid(data)
                if code:
                    print("Vehicle Validated\n")
                    LCD.write(0,0, "Vehicle         ")
                    LCD.write(0,1, "Validated       ")
                    # Vehicle type check logic here...
                else:
                    print("RFID not valid!\n")
                    start_buzzer()
                    LCD.write(0,0, "RFID not valid ")
                    time.sleep(4)
                    LCD.write(0,0, "Enter Passcode ")
                    LCD.write(0,1, "to open website")
                    key_final = get_passcode()
                    # Passcode verification logic...

if __name__ == "__main__":
    main()
