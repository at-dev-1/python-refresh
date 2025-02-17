import random

roll = random.randint(1, 6)

guess = int(input("Guess a number between 1 and 6:\n "))

if guess == roll:
    print("You got it! The computer rolled " + str(roll))

else:
    print("Sorry, better luck next time. The computer rolled " + str(roll))