#!/usr/bin/env python
import sys
sys.path.append("/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/")
sys.path.append("/home/pi/Desktop/BLIND_FLY2.0/LOGIKA/FX/")
from META import *
import time
from grove.gpio import GPIO

usleep = lambda x: time.sleep(x / 1000000.0)
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.dio = GPIO(pin)

    def _get_distance(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)
        self.dio.dir(GPIO.IN)

        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()
        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm
        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

Grove = GroveUltrasonicRanger

class Ranger():
    Time=1
    pin = 5#Grove socket digital 5
    sonar = GroveUltrasonicRanger(pin)
    #print('Detecting distance...')
    ##########################READ DISTANCE
    def Distancer(self):
        while True:
            if self.sonar.get_distance()<=1000 and self.sonar.get_distance()>750:
                self.Time=2
                soundplay("ranger","far",.1)
            elif self.sonar.get_distance()<=750 and self.sonar.get_distance()>500:
                self.Time=1.75
                soundplay("ranger","med",.2)

            elif self.sonar.get_distance()<=500 and self.sonar.get_distance()>350:
                self.Time=1.5
                soundplay("ranger","med1",.3)
            elif self.sonar.get_distance()<=350 and self.sonar.get_distance()>250:
                self.Time=1.25
                soundplay("ranger","med2",.5)
            elif self.sonar.get_distance()<=250 and self.sonar.get_distance()>150:
                self.Time=1
                soundplay("ranger","close",.7)

            elif self.sonar.get_distance()<=150 and self.sonar.get_distance()>75:
                self.Time=.75
                soundplay("ranger","close1",.9)
            elif self.sonar.get_distance()<=75 and self.sonar.get_distance()>5:
                self.Time=.5
                soundplay("ranger","close2",1.0)

            elif self.sonar.get_distance()<=5:#optional buttonless shutoff. cover the sensor to shut off the device
                ShutDown()

            print('{} cm'.format(self.sonar.get_distance()))#prints distance in CM
            time.sleep(self.Time)
            
UR=Ranger()
soundplay("meta","connected",.5)#lets you know the program has started and your speaker is functional
time.sleep(1.5)
UR.Distancer()

