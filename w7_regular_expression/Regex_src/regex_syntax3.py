import re

email = input("Enter your email: ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$",email):
    print("Valid")
else:
    print("Invalid")