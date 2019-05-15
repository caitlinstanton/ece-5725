import time
import datetime
import RPi.GPIO as GPIO
import math
import socket

import messages
#import servomotion
GPIO.setmode(GPIO.BCM)

timeVal = [0,0]
diameter = 15.24 #centimeters
circumference = math.pi*diameter
numPasses = 0
velocity = 0 #cm/s

GPIO_pin = 13
on_time = 1.2
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
GPIO.setup(13,GPIO.OUT)
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)
food_time = (15,21)
current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)

#GPIO.setmode(GPIO.BCM)

def fetchCallback(channel):
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
        print "hall"
        global numPasses
        #messages.send_sms("Playing fetch!")
        '''s = socket.socket()
        s.connect(('10.148.12.144',5725))
        print "connected"
        server = s.recv(1024)
        s.close()'''
        numPasses = 0

def calculate(magnetPass):
  global numPasses
  numPasses = numPasses + 1
  timeVal[0] = timeVal[1]
  timeVal[1] = magnetPass
  period = timeVal[1]-timeVal[0]
  global velocity
  velocity = circumference/period

def change_PWM(on_time, p):
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)

def petCallback(channel):
  if not (GPIO.input(channel)):
      print "Pet in range"
      #servomotion.pet()

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
  fetchCallback(12)
  petCallback(13)
  global current_time

  while (food_time != current_time):
      current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
  print("Time for food!")

  change_PWM(2, p)
  time.sleep(1)
  while GPIO.input(5):
      pass
  change_PWM(1.2, p)

  try:
    # Loop until users quits with CTRL-C
    while True :
        time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    p.stop()
    GPIO.cleanup()

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=fetchCallback, bouncetime=200)
#GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(13,GPIO.BOTH,callback=petCallback,bouncetime=200)

#GPIO.setup(13, GPIO.OUT)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)

if __name__=="__main__":
   main()
