"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""


import random

import sys

def start_game(): 
    number = random.randint(1, 10)  
    number_guesses =0      
    print("Welcome to the Guessing Game!")
    while True:
        try:
            guess = int(input("Please guess the number 1 through 10: "))
            if guess >= 11:            
                print("\nThe number is not within the range. Try again...")
            if guess <= 0:
                print("\nThe number is not within the range. Try again...")
        except ValueError:
            print("Oh no! That's invalid entry, Try again...")
        else:        
            if guess < number:
                print("Your number is lower than the guessing number.")
                number_guesses += 1
            if guess > number:
                print("Your number is higher than the guessing number.")
                number_guesses += 1
            if guess == number:
                guess = int(input("Got it! You guessed the number in {} guesses! The Game is Over! Have a great day!".format(number_guesses)))
            
            
start_game()