class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self.name = name
        self.house = house

    
    # string method otherwise <__main__.Student object at 0x70bdf35bbce0>
    def __str__(self):
        return f"{self.name} from {self.house}"
    
            
def main():
    student = get_student()
    # house name is overwritten after being validated
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return Student(name, house)

if __name__ == "__main__":
    main()