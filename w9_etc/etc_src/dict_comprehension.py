students = ["Hermione", "Harry", "Ron"]

#gryffindors = [{"name": std, "house":"Gryffindor"} for std in students]
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)