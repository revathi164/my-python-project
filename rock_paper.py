import random

while True:
    choice = ["rock","paper","scissor"]

    computer = random.choice(choice)
    player = None
    while player not in choice:
        player = input("rock, Paper, or Scissor?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("you lose")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you Win")

    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")

    elif player == "scissor":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")

    play_again = input("Do you want to play again?(yes/no): ").lower()

    if play_again != "yes":
        break

print("Thank you for playing")