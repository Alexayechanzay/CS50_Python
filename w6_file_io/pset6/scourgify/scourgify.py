import sys
import csv

address = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many commadn-line arguments")
else:
    if sys.argv[1].endswith(".csv"):
        try:
            # Read file
            with open(sys.argv[1]) as read_file:
                reader = csv.DictReader(read_file)

                # creating a list
                for row in reader:
                    last, first = row["name"].split(",")
                    address.append({"first":first.strip(), "last":last.strip(), "house":row["house"].strip()})

                # write file
                with open(sys.argv[2],'w') as write_file:
                    writer = csv.DictWriter(write_file, fieldnames=['first','last','house'])

                    # writing into a new file
                    writer.writeheader()
                    writer.writerows(address)

        except (FileNotFoundError):
            sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file")
