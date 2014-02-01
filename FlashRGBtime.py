import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19, 0)
GPIO.output(11, 0)
GPIO.output(15, 0)

rest = raw_input('How long would you like each stage? -->')

while 1:
        GPIO.output(15, 0)
        GPIO.output(11, 1)
        time.sleep(float(rest))
        GPIO.output(19, 1)
        time.sleep(float(rest))
        GPIO.output(11, 0)
        time.sleep(float(rest))
        GPIO.output(15, 1)
        time.sleep(float(rest))
        GPIO.output(19, 0)
        time.sleep(float(rest))
