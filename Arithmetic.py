# Q) WAP to enter 2 number & any arithmetic operator & print appropriate?

a = int(input("Enter NO1: "))
b = int(input("Enter NO2: "))
c = input("Enter Operator: ")
d = 0

if c == "+":
    d = a + b
    print("\n ADDITION = "+str(d))
elif c == "-":
    d = a - b
    print("\n SUBTRACTION = "+str(d))
elif c == "*":
    d = a * b
    print("\n MULTIPLICATION = "+str(d))
elif c == "/":
    d = a / b
    print("\n DIVISION = "+str(d))
elif c == "%":
    d = b % a
    print("\n MOD = "+str(d))
else:
    print("\n\n Invalid Operator!")