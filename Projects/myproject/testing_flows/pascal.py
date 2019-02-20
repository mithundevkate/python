n = int(input("length \n\n"))
p =[0,1,0]
d = []
print("\n{:^60}".format(1))
for w in range(n):
    for a in range(len(p)-1):
        b=int(p[a])+int(p[a+1])
        d.append(str(b))
    if n==1 or w==0:
        pass
    else:
        d[0:0]='1'
        d[w+1:w+1] ='1'
    p=d
    print("\n{:^60}".format(''.join(d)))
    d=[]
