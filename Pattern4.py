# Q) WAP to draw Pattern eg:- ↓ ?
# 12345
# 2345
# 345
# 45
# 5

no = int(input("Enter No: "))

for i in range(1, no+1):
    for j in range(i, no+1):
        print(" "+str(j), end="")
    print("")
    i += 1