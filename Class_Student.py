# Q) WAP to create class student pass id, name, age & marks of 3 subjects & print total marks & percentage?

class Student:
    def __init__(self, id, name, age, submarks1, submarks2, submarks3):
        self.id = id
        self.name = name
        self.age = age
        self.submarks1 = submarks1
        self.submarks2 = submarks2
        self.submarks3 = submarks3

    def show(self):
        print("")
        print("Student Id: ",self.id)
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)
        total = self.submarks1 + self.submarks2 + self.submarks3
        per = total / 3
        print("\n Total: ",total)
        print("\n Percentage: ",per)

submarks1 = int(input("Enter marks of subject 1: "))
submarks2 = int(input("Enter marks of subject 2: "))
submarks3 = int(input("Enter marks of subject 3: "))

s1 = Student(1, "Vyomesh", 20, submarks1, submarks2, submarks3)

s1.show()