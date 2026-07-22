def main():
    yell("This", "is", "CS50!")

def yell(*word_list):
    uppercased = []
    for word in word_list:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()