print("This is a program to create a rock-paper-scissors game:")

import random

choice=["rock", "paper", "scissors"]
comp_choice= random.choice(choice)

def play_game(user_choice):
    if user_choice=="rock" and comp_choice=="scissors":
        return("User: 1; Comp: 0")
    elif user_choice=="paper" and comp_choice=="rock":
        return("User: 1; Comp: 0")
    elif user_choice=="scissors" and comp_choice=="paper":
        return("User: 1; Comp: 0")
    elif user_choice==comp_choice:
        return("Its a tie")
    else:
        return("User: 0; Comp: 1")

while True:
    user_choice=input("Enter your choice: rock, paper or scissors:")
    print("The choice of the user is:", user_choice, "and the choice of the computer is:", comp_choice)

    result=play_game(user_choice)
    print("The result of the game is:", result)

    play_again= input("Do you want to play again? Type Yes or No:")

    if play_again != "Yes":
        break

    
