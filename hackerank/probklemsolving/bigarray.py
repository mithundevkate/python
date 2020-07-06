j = [1000000001, 1000000002, 1000000003, 1000000004 ,1000000005]
#k = [3,2,5]
#print(sum(j))

k = "fUn IS Good"
m = k.split()
#k = [i for i in m[::-1]]

l = []

for h in k:

    for i in h:
        if i == i.upper():
            i = i.lower()
            l.append(i)

        elif i == 'is':
            pass
        else:
            i = i.upper()
            l.append(i)

x = "".join(l).split()
print(" ".join(x[::-1]))

