# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 1, Due 2/21

import sys
import subprocess

# Continue looping until "end script" is read
while True:
    # read from stdin
    s = raw_input()
    # terminate if "end script"
    if s == "end script":
        break
    # otherwise send to fifo
    command = "echo " + s + " > video_fifo"
    subprocess.check_output(command, shell = True)
