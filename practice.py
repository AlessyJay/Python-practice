import random
import os
import math
import re
import sys

n = random.randint(0,20)
while True:
    ans = int(input("Try guessing your number here: "))
    if ans < n:
        print("Too bad! Try raising your number!")
    elif ans > n:
        print("Too bad! try lowering your number!")
    elif ans == n:
        print("Congrats!")
        break