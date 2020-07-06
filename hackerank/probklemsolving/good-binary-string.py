s = '00100'
newl = list(s)
i = 3
sub = ['01','10','1']
z = list(map(''.join, zip(*[iter(newl)]*2)))
print(z)
count = ''
for i in s:
    newl[s.index(i)] = 1
    #print(s.index(i))
leap = False
year = 2000
if year % 4 == 0 and year % 100 == 0 :#and year % 400 ==0:

    if  year % 400 != 0:
        leap = False
        print(1)
    else:
        leap = True

elif year % 100 == 0 and year % 400 == 0:
    leap = True
elif year % 100 == 0 and year % 400 != 0:
    leap = False
    print(2)
elif year % 4 == 0:
    leap = True
else:
    leap = False
    print(3)
print(leap)

n = 3
x = [i for i in range(1,n+1)]
print(x)
print("".join((str (e) for e in x)))
