# AI-generated version 
"""
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if not match:
        return False

    for group in match.groups():
        # leading zero check
        if len(group) > 1 and group.startswith("0"):
            return False

        # range check
        if not (0 <= int(group) <= 255):
            return False

    return True


if __name__ == "__main__":
    main()

"""