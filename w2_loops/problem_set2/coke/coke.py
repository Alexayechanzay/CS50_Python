amount = 50
change = None
print('Amount Due: %s'%amount)
while amount != 0:
    coin = int(input('Insert coin: '))
    if coin <= amount:
        if coin == 25 or coin == 10 or coin == 5:
            amount = amount - coin
            print(f'Amount Due: {amount}')
        else:
            print(f'Amount Due: {amount}')
    else:
        change = coin - amount # greater
        print(f'Change Owed: {change}') # output change
        break

if amount == 0:
    print(f'Change Owed: {amount}') # output amount
