#app.py
"""
Quick Dice Rolling Application (DiceRolling)

Uses input validation to roll a dice with x faces for y amount of times
"""

__author__ = "Maximus Barraza (Github: X86-Point5)"
__version__ = "1.0.0"
__date__ = "2025-04-30"

#uses random for generating rolls
import random



#prints the header for the dice roller
print("\n\t----- Dice Roller -----")

#counts the amount of faces
faces = 0

#loops until the right amount of faces is entered
while True:

    #inputs the string from the user
    input_string = input("\n\tEnter the amount of faces on each die: ")

    #checks to make sure that a positive number was entered
    if not input_string.isdigit():
        #outputs an error if a positive number was not entered
        print("\tError - Input must be a positive integer ")

    else:
        #converts the string to an integer value
        faces = int(input_string)

        #makes sure that faces is larger than one
        if faces < 2:
            #outputs an error if the face amount is too low
            print("\tError - Input must be greater than one ")
        else:
            #exits the loop if the right amount of faces was entered
            break

#counts the amount of rolls
rolls = 0

#loops until the right amount of rolls is entered
while True:

    #gets a string from the user
    input_string = input("\n\tEnter the amount of rolls: ")

    #checks if the string can be turned to a postive number
    if not input_string.isdigit():
        #informs the user that string entered was not valid
        print("\tError - Input must be a positive integer ")

    else: 
        #converts the string to an integer
        rolls = int(input_string)

        #the zero case
        if rolls < 1:
            #informs the user that the number can not be zero
            print("\tError - Input must be greater than zero ")
        else:
            #exits the loop if the right amount of rolls was entered
            break

#whitespace print
print()

#rolls for "rolls" amount of times
for roll in range(1, rolls + 1):

    #calculates the value with an rng
    value = random.randint(1, faces)
    #outputs the roll number and value
    print(f"\tRoll {roll}: {value}")
            