import math
cube = lambda x: x*x**2 # complete the lambda function

def fibonacci(nr):
    # return a list of fibonacci numbers
    sequence = [0, 1]

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, nr)))

    return sequence[:nr]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
