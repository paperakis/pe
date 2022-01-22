#!/usr/bin/python3

import RPi.GPIO as GPIO
import dht11
# import time
# import datetime
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=4)
RETRIES = 3

def temperature():
    result = instance.read()
    if result.is_valid():
        return result.temperature
    return None

def humidity():
    result = instance.read()
    if result.is_valid():
        return result.humitidy
    return None

def retry_for_result(which_value, retries):
    for i in range(retries):
        result = get_value(which_value)
        if result:
            return result

def get_value(name):
    result = instance.read()
    if result.is_valid():
        return getattr(result, name)
    return None
try:
    print(retry_for_result(sys.argv[1], RETRIES))
except KeyboardInterrupt:
    pass