a = [3,1,4,6,5]
b = [9,8,3,15,1]
l = []
for i , j in zip(a,b):

    result = min(min(a),min(b))
    print(i,j , '-->',result)
l3 = zip(sorted(a), sorted(b))
s = 0

for i in l3:
    print(abs(i[0]-i[1]))
    s += abs(i[0] -i[1])
print(s)

