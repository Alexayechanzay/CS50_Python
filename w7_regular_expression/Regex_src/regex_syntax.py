import re

email = input("Enter your email: ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    # [^@] means any chars except @
    print("Valid")
else:
    print("Invalid")