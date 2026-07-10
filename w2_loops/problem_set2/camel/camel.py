CamelCase = input('CamelCase: ').strip()
snake_case = ''

for letter in CamelCase:
    if letter.isupper(): #upper
        letter = letter.lower()
        snake = '_' + letter
        snake_case += snake
    else: #lower
        snake_case += letter
print(snake_case.lstrip("_"))
