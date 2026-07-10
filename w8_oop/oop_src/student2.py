class Student:
    def __init__(self, name, house):
        self.name = name # trigger the name setter
        self.house = house # trigger the hosue setter

    
    # string method otherwise <__main__.Student object at 0x70bdf35bbce0>
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # private internal variable

    @property # Getter
    def name(self):
        return self._house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name # _name (Validated value) <-- name (Raw) if valid
            
def main():
    student = get_student()
    # house name is overwritten after being validated
    student.house = "Ravenclaw"
    print(student.house)

def get_student():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return Student(name, house)

if __name__ == "__main__":
    main()