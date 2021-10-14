#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
from time import sleep

ledPin1 = 12 # define ledPins
ledPin2 = 22
sensorPin = 11    # define sensorPin
leds = [ledPin1, ledPin2]

def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin1, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(ledPin2, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

    
 


def main():
    while True:
        for led in leds:
            if GPIO.input(sensorPin)==GPIO.HIGH:
                        GPIO.output(led, GPIO.HIGH)
                        sleep(.03)
                        GPIO.output(led, GPIO.LOW)
                        print ('led turned on >>>')
            else :
                GPIO.output(led, GPIO.LOW) # turn off led
                print ('led turned off <<<')
             



def destroy():
    GPIO.cleanup()                     # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        main()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

