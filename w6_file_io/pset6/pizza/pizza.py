import csv
import tabulate
import sys

datas = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguemnts")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguemnts")
else:
    if sys.argv[1].endswith(".csv"):

        try:
            with open(sys.argv[1],'r') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    datas.append(line)

                print(tabulate.tabulate(datas,headers="keys",tablefmt="grid"))
        except (FileNotFoundError):
            sys.exit("File does not exit")
    else:
        sys.exit("Not a CSV file")
