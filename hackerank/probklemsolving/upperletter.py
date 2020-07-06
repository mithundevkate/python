from collections import Counter
s = 'mithun devkate'
s = str(s)
print(s.title())
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

s = 'AABCAAADA'
num = 3
z = list(map(''.join, zip(*[iter(s)]*3)))
for i in z:
    #print(Counter(i))
    print ("".join(set(i)))
l = [1,2]
t = tuple(l)
print(hash(t))
