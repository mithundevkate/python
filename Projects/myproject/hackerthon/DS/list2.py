'''
You are given a list of n elements (integers with values between 0 and 99 that can appear more than once in the list), and you should find the element that appears most often, and you are allowed to go trough the list just once
'''
import collections

a = [1,1,1,2,2,2,2,2,2,2,4,5,6,7,4,4,6,7,4,67,66]

aa = collections.Counter(a).most_common(1)[0]
print(list(aa)[0])
