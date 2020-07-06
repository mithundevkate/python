j = [4,2,3]
k = [3,2,5]
#print(sum(j))
count = 0
count1 = 0
newl= []
newj = []
for i,l in zip(j,k):

    if i > l:
        count = count + 1
        print('first' , count)
    elif i == l:
        pass
    else:
        count1 = count1 + 1
        print('second' , count1)
newl.append(count)
newl.append(count1)

print(newl)
