#!/usr/bin/python


import time
import sys


# Initiate vars
PTWORK = 0
PTWAIT = 0
PTCOUNT = 1

# Test args to assure they are integers
try:
    PTWORK = int(sys.argv[1])
    PTWAIT = int(sys.argv[2])
except (ValueError, IndexError):
    print("Requriers work time and wait time in minutes as arguments")
    sys.exit()

#convert time to minutes
PTWORK *= 60
PTWAIT *= 60

while True:
    print("---TASKS---")
    time.sleep(int(PTWORK))
    print("---Good, now have some fun---")
    time.sleep(int(PTWAIT))
    PTCOUNT += 1
    print("|||Pomodero cycles: ", PTCOUNT, "|||")
    PTCOUNT = PTCOUNT + 1
