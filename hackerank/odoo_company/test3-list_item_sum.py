'''Write a function that takes a list of strings and returns the sum of the list items that represent an integer (skipping the other items)'''

def str_lis(stringInput):
    sum_int = sum([i for i in stringInput if type(i) == int])
    print(sum_int)

str_lis(['a','b','3',3,4,4])
