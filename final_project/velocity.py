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
on_time = 1.3
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))

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
    if velocity > 50 or numPasses > 10:
      playFetch()

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
  p = GPIO.PWM(servoPin,freq)
  p.start(dc)

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
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.OUT)
GPIO.add_event_detect(12, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
   main()
