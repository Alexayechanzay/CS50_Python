import random

class Hat:
    # class variable
    houses = ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")

# Do not need to instantiate an instance/obj
# hat = Hat()

Hat.sort("Alex")

names = ["A","B","C",'D','E']
for name in names:
    Hat.sort(name)