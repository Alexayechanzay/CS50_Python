def main():
    yell("This", "is", "CS50P")
    yell2("This","is","CS50x")

def yell(*words):
    uppercased = map(str.upper,words)
    print(*uppercased)

## ALT: list comprehension 
def yell2(*words: tuple) -> str:
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()