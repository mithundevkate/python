n,n1 = int(input()),int(input())
l = []
for i in range(n):

    l.append(max(map(int,input().split())))


print(sum([i**2 for i in l])%n1)
print(l)


