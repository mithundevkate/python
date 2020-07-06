l = '1222311'
a = map(int,list(l))
print(a)
from itertools import groupby
import itertools
from operator import itemgetter


a = sorted(a)

for key, value in groupby(a):
    print((len(list(value)), int(key)), end=' ')
for k, g in itertools.groupby( enumerate(a), lambda x: x[1]-x[0] ) :
  print (list(map(itemgetter(1), g)))

d = {x:a.count(x) for x in a}
print(d)
