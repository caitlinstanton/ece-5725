# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO_pin = 13

# Initial PWM parameters
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)
print("Stopped")
time.sleep(3.0)

# Take 10 clockwise steps
print("Clockwise")
for i in range(10):
    on_time = on_time - 0.05 
    # Calculate new freq and dc based on new on_time
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    print("\nPulse width: " + str(on_time))
    print("Duty cycle: " + str(dc))
    print("Frequency: " + str(freq))
    # Update PWM
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)
    time.sleep(3.0)
    
# Reset
on_time = 1.5

# Take 10 counter-clockwise steps
print ("Counter-clockwise")
for i in range(10):
    on_time = on_time + 0.05 
    # Calculate new freq and dc
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    print("\nPulse width: " + str(on_time))
    print("Duty cycle: " + str(dc))
    print("Frequency: " + str(freq))
    # Update PWM
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)
    time.sleep(3.0)

# Stop at end
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
time.sleep(3.0)

p.stop()
GPIO.cleanup()
