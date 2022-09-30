class Student:
    def __init__(self, sid, sna, sag):
        self.sid = sid
        self.sna = sna
        self.sag = sag

    def show(self):
        print(self.sid,":",self.sna,":",self.sag)


s1 = Student(101, "Vyomesh", 20)
s2 = Student(102, "Darsh", 23)
s3 = Student(103, "Karan", 25)

s1.show()
s2.show()

del s3