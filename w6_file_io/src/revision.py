names_list = []

with open("names.txt",'r') as file:
    for line in file:
        names_list.append(line.rstrip())

    for name in sorted(names_list):
        print(name)
