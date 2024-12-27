"""
rock paper scissors
"""

import random

options: list = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice: str = input("enter paper/rock/scissor: ")
print(computer_choice)

if user_choice != "rock" and user_choice != "scissors" and user_choice != "paper":
    print("invalid comment")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you win")
elif user_choice == computer_choice:
    print("you tie")
else:
    print("you lost")
