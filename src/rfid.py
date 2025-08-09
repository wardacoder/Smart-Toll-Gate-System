# rfid.py
import serial
from config import SERIAL_PORT

#setting the serial port according to the Parallax reader’s datasheet 
ser = serial.Serial(
    baudrate = 2400,  
    bytesize = serial.EIGHTBITS,  
    parity = serial.PARITY_NONE,  
    port = SERIAL_PORT, 
    stopbits = serial.STOPBITS_ONE,  
    timeout = 1
)

#function to validate RFID tag - if the tag is valid the code will be returned else False 
def validate_rfid(code):
    s = code.decode("ascii")
    if (len(s) == 12) and (s[0] == "\n") and (s[11] == "\r"):
        return s[1:11]
    else:
        return False
