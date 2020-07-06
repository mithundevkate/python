



arr = [2,3,4,-3,5,-7,-8,0]
l = []
l1= []
l2 = []
x = []
for i in arr:
    if i > 0:
        l.append(i)
    elif i < 0:
        l1.append(i)
    else:
        l2.append(i)
print(len(l))
x.append(format(len(l)/len(arr),'.6f'))
x.append(format(len(l1)/len(arr),'.6f'))
x.append(format(len(l2)/len(arr),'.6f'))

print("\n".join(x))
