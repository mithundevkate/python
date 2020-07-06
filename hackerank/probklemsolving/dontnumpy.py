import numpy
A = [ 1, 2 ]
B = [ 3, 4 ]
result = numpy.dot( A,B)

result1= numpy.cross(A,B)

print(result)
print(result1)

x = 2
y = 2
n = 2
z=2
print( [ [ i, j ,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j +k) != n )])

x = [2,3,6,6,5]#[57,57,-57,57]
li = sorted(set(x) , reverse=True)
print(li)
print(li[1])

nums = tuple(map(int, input().split()))

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))

