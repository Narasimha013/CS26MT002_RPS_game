print("Welcome to Rock Paper Scissors!")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

user_cholice = input("Enter rock , paper, or scissors:")
print("You chose:",user_choice)

import random 

cholices = ["rock","paper","scissors"]
computer_choice = random.choice(choices)

print("Computer chose:",computer_choice)