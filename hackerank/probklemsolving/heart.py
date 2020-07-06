import math

c='♥'
width = 40

'''print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))'''

num = int(input("enter the number:"))
msg = input("Enter any msg:")
l = len(msg)
n = num//2
for i in range(n):
    print(" "*(n-i-1) + "* "*(i+1) ,end="" )
    if num % 2 == 0:
        for j in range(2*(n-i-1)):
            print(" ",end ="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ",end ="")
    for j in range(i+1):
         print("* ",end="")
    print()
if num%2==0:
    if l%2==0:
        print("* "*((num-1)//2) + " ".join(msg) + " *"*((num-1)//2) )
    else:
        print("* "*((num-1)//2) + " ".join(msg) + " *"*(((num-1)//2)+1) )
else:
    if l%2==0:
        print("* "*((num-1)//2) + " ".join(msg) + " *"*(((num-1)//2)+1) )
    else:
        print("* "*((num-1)//2) + " ".join(msg) + " *"*(((num-1)//2)) )
for i in range(num,0,-1):
    print(" "*(num-i)  +  " *"*(i))

