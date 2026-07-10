menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total = 0 # not to overwrite,thus initialize outside the loop
while True:
    try:
        item = input('Item: ').lower()
        if item in menu:
            total += menu.get(item)
            print(f'${total:.2f}')
    except EOFError:
        print() # to display the reprompt in new line
        break # break when ctr+d entered
    except KeyError:
        pass
