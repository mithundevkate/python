import numpy
n =list(map(float,input().split()))

my_array = numpy.array(n)

print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))
