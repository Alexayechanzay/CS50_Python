# names = []

# for i in range(3):
#     names.append(input("What's your name: "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")

# with open('file_name','mode') as variable:
    # code block

# write line
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")

# read lines
# with open("names.txt",'r') as file:
#     lines = file.readlines() # return the line as one element in a list


# for line in lines:
#     # print(f"hello, {line}",end='')
#     print(f"hello, {line.rstrip()}")

with open("names.txt",'r') as file:
    for line in sorted(file,reverse = True):
        print("hello",line.rstrip())

names = []

with open("names.txt") as file:
    for lines in file:
        names.append(lines.rstrip())

for name in sorted(names):
    print('hello,',name)

