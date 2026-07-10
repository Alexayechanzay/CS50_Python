user = input('Expression: ')
x,y,z = user.split(' ') # y -> arithmetic signs
x = int(x)
z = int(z)

if y == '+':
    ans = float(x+z)
elif y == '-':
    ans = float(x-z)
elif y == '*':
    ans = float(x*z)
else:
    ans = float(x/z)

print(f"{ans:.1f}")