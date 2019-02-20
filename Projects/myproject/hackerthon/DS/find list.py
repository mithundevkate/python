'''
You are given two lists (each element is an integer that is less than 10), and you are asked to create a third list that represents a sum of these two. For example,
list1: 1 -> 2 -> 3
list2: 7 -> 7
123 + 77 = 200 ----> list3: 2 -> 0 -> 0
'''

l1 = [1,2,3,8,9]
l2 = [7,7]

l3 = [int(i) for i in str (int("".join(str(x) for x in l1))+int("".join(str(x) for x in l2)))]
print(l3)
