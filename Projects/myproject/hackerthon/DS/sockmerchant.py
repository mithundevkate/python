def sockMerchant(n, ar):

    # progrm to fin socks pairs
    d={}

    for i in ar:
        if ar.count(i) != 1 and ar.count(i) % 2 == 0:
            d[i] = int((ar.count(i))/2)

        elif ar.count(i) != 1 and ar.count(i)%2 != 0:
            d[i] = int((ar.count(i))/2)

        else:
            pass
    print(sum(d.values()))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar =[]

    for i in range(n):
        arr_item = int(input().strip())
        ar.append(arr_item)

    result = sockMerchant(n, ar)
