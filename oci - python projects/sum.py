x1 = input()
x = list(map(int,x1.split()))
z = [i*i for i in x if (i % 2 != 0)]

print (z)
print ([i+i for i in z])#(sum(z))
