modi_str = ''
vowel = ['a','e','i','o','u']
text = input('input: ')
for char in text:
    if char.lower() in vowel:
        del char
    else:
        modi_str += char

print('Output: {}'.format(modi_str))
