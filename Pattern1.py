# Q) WAP to draw a Pattern eg :- ↓ ?
# *****
# *****
# *****
# *****
# *****

no = int(input("Enter No : "))

for i in range(1, no+1):
    for j in range(1, no+1):
        print("*", end="")
    print("")