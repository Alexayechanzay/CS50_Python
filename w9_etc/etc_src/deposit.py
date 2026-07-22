balance = 0

def main():
    print(f"balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"balance: {balance}")

def deposit(n):
    # Raise UnboundLocalError: Cannot assign new value to Global var
    # balance += n

    # solution: keyw global
    global balance
    balance += n

def withdraw(n):
    # Raise UnboundLocalError: Cannot assign new value to Global var
    # balance -= n

    global balance
    balance -= n

if __name__ == "__main__":
    main()