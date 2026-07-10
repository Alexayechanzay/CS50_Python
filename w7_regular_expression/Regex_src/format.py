import re

name  = input("What's your name: ").strip()
# match = re.search(r"^(.+),[ ]?(.+)$",name)
# match = re.search(r"^(.+), (.+)$",name) 
# match = re.search(r"^(.+), *(.+)$",name) # , * means zeros or more repetitions of space
if match:= re.search(r"^(.+), *(.+)$",name):
    lname = match.group(1)
    fname = match.group(2)
    name = f"{fname} {lname}"
print(f"Hello, {name}")

"""
Standard Assignment (=): 
A statement that performs an action 
but returns nothing. You cannot place it inside 
loops or if conditions.

Walrus Assignment (:=): 
An expression that assigns the value 
and immediately returns that value. 
This allows you to combine assignment 
and evaluation into a single line
"""