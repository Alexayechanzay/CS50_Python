import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(time):
    pattern  = r"^(\d?\d?):?([0-5]?\d?) (AM|PM){1} to (\d?\d?):?([0-5]?\d?) (AM|PM){1}$"
    match = re.search(pattern, time)
    if match:
        # Validating time 
        if 1 <= int(match.group(1)) <= 12 and 1 <= int(match.group(4)) <= 12:

            # Conversion
            h1 = int(match.group(1))
            h2 = int(match.group(4))

            # handling minutes 
            m1 = int(match.group(2)) if len(match.group(2)) !=  0 else 0
            m2 = int(match.group(5)) if len(match.group(5)) != 0 else 0

            # standard 24-hour conversion rules
            # PM AND time = 12 is Noon
            # AM and time = 12 is Midnight 
            # AM (00:00 - 11:59)
            # PM (12:00 - 11:59)
            if match.group(3) == "PM" and h1 != 12:
                h1 = 12 + h1
            elif match.group(3) == "AM" and h1 == 12:
                h1 = 0 # Midnight
            # elif match.group(3) == "PM" and h1 == 12:
                h1 = h1 # Noon (So no changes)

            if match.group(6) == "PM" and h2 != 12:
                h2 += 12
            elif match.group(6) == "AM" and h2 == 12:
                h2 = 0 # Midnight
            # no condition for noon since there is no changes

            # return 24-h format
            return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
        else:
            raise ValueError # invalid 12-h time format
    else:
        raise ValueError # invalid input format
    
if __name__ == "__main__":
    main()