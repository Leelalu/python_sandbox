#!/bin/python3
import random


RANDNUM = 0
CHOICE = ''
RPS = {1 : "rock", 2 : "paper", 3 : "sissors"}


# Set random number determining computers play
RANDNUM = random.randint(1, 3)


# Main program
# Get input for player choice
print(" == =Rock  Paper  Sissors == =\n")
CHOICE = input("Whats your CHOICE, rock, paper, or sissors: ")

# Respond to input
if CHOICE == "rock":
    if RPS[RANDNUM] == "rock":
        print("A tie between the rocks")
    if RPS[RANDNUM] == "paper":
        print("You lost Rock vs Paper")
    if RPS[RANDNUM] == "sissors":
        print("You won Rock vs Sissors")
elif CHOICE == "paper":
    if RPS[RANDNUM] == "rock":
        print("You won Paper vs Rock")
    if RPS[RANDNUM] == "paper":
        print("A tie between the papers")
    if RPS[RANDNUM] == "sissors":
        print("You lost Paper vs Sissors")
if CHOICE == "sissors":
    if RPS[RANDNUM] == "rock":
        print("You lost Sissors vs Rock")
    if RPS[RANDNUM] == "paper":
        print("You won Sissors vs Paper")
    if RPS[RANDNUM] == "sissors":
        print("A tie between the sissors")
# If input incorrect reply
else:
    print("Please enter rock, paper, or sissors.")
