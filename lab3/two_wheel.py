# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO

# Function for setting direction of a servo
# PWM_number is a pointer to a GPIO.PWM object
# Direction is a string equal to one of: - "stop"
#                                        - "clockwise"
#                                        - "counter-clockwise"
def set_direction(PWM_number, direction):
    # Set freq and dc based on desired direction
    if direction = "stop":
        freq = 50
        dc = 0
    if direction = "clockwise":
        freq = 46.948
        dc = 6.103
    if direction = "counter-clockwise":
        freq = 46.083
        dc = 7.834
    # Update servo with new values
    PWM_number.ChangeFrequency(freq)
    PWM_number.ChangeDutyCycle(dc)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize servo objects
left_servo = GPIO.PWM(13, 50)
right_servo = GPIO.PWM(26, 50)

# Left vs Right servo selected
left = False

# Interrupt function calls
def stop(channel):
    if left:
        set_direction(left_servo, "stop")
    else:
        set_direction(right_servo, "stop")
def clockwise(channel):
    if left:
        set_direction(left_servo, "clockwise")
    else:
        set_direction(right_servo, "clockwise")
def counter_clockwise(channel):
    if left:
        set_direction(left_servo, "counter-clockwise")
    else:
        set_direction(right_servo, "counter-clockwise")
def swap_servo(channel):
    left = not left

# Attach interrupts to falling edges
GPIO.add_event_detect(17, GPIO.FALLING, callback=counter_clockwise, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, callback=swap_servo, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=clockwise, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=stop, bouncetime=200)

# Wait until falling edge
try:
    GPIO.wait_for_edge(27, GPIO.FALLING)
except KeyboardInterrupt:
    GPIO.cleanup()
left_servo.stop()
right_servo.stop()
GPIO.cleanup()


