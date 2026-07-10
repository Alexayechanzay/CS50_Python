import re

def main():
    code = input("Hexadecimal color code: ").strip()
    pattern = r"^#[a-fA-F0-9]{6}$"
    if match := re.search(pattern, code):
        # matched text is stored as Match object
        # hence, use .group to retrieve the text
        print(f"Valid. Matched with {match.group()}")
        # group() = group(0)= entire text that matches the pattern
    else:
        print(f"Invalid.")

main()