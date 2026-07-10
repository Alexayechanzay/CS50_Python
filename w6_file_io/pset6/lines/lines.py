import sys

lst = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguemnts")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1],'r') as file:

                file = file.readlines()

                for line in file:
                    if not (line.lstrip(' ').startswith(('\n','#'))):
                        lst.append(line)
                print(len(lst))

        except (FileNotFoundError):
            sys.exit("File does not exit")
    else:
        sys.exit("Not a Python file")
