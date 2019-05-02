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

timeVal = [0,0]

def sensorCallback(channel):
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if GPIO.input(channel):
    # No magnet
    print("Sensor HIGH " + stamp)
  else:
    # Magnet
    print("Sensor LOW " + stamp)

def calculatePeriod(magnetPass):
  timeVal[0] = timeVal[1]
  timeVal[1] = magnetPass
  period = timeVal[1] - timeVal[0]

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
<<<<<<< HEAD
  sensorCallback(12)

=======
  #sensorCallback(18)
  #print(GPIO.input(18))
>>>>>>> 1d925e171e310745d8944121dcccd9d125c4a964
  try:
    # Loop until users quits with CTRL-C
    while True :
        if (GPIO.input(10) == False):
            print("yee magnet")
            GPIO.output(18,True)
        else:
            print("no magnet")
            GPIO.output(18,False)
        time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print("Setup GPIO pin as input on GPIO18")

# Set Switch GPIO as input
# Pull high by default
<<<<<<< HEAD
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=sensorCallback, bouncetime=200)
=======
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.BOTH, callback=sensorCallback, bouncetime=200)
GPIO.setup(18,GPIO.OUT)
>>>>>>> 1d925e171e310745d8944121dcccd9d125c4a964

if __name__=="__main__":
   main()
