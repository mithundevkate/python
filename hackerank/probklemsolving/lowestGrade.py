students = [['Harry', 47.21], ['Berry', 37.2], ['Tina', 39], ['Akriti', 41], ['Harsh', 39]]
x = []
y = []
z = []

for i in range(1):
    z.append([1,'abc'])
print(z)
for i in students:
    print (i[1])
    x.append(i[1])
    y.append(i[0])



l = sorted(x)

newl = list(zip(l,y))
sorted = sorted(set(l))[1]

newl = []

for i in students:
    if i[1] == sorted:
        newl.append(i[0])
newl.sort()
print(newl)
