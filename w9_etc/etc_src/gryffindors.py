students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
#print(gryffindors) # return a filter obj

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    #print(gryffindor)
    print(gryffindor["name"])