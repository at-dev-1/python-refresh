
import random


def roll_dice():
    dice_total= random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1= input("Enter player 1 name: ")
    player2= input("Enter player 2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, " rolled a total of ", roll1)
    print(player2, " rolled a total of ", roll2)

    if roll1 > roll2:
        print(player1, " wins!")
    elif roll2 > roll1:
        print(player2, " wins!")
    else:
        print("It's a tie!")

main()