# Q) WAP to draw Pattern eg:- ↓ ?
#    *
#   ***
#  *****
# *******

no = int(input("Enter Rows: "))
m = 1

for i in range(1, no+1):
    for j in range(i, no+1):
        print(" ", end="")
        j = j + 1
    for j in range(1, m+1):
        print("*", end="")
        j = j + 1
    i = i + 1
    print("\n")
    m = m + 2