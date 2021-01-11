#!/bin/python3
import random
import sys


GUESSNUM = 0
RANDNUM = 0
MINNUM = 0
MAXNUM = 0


# Retrieve low/high number from args
try:
    MINNUM = int(sys.argv[1])
    MAXNUM = int(sys.argv[2])
except (IndexError, ValueError):
    print("Please add a min and max number to the arguments")
    sys.exit(0)

# Generat rand int
RANDNUM = random.randint(MINNUM, MAXNUM)

# Gets input assuring value is integer
print("Hey supposed human,")
try:
    print("try to divine a number between", MINNUM, "&", MAXNUM, ": ")
    GUESSNUM = int(input())
except ValueError:
    print("Please enter in an integer")
    sys.exit()

# Compares guess against RANDNUM
if GUESSNUM > 20:
    print("Little high, but here it was anyway", RANDNUM)
elif GUESSNUM < 0:
    print("Shoot to low, here it is not that you tried", RANDNUM)
elif GUESSNUM == RANDNUM:
    print("You Wizard, you were correct in foreseeing", GUESSNUM)
else:
    print("So close but not even close - ", "you: ", GUESSNUM, "reality: ", RANDNUM)
