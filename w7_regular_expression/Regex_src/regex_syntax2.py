import re

email = input("Enter your email: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    # [^@] means any chars except @
    print("Valid")
else:
    print("Invalid")