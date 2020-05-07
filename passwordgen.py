#!/usr/bin/python3


import string
import secrets
import sys


CHARSTR = ""
PASSWORD = ""
PASSLEN = 0

# Get int for password lengt
try:
    PASSLEN = int(sys.argv[1])
except (ValueError, IndexError):
    print("Needs an number as an argument")

#gen string to retrieve chars from
CHARSTR = string.ascii_letters+string.punctuation+string.digits

#put rand char in password var
for char in range(PASSLEN):
    PASSWORD += secrets.choice(CHARSTR)

print(PASSWORD)
