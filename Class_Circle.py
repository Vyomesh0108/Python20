# Q) WAP to create class circle, enter radius & print area of circle?

class Circle:
    def __init__(self, r):
        self.r = r

    def show(self):
        area = pie * self.r * self.r
        print("\n Area of Circle: ",area)


pie = 3.14
r = int(input("Enter Radius: "))

c1 = Circle(r)
c1.show()