import sys
import random

sum = {"Rock":1, "Paper":1, "Scissors":1}
B = random.choice(sum)

print(B)

def game():
    while True: 
        #A = input("Your turn: ")
        B = random(sum)

        """if Rock == Paper:
            Rock - 1
        elif Rock == Scissors:
            Scissors - 1
        elif Paper == Scissors:
            Paper - 1"""
