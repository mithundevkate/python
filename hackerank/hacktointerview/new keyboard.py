keys = ['<','>','*','#']
str = 'HE*<LL>O'
lis =list(str)

for index, i in enumerate(range(len(lis))):

    count = 0
    #print(lis[i] ,i )
    if  '*' in lis:
       # print(lis[i])
        #print(i)
        lis.remove('*')
        lis.pop(index+1)

       # print(i)
        #lis.remove('*')
    if '<' in lis:
        lis.remove('<')
        lis[index] = lis[i]
        count = count+1
    if '>' in lis:
        lis.remove('>')
        lis[-1] = lis[i]

    #lis.append(i)
print("".join(lis))
