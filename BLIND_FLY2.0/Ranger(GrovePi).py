#!/usr/bin/env python

import sys
sys.path.append("/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/")
sys.path.append("/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/FX/")
from META import *
import grovepi
import time

# set I2C to use the hardware bus
grovepi.set_bus("RPI_1")

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 7
#sonar=grovepi.ultrasonicRead(ultrasonic_ranger)

Time=1
#print('Detecting distance...')
##########################READ DISTANCE
def Distancer():
    while True:
        if grovepi.ultrasonicRead(ultrasonic_ranger)<=1000 and grovepi.ultrasonicRead(ultrasonic_ranger)>750:
            Time=2
            soundplay("ranger","far",.1)
        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=750 and grovepi.ultrasonicRead(ultrasonic_ranger)>500:
            Time=1.75
            soundplay("ranger","med",.2)

        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=500 and grovepi.ultrasonicRead(ultrasonic_ranger)>350:
            Time=1.5
            soundplay("ranger","med1",.3)
        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=350 and grovepi.ultrasonicRead(ultrasonic_ranger)>250:
            Time=1.25
            soundplay("ranger","med2",.5)
        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=250 and grovepi.ultrasonicRead(ultrasonic_ranger)>150:
            Time=1
            soundplay("ranger","close",.7)

        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=150 and grovepi.ultrasonicRead(ultrasonic_ranger)>75:
            Time=.75
            soundplay("ranger","close1",.9)
        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=75 and grovepi.ultrasonicRead(ultrasonic_ranger)>5:
            Time=.5
            soundplay("ranger","close2",1.0)

        elif grovepi.ultrasonicRead(ultrasonic_ranger)<=5:
            ShutDown()

        print('{} cm'.format(grovepi.ultrasonicRead(ultrasonic_ranger)))
        time.sleep(Time)
            
soundplay("meta","connected",.5)
time.sleep(1.5)
Distancer()

'''while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))

    except Exception as e:
        print ("Error:{}".format(e))
    
    time.sleep(0.1) # don't overload the i2c bus'''
