import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = False
    num_valid = False
    pattern  = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)

    if match:
        # convert str ip address to integer
        ip_addr = []
        for i in range(1,4+1):
            num = match.group(i)
            if len(num) > 2 and num.startswith("0"):
                num_valid = False
                ip_addr.append(int(num))
                break
            else:
                ip_addr.append(int(num))
                num_valid = True

        # checking leading zero and validadity of each byte
        if ip_addr[0] != 0 and num_valid:
            for i in range(4): # index is list index not group
                if 0 <= ip_addr[i] <= 255:
                    valid = True
                else:
                    valid = False
                    break
        else:
            valid = False

    return valid

if __name__ == "__main__":
    main()
