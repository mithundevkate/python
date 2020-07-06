n ='Sorting1234'
nllower = []
nlupper = []
nlodd =[]
nleven = []
n = list(n)
for i in n:
    print (i)
    try:
        if i.islower() == True :
            nllower.append(i)
        elif i.isupper() == True:
            nlupper.append(i)

        elif int(i) % 2 != 0:
            nlodd.append(i)
        elif int(i) % 2 == 0:
            nleven.append(i)
        else:
            pass
    except ValueError:
        pass
print("".join(sorted(nllower)+sorted(nlupper)+sorted(nlodd)+sorted((nleven))))
#print("".join(nl))
