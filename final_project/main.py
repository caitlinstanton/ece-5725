import time
import datetime
import RPi.GPIO as GPIO
import math
import socket
import messages

GPIO.setmode(GPIO.BCM)

# Variables to be used for fetch 
timeVal = [0,0]
diameter = 15.24 #centimeters
circumference = math.pi*diameter
numPasses = 0
velocity = 0 #cm/s

# Variables to be used for food dispenser
GPIO_pin = 13
on_time = 1.2
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
food = GPIO.PWM(GPIO_pin, freq)
food.start(dc)
food_time = (15,55)
current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)

# Variables to be used for petting
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
pet1 = GPIO.PWM(20, freq)
pet2 = GPIO.PWM(21,freq)
pet1.start(dc)
pet2.start(dc)

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
    if velocity > 50 or numPasses > 10:
        global numPasses
        messages.send_sms("Playing fetch!")
        # connect to Pi zero
        s = socket.socket()
        s.connect(('10.148.12.144',5725))
        print "connected"
        server = s.recv(1024)
        s.close()
        numPasses = 0

# Update velocity
def calculate(magnetPass):
  global numPasses
  numPasses = numPasses + 1
  timeVal[0] = timeVal[1]
  timeVal[1] = magnetPass
  period = timeVal[1]-timeVal[0]
  global velocity
  velocity = circumference/period

# Changes PWM signal of p to be high for "on_time" microseconds
def change_PWM(on_time, p):
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)

# ISR for petting arm
def petCallback(channel):
  motion = [1.3,1.7]
  i = 0
  while not (GPIO.input(channel)):
      print "Pet in range"
      change_PWM(pet1,motion[i%2])
      change_PWM(pet2,motion[i%2])
      i = i + 1



def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.
  global current_time

  # Wait until feeding time
  while (food_time != current_time):
      current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
  print("Time for food!")

  # Open tank
  change_PWM(2.5, food)
  time.sleep(1)
  while GPIO.input(5):
      pass
  # close tank
  change_PWM(1.2, food)

  try:
    # Loop until users quits with CTRL-C
    while True :
        time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    p.stop()
    GPIO.cleanup()

# Set Switch GPIO as input
# Setup ISRs
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=fetchCallback, bouncetime=200)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(13,GPIO.BOTH,callback=petCallback,bouncetime=200)

if __name__=="__main__":
   main()
