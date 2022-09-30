s1 = {10, 20, 30, "svit", "bit", "ntc", 50, 20, 500, 44, 10, 20, 33, 20}

for x in s1:
    print(x, end=" ")

s1.discard(20)
s1.add(1000)

print("")

for x in s1:
    print(x, end=" ")
    