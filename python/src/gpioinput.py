#! /usr/dev/env python

import RPi.GPIO as GPIO

pinin = 12

GPIO.setup(pinin, GPIO.IN)

count = 1

while True:
    input_value = GPIO.input(pinin)

    if input_value == False:
        print "The button has been pressed {0} times." .format(count)
        count += 1
        while input_value == False:
            input_value = GPIO.input(pinin)
            
