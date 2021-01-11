#!/usr/bin/python3


import sys


HIGHNUM = 0
LOWNUM = 0
GUESSNUM = 0
USRCHOICE = ""


# Retrieve low/high number from args
try:
    LOWNUM = int(sys.argv[1])
    HIGHNUM = int(sys.argv[2])
except (IndexError, ValueError):
    print("Please add a min and max number to the arguments")
    sys.exit(0)

# Set a guess number between the lowest and highest number
GUESSNUM = int((LOWNUM+HIGHNUM)/2)

def main():
    # Main prorgram loop for binary search
    while USRCHOICE != "r" and LOWNUM != GUESSNUM and HIGHNUM != GUESSNUM:
    
        print("Is", GUESSNUM, "the right number?")
        USRCHOICE = input("(h)igher, (l)ower, or (r)ight: ")
    
        if USRCHOICE == "h":
            LOWNUM = GUESSNUM
        elif USRCHOICE == "l":
            HIGHNUM = GUESSNUM
    
        GUESSNUM = int((LOWNUM+HIGHNUM)/2)
    
    print("The Number is: ", GUESSNUM)

if __name__ == "__main__":
    main()
