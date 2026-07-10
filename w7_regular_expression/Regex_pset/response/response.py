from validator_collection import checkers

def main():
    email = input("What's your email address? ").strip()
    valid = checkers.is_email(email)
    if valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()