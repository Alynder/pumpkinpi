#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os

ledPin1 = 12 # define ledPins
ledPin2 = 16
sensorPin = 11    # define sensorPin

def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin1, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(ledPin2, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin1,GPIO.HIGH) # turn on led's
            GPIO.output(ledPin2,GPIO.HIGH)
            os.system("mplayer -ao alsa:device=bluetooth witch.wav")
            print ('led turned on >>>')
        else :
            GPIO.output(ledPin,GPIO.LOW) # turn off led
            print ('led turned off <<<')

def destroy():
    GPIO.cleanup()                     # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

