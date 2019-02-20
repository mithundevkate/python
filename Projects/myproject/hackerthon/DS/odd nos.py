def oddNumbers(l, r):
    for i in range(l,r+1):
        if (i%2) != 0:
            print (i)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)
