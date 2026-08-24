print("Welcome to Rock Paper Scissors!")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

user_choice = input("Enter rock , paper, or scissors:")
print("You chose:",user_choice)

import random 

cholices = ["rock","paper","scissors"]
computer_choice = random.choice(choices)

print("Computer chose:",computer_choice)

if user_choice == computer_choice:
   while True:
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie! Rematching...")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        break
    else:
        print("Computer wins!")
        break

