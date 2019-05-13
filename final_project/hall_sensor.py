import time
import datetime
import RPi.GPIO as GPIO
import math
import messages
<<<<<<< HEAD
import socket 
=======
import socket
>>>>>>> 550bbe038e8c587abf7c0f385db9ecbf61b63eb1

timeVal = [0,0]
diameter = 15.24 #centimeters
circumference = math.pi*diameter
numPasses = 0
velocity = 0 #cm/s

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "socket successfully created"
port = 5725
s.bind(('',port))
print "socket binded to port %s" %(port)
s.listen(5)
print "socket is listening"
c,addr = s.accept()
print "c"
GPIO.setmode(GPIO.BCM)

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
        messages.send_sms("Playing fetch!")
        global c
        global addr
        print "got connection %s %s" %(c,addr)
        c.send("hi")
        c.close()

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

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
   main()
