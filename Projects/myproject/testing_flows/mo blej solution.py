def str1(abc,xyz):
    a = abc[0]
    abc[0]=xyz[0]
    xyz[0]=a
    #xyz = [x for x in xyz]
    #abc[0:2] , xyz [0:2] = xyz [0:2] ,abc[0:2]
    str =abc+""+xyz
    #x= print("'%s %s'" % ("".join(abc),"".join(xyz)))
    return(str)
a = input("First string:\n")
b = input("Second string:\n")
str= str1(a,b)
print(str)
