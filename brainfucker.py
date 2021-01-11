#!/usr/bin/python3


import sys
import readchar


# Create vars
CELLSPNTR = 0
CELLS = [ 0 ]
LOOPSTARTS = []
STRPNTR = 0
FILESTR = ""

# Attempt to open given file
try:
    FILESTR = open(sys.argv[1], 'r').read()
except IndexError:
    print('Error: Requires bf file')
    sys.exit()
except FileNotFoundError:
    print('Error: File nonexistent')
    sys.exit()


# Main program loop for interpreter
while STRPNTR < len(FILESTR):
    char = FILESTR[STRPNTR]


    # Check char, if Brainfuck command process accordingly
    if char == '>':
        CELLSPNTR = CELLSPNTR + 1
        if CELLSPNTR > len(CELLS)-1:
            CELLS.append(0)
    elif char == '<':
        CELLSPNTR = CELLSPNTR - 1
        if CELLSPNTR < 0:
            CELLSPNTR = len(CELLS)
    elif char == '+':
        CELLS[CELLSPNTR] = CELLS[CELLSPNTR]+1
    elif char == '-':
        CELLS[CELLSPNTR] = CELLS[CELLSPNTR]-1
    elif char == '.':
        print(chr(CELLS[CELLSPNTR]))
    elif char == ',':
        CELLS[CELLSPNTR] = ord(readchar.readchar())
    elif char == '[':
        LOOPSTARTS.append(STRPNTR)
    elif char == ']':
        if CELLS[CELLSPNTR] == 0:
            LOOPSTARTS.pop(-1)
        else:
            STRPNTR = LOOPSTARTS[-1]
    # Lack of char represents EOF
    else:
        if not char:
            break

    STRPNTR = STRPNTR+1
