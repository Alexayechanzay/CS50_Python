greeting = input('Greeting: ').lower().strip()
first_char = greeting[0]
x = greeting.split(',')

leading_word = x[0]

if leading_word == 'hello':
    print("$0")
elif first_char == 'h':
    print('$20')
else:
    print('$100')

#Alternative approach

# greeting = input('Greeting: ').lower().strip()
# if 'hello' in greeting:
#     print('$0')
# elif 'h' in greeting[0]: #specifying the first letter in a string
#     print('$20')
# else:
#     print("$100")