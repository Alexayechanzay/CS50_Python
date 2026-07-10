# using flag parameter in re.search
import re

# re.IGNORE case-insensitive matching
email = input("Enter your email: ").strip()

if re.search(r"^\w+@(\w+)?\w+\.edu$",email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")