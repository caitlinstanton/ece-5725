import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
pet1 = GPIO.PWM(20, freq)
pet2 = GPIO.PWM(21,freq)
pet1.start(dc)
pet2.start(dc)

def change_PWM(on_time, p):
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)

def petCallback(channel):
  motion = [1.3,1.7]
  i = 0
  while not (GPIO.input(channel)):
      print "Pet in range"
      change_PWM(pet1,motion[i%2])
      change_PWM(pet2,motion[i%2])
      i = i + 1

def main():
	petCallback(19)

	try:
	  # Loop until users quits with CTRL-C
	  while True :
	      time.sleep(0.1)

	except KeyboardInterrupt:
	  # Reset GPIO settings
	  p.stop()
	  GPIO.cleanup()

GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(19,GPIO.BOTH,callback=petCallback,bouncetime=200)

p.stop()
GPIO.cleanup()

if __name__=="__main__":
   main()