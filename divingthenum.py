#!/bin/python3
import random
import sys

GUESSNUM = 0
RANDNUM = 0


#generat rand int
RANDNUM = random.randint(1, 20)

#gets input assuring value is integer
print("Hey supposed human,")
try:
    GUESSNUM = int(input("try to divine a number between 1 & 20: "))
except ValueError:
    print("Please enter in an integer")
    sys.exit()

#compares guess against RANDNUM
if GUESSNUM > 20:
    print("Little high, but here it was anyway", RANDNUM)
elif GUESSNUM < 0:
    print("Shoot to low, here it is not that you tried", RANDNUM)
elif GUESSNUM == RANDNUM:
    print("You Wizard, you were correct in foreseeing", GUESSNUM)
else:
    print("So close but not even close - ", "you: ", GUESSNUM, "reality: ", RANDNUM)
