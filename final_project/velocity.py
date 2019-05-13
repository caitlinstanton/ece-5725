#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author : Matt Hawkins
# Date   : 08/05/2018
#
# https://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO
import math

timeVal = [0,0]
diameter = 15.24 #centimeters
circumference = math.pi*diameter
numPasses = 0
velocity = 0 #cm/s

servoPin = 13
#freq = 1000.0/(20.0+on_time)
dc = 5 #left position:5, middle:7.5, right:10 
#100.0*(on_time/(20.0+on_time))

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin,50)
p.start(dc)
dc = 7.5

def sensorCallback(channel):
  # Called if sensor output changes
  stamp = time.time()
  if GPIO.input(channel):
    # No magnet
    print("Sensor HIGH ")
  else:
    # Magnet
    print("Sensor LOW ")
    calculate(stamp)
    #print(numPasses)
    #print(velocity)
    if velocity > 50 or numPasses > 10:
        print("hello")
        #playFetch()

def calculate(magnetPass):
  global numPasses
  numPasses = numPasses + 1
  timeVal[0] = timeVal[1]
  timeVal[1] = magnetPass
  period = timeVal[1]-timeVal[0]
  #print(period)
  global velocity
  velocity = circumference/period
  #print(velocity)

def playFetch():
  #print(on_time)
  global dc
  p.ChangeDutyCycle(dc)
  dc = 5
  time.sleep(0.1)

def stopServo():
    global on_time
    on_time = 1.5
    p.ChangeFrequency(1000.0/(20.0+on_time))

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
  sensorCallback(12)
  try:
    # Loop until users quits with CTRL-C
    while True :
        time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    stopServo()
    p.stop()
    GPIO.cleanup()

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
   main()
