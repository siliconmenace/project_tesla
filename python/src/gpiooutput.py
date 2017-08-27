#! /usr/dev/env python

import RPi.GPIO as GPIO
import time

pinout = 11
sleeptime = 2

GPIO.setup(pinout, GPIO.OUT)

while True:
    GPIO.output(pinout, True)
    time.sleep(sleeptime)
    GPIO.output(pinout, False)
    time.sleep(sleeptime)
    
