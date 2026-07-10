import random
import sys

valid = True

while True:
    # validation test
    while valid:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level > 0:  # positive nums
                secret_num = random.randint(1, level)
                valid = False

    # uesr input
    guess = input("Guess: ")
    if guess.isdigit():
        # checking
        guess = int(guess)
        if guess < secret_num:
            print("Too small!")
        elif guess > secret_num:
            print("Too large!")
        else:  # equal
            print("Just right!")
            sys.exit()  # break
