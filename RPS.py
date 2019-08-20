import random

print("Welcome to rock, paper, scissor")
print("Your options are as follows:")
print("Rock")
print("Paper")
print("Scissor")
print("Quit")

# ignore the varible below, it means nothing. It's sole purpose is to keep the game running
game_continue = 1

while game_continue == 1:
    option = input("Pick one to play: ")
    if option == "rock":
        print("You have chose rock")
        rps = random.randrange(0, 3)
        if rps == 0:
            print("The opponent has chosen rock, it's a tie")
        if rps == 1:
            print("The opponent has chosen paper, you lose")
        if rps == 2:
            print("The opponent has chosen scissor, you win")
    if option == "paper":
        print("You have chose paper")
        rps = random.randrange(0, 3)
        if rps == 0:
            print("The opponent has chosen rock, you win")
        if rps == 1:
            print("The opponent has chosen paper, it's a tie")
        if rps == 2:
            print("The opponent has chosen scissor, you lose")
    if option == "scissor":
        print("You have chose scissor")
        rps = random.randrange(0, 3)
        if rps == 0:
            print("The opponent has chosen rock, you lose")
        if rps == 1:
            print("The opponent has chosen paper, you win")
        if rps == 2:
            print("The opponent has chosen scissor, it's a tie")

    if option == "Quit":
        break




