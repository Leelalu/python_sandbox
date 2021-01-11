#!/usr/bin/python3


import string
import secrets
import sys


CHARSTR = ""
PASSWORD = ""
PASSLEN = 0

# Get int for password length
try:
    PASSLEN = int(sys.argv[1])
except (ValueError, IndexError):
    print("Needs an number as an argument")

# Gen string of charectors
CHARSTR = string.ascii_letters+string.punctuation+string.digits

# Put rand char from CHARSTR in password var
for char in range(PASSLEN):
    PASSWORD += secrets.choice(CHARSTR)

# Output result
print(PASSWORD)
