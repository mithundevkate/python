

n = input().split()
n1 = input()

n1 = n1.replace('x',n[0])
print(eval(n1))

if eval(n1)== int(n[1]) :
    print(True)
else:
    print(False)
