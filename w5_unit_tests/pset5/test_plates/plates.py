def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    # Length check
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            if s.isalnum():

                start = 0
                for i in range(len(s)):
                    if s[i].isdigit():
                        start = i
                        break

                if s[start] != '0':
                    if not (s.isalpha()):
                        if s[start:].isdigit():
                            return True
                        else:
                            return False
                    else:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()

