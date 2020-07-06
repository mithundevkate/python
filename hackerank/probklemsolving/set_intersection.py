a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
c = [i for i in (a.difference(b),b.difference(a))]
for i in c:
    for j in i:
        #print(j)
        pass
dic = {'ID':[1,2,3,4,5],'MARKS':[97,50,91,72,80]}

for i in dic['MARKS']:
    print(i)

print(sum(dic['MARKS'])/len(dic['MARKS']))


from collections import namedtuple

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())
