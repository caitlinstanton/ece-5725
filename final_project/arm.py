import RPi.GPIO as GPIO
import time
import messages

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
  motion2 = [1.3,1.7]
  motion1 = [1.45,1.55]
  i = 0
  messages.send_sms("Pet in range")
  while not (GPIO.input(channel)):
      change_PWM(motion1[i%2],pet1)
      change_PWM(motion2[i%2],pet2)
      i = i + 1
      time.sleep(0.2)

def main():
	petCallback(19)

	try:
	  # Loop until users quits with CTRL-C
	  while True :
	      time.sleep(0.1)

	except KeyboardInterrupt:
	  # Reset GPIO settings
	  pet1.stop()
          pet2.stop()
	  GPIO.cleanup()

GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(19,GPIO.BOTH,callback=petCallback,bouncetime=200)

if __name__=="__main__":
   main()
