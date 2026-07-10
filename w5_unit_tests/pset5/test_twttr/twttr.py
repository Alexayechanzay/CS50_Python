def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    sentence = ""
    for i in word:
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            sentence += i
    return sentence

if __name__ == "__main__":
    main()

