import re 
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # to match the word  "...um..." exactly
    pattern = r"\bum\b"
    # match store the No. of "um" in a list
    match = re.findall(pattern, s, re.I)
    return len(match) if match else 0

if __name__ == "__main__":
    main()