#import sys

#if len(sys.argv) == 1:
    #print("meow")
#elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#    n = sys.argv[2]
#    print(int(n) * "meow\n")
#else:
#    print("usage: meows.py [-n NUMBER]")

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat n times")
parser.add_argument("-n", help="number of times to meow", default=1, type=int) # tell argparse expected arg from user
args = parser.parse_args() # ensure that all args have been included properly
#print(args.n)

for _ in range(args.n):
    print("mewo")