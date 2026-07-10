def main():
    item_list = []
    value = 0
    while True:
        try:
            item = input()
            item_list.append(item)
        except EOFError:
            print('\n')
            data = {}
            item_list.sort()
            for i in item_list:
                value = item_list.count(i)
                i = i.upper()
                data[i]= value # append number of times with corresponding item
            for x,y in data.items(): # x is item and y is times
                print(f'{y} {x}')
            break

main()
# dict{'item':'Number of time'}
