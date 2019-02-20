'''
swapping program for first two letters of given strings:

iput == abc
input2 = xyz

output == 'xyc abz'
'''

def str1(abc,xyz):
    abc = [x for x in abc]
    xyz = [x for x in xyz]
    abc[0:2] , xyz [0:2] = xyz [0:2] ,abc[0:2]
    x= print("'%s %s'" % ("".join(abc),"".join(xyz)))
    return(x)
a = input("First string:\n")
b = input("Second string:\n")
str1(a,b)
