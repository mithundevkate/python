def collatz(no):

    if no % 2 ==0:
        print(no//2)
        return no//2
    else:
        print(3*(no) +1)
        return 3*(no) +1
        #collatz(number)

    #return (number)

if __name__ == '__main__':

    number = input("enter no:\n")

    while(number != 1):
        number = collatz(int(number))
    #x = collatz(number)
    #print(x)
    #for i in range(1,number+1):

     #   collatz(number)


