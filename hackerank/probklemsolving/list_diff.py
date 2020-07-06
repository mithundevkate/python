t = [709552565, 473251358, 803612259, 579542802, 183012194, 689345248, 151290765, 123232501, 994391793, 25107191, 862726097]
v = [t[i+1]-t[i] for i in range(len(t)-1)]
k = 440987423

mylist = [3,4,5,2,1,1]
#max_diff =  [mylist[i+1]-mylist[i] for i in range(len(mylist)-1) if mylist[i]- mylist[i+1] ==j]

#print(max_diff)
l = []
count = ''


l = [9,5,8]
x = []
count = 1
for i in sorted(l):
    x.append(i*1)
    #m = i
    count = count + 1
    #x.append(i*1)
    #print(m,count)
    #x.append(i*count)
print(x)
print(sum(set(x)))
