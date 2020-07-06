from collections import Counter

s  = 'qwertyuiopasdfghjklzxcvbnm'

#for i in range(len(list(s))):
 #   print(s.count(str(i)))


d = Counter(s)
l = {}
for item, ct in sorted(d.items()):
    #print ('%s occured %d times' % (item, ct))
    l[item] = ct

counter = 0
for i , j in list(l.items()):
    print(max(l , key=l.get) , l[max(l , key=l.get)])
    l.pop(max(l , key=l.get))
    counter = counter+1
    if counter == 3:
        break


