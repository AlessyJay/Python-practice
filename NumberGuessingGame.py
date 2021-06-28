import random
import sys

B = random.randint(0,50)

def game():
    while True:
        A = eval(input("Guess your number: "))

        if A < B:
            print("Try raising your number :)")
        elif A > B:
            print("Try lower your number :)")
        elif A == B:
            print("Congrats!")
            break

print(game())

ans = input("Do you want to continue playing? (Y/N)").upper()
if ans == "Y":
    game()
elif ans == "N":
    sys.exit