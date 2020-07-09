'''
Test 4: Any language (1/20)
Write a recursive version of the previous function (or an iterative version if you have already done a recursive version).'''


def str_lis(stringInput):
    sum_int = sum([i for i in stringInput[1:] if type(i) == int])
    print(sum_int)

str_lis(['a','b','3',3,4,4])
