# Q) WAP to find Factorial of a given number?

no = int(input("Enter No: "))
f = 1

while no >= 1:
    f = f * no
    no -= 1

print("\n FACTORIAL : "+str(f))