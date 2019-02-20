def fruits(l,total):
    return fruits(l,total)

if __name__ == '__main__':
    l = {'Apple':160,'Banana':120,'Mango':110,'Peach':100,'Grapes':130}
    d = []
    total = ''

    for i ,v  in l.items():
        inp = input("How many %s did you buy : " % i)
        #d.append(inp)
        total = int(inp) * v
        d.append("Price for %s : %s * %s = %s " % (i,inp,v,total))
        #return (l,total)
    print("=================================")
    [print(x) for x in d]


