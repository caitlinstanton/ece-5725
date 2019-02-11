import sys
import subprocess

while True:
    s = raw_input()
    if s == "end script":
        break
    command = "echo " + s + " > video_fifo"
    subprocess.check_output(command, shell = True)
