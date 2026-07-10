import random
import sys

def main():
    total = 10
    score = 0
    level = get_level()

    while total != 0:
        x,y = generate_integer(level)

        count = 0
        while count < 3 :
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess != (x+y):
                    print("EEE")
                else:
                    break
            except ValueError:
                print('EEE')

            count += 1


        # After 3 attemps
        if guess == (x+y):
            score += 1
        else: # auto-display the answer
            print(f"{x} + {y} = {x+y}")

        total -= 1
    print(f'score: {score}')
    sys.exit()

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit():
            if int(level) in [1,2,3]:
                return float(level)


def generate_integer(level):
    if type(level) == float:
        level = int(level)
        lower = 10 ** (level - 1)
        upper = (10 ** level) - 1
        if level != 1:
            x,y = random.randint(lower,upper),random.randint(lower,upper)
        else:
            x,y = random.randint(lower-1,upper),random.randint(lower-1,upper)
        return x,y
    else:
        raise ValueError
if __name__ == "__main__":
    main()
