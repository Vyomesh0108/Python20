# Q) WAP to create class employee pass id, name, & salary & print income tax & net salary?

class Employee:
    def __init__(self, eid, ename, esalary):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary

    def show(self):
        print(self.eid,":",self.ename)
        tax = self.esalary * 10 / 100
        net = self.esalary - tax
        print("SALARY : ",self.esalary)
        print("INCOME TAX : ",tax)
        print("NET SALARY : ",net)
        print(" ")


e1 = Employee(1, "Vyomesh", 150000)
e2 = Employee(2, "Darsh", 175000)
e3 = Employee(3, "Dhyeya", 125000)

e1.show()
e2.show()
e3.show()