# Q) WAP to draw a Pattern eg :- ↓ ?
# *
# **
# ***
# ****
# *****

no = int(input("Enter No: "))

# i for columns & j for rows

for i in range(1, no+1):
    for j in range(1, i+1):
        print("*", end="")
    print("")