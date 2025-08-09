# keypad_module.py
from keypadfunction import keypad
import time

def get_passcode():
    key1 = keypad(); time.sleep(1)
    key2 = keypad(); time.sleep(1)
    key3 = keypad(); time.sleep(1)
    key4 = keypad(); time.sleep(1)
    return str(key1) + str(key2) + str(key3) + str(key4)
