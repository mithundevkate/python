n = input().split()

l = []

for i in range(int(n[1])):
    l.append(list(map(float,input().split())))

x = list(zip(*l))
for i in x:
    print(sum(list(i))/int(n[1]))
