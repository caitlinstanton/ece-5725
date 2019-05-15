import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def sensorCallback(channel):
    print GPIO.input(channel)
    '''
    if GPIO.input(channel):
        print "not close"
    else:
        print "wow omg"'''


GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(13,GPIO.BOTH,callback=sensorCallback,bouncetime=200)

if __name__=="__main__":
    try:
        while True:
            sensorCallback(13)
    except KeyboardInterrupt:
        GPIO.cleanup()
