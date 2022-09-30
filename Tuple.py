l = [10, 20, "hello", "nice", 30, 40, 20]
t1 = (10, 20, "hello", "nice", 20)

l[1] = 200
# t1[1] = 200       # Tuple cannot be modified

t2 = (40, 50, 60)
t1 = t1 + t2

for x in l:
    print(x, )

print("")

for x in t1:
    print(x, )

print("")

print(t1[2])
print(t1[1:4])
print(t1[-1])
print(t1[-3])
