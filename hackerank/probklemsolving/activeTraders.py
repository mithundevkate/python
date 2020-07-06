from collections import Counter
n = 10
arr = [1,1,1,3,1,5,5,7,7,7,8,8,8,8,8,9,9,9,9,2,2,2]

l = []
l1= []
l2 = []
x = []
abc = Counter(arr)
for i in abc.items():
    if i[1]/len(arr) * 100 > 5 :
        print(i[0])
        l.append(i[0])
        print(i[1]/len(arr) * 100)



#print("\n".join(x))
#rint(Counter(arr))
abc = ['mithun','ajay']
print(sorted(abc))
