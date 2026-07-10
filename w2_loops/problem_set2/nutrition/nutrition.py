fruit_fact = {
    'Apple' : 130,'Avocado' : 50,'Banana': 110,
    'Cantapoupe' : 50,"Grapefruit" : 60,'Grapes' : 90,
    'Honeydew Melon' : 50,'Kiwifruit' : 90,'Lemon' : 15,
    'Lime': 20, "Nectarine" : 60,'Orange' : 80,
    'Peach' : 60,
    'Pear' :100,
    'Pineapple' : 50,
    'Plums' : 70,
    "Strawberries" : 50,
    'Sweet Cherries': 100,
    'Tangerine' : 50,
    'Watermelon' : 80
}

prompt  = input('Item: ')
prompt = prompt.split(' ') # return a list 

text = [ x.capitalize() for x in prompt ] # capitalize each first letter in the list
separator = ' ' # separated by a space
full_text = separator.join(text) # to join elements from list into one string


if full_text in fruit_fact:
    calories = fruit_fact.get(full_text,None)
    print(f'Calories: {calories}')

