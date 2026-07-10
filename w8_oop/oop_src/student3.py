class Student:
    def __init__(self, name, house):
        self.name = name # trigger the name setter
        self.house = house # trigger the hosue setter

    
    # string method otherwise <__main__.Student object at 0x70bdf35bbce0>
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        house = input("House: ").strip()
        # cls = cls itself -> Student
        # same as Student(name, house)
        return cls(name, house)
    

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
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name # _name (Validated value) <-- name (Raw) if valid
    
            
def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()