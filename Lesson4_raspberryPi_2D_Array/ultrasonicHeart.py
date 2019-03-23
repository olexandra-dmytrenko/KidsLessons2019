#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import RPi.GPIO as GPIO
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM) 

#set GPIO Ultrasonic Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# Main program logic follows:

##
# Run as: cd /home/pi/rpi_ws281x/python/examples; sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest
##

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

print ('Press Ctrl-C to quit.')

try:        
    heart1 = [
        0,1,1,0,0,1,1,0,
        1,1,1,0,0,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        0,1,1,1,1,1,1,0,
        0,0,1,1,1,1,0,0,
        0,0,0,1,1,0,0,0
    ]
    heart2 = [
        0,0,0,0,0,0,0,0,
        0,1,1,0,0,1,1,0,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        0,1,1,1,1,1,1,0,
        0,0,1,1,1,1,0,0,
        0,0,0,1,1,0,0,0,
        0,0,0,0,0,0,0,0
    ]
    heart3 = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,1,0,0,1,0,0,
        0,1,1,1,1,1,1,0,
        0,1,1,1,1,1,1,0,
        0,0,1,1,1,1,0,0,
        0,0,0,1,1,0,0,0,
        0,0,0,0,0,0,0,0
    ]
    heart4 = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,1,0,0,1,0,0,
        0,0,1,1,1,1,0,0,
        0,0,0,1,1,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
    ]
    
    hearts = [heart1, heart2, heart3, heart4]

    slide_shifter = 1
    slide_item = 0
    
    while True:
        colorWipe(strip, Color(0,0,0), 0)
        print("Erased!")
        
    #for q in range(3):
        #letterShape = hearts[slide_item]
        #slide_item = slide_item + slide_shifter
        #print("DEBUG: %s" % slide_item)
        
        #if slide_item == 3:
        #    slide_shifter = -1
        #    slide_item = 2
        #    print("DEBUG: Correction from 3 to %s" % slide_item)
        #elif slide_item == -1:
        #    slide_shifter = 1
        #    slide_item = 0
        #    print("DEBUG: Correction from -1 to %s" % slide_item)

        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
        #time.sleep(1)
        
        if dist<80:
            color_strength = int(dist/2)

            if dist >60:
                letterShape = hearts[3]
                color_strenght = 8
                print("DEBUG: %s" % slide_item)
            elif dist >40 and dist <=60:
                letterShape = hearts[2]
                color_strength = 24
                print("DEBUG: %s" % slide_item)
            elif dist >20 and dist <=40:
                letterShape = hearts[1]
                color_strength = 64
                print("DEBUG: %s" % slide_item)
            elif dist >0 and dist <=20:
                letterShape = hearts[0]
                color_strength = 128
                print("DEBUG: %s" % slide_item)
                

            for row_index, row_data in enumerate(letterShape):
                    strip.setPixelColor(row_index, Color(128, color_strength, 255) * row_data)
                    strip.show()
                    print("Set: pos: %s, Data: %s" % (row_index, row_data))
                    #time.sleep(0.0025)

            print("Shown!")
        time.sleep(0.5)
            
            


except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 0)



