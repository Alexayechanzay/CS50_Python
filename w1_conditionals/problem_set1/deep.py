user = input("what is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
user = user.replace('-',' ')
if user == "42" or user =='forty two':
    print('Yes')
else:
    print('No')