import RPi.GPIO as GPIO
import datetime
import time
HALL_SENSOR = 11

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HALL_SENSOR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def hallStatus():
    return GPIO.input(HALL_SENSOR)

def timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S UTC')

if __name__ == "__main__":
    init()
    while(True):
        print(hallStatus())
        print(timestamp())
        print("\n")
