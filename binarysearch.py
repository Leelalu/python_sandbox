#!/usr/bin/python3


import sys


HIGHNUM = 100
LOWNUM = 0
GUESSNUM = 0
USRCHOICE = ""

#try to get vars
try:
    LOWNUM = int(sys.argv[1])
    HIGHNUM = int(sys.argv[2])
except (IndexError, ValueError):
    print("Please add a min and max number to the arguments")
    sys.exit(0)

#set base for binary loop
GUESSNUM = int((LOWNUM+HIGHNUM)/2)


#binary search loop
while USRCHOICE != "r" and LOWNUM != GUESSNUM and HIGHNUM != GUESSNUM:

    print("Is", GUESSNUM, "the right number?")
    USRCHOICE = input("(h)igher, (l)ower, or (r)ight: ")

    if USRCHOICE == "h":
        LOWNUM == GUESSNUM
    if USRCHOICE == "l":
        HIGHNUM = GUESSNUM

    GUESSNUM = int((LOWNUM+HIGHNUM)/2)

print("The Number is: ", GUESSNUM)
