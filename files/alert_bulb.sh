#!/usr/bin/python3

import sys
from yeelight import Bulb

bulbip = '192.168.101.99'

alert_bulb = Bulb(bulbip)


def warm_alarm():
    alert_bulb.turn_on()
    alert_bulb.set_rgb(255, 0, 0)


def cold_alarm():
    alert_bulb.turn_on()
    alert_bulb.set_rgb(0, 0, 255)


def default_state():
    alert_bulb.turn_off()


def trigger(alert_value):
    if alert_value == 'warm':
        warm_alarm()
    elif alert_value == 'cold':
        cold_alarm()
    else:
        default_state()


try:
    trigger(sys.argv[1])
except KeyboardInterrupt:
    pass
