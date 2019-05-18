# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Final Project

import time
import datetime
import RPi.GPIO as GPIO
import math
import socket
import messages

GPIO.setmode(GPIO.BCM)

# Variables for fetch
timeVal = [0,0]
diameter = 15.24 #centimeters
circumference = math.pi*diameter
numPasses = 0
velocity = 0 #cm/s

# ISR to be called
def fetchCallback(channel):
  # Called if sensor output changes
  stamp = time.time()
  if GPIO.input(channel):
    # No magnet
    print("Sensor HIGH")
  else:
    # Magnet
    print("Sensor LOW")
    calculate(stamp)
    global velocity
    if velocity > 200:
        print "hall"
        # Connect to Pi zero
        messages.send_sms("Playing fetch!")
        s = socket.socket()
        s.connect(('10.148.12.144',5725))
        print "connected"
        server = s.recv(1024)
        s.close()
        velocity = 0

# Update velocity
def calculate(magnetPass):
  global numPasses
  numPasses = numPasses + 1
  timeVal[0] = timeVal[1]
  timeVal[1] = magnetPass
  period = timeVal[1]-timeVal[0]
  global velocity
  velocity = circumference/period

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
  fetchCallback(12)
  
  try:
    # Loop until users quits with CTRL-C
    while True :
        time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=fetchCallback, bouncetime=200)

if __name__=="__main__":
   main()
