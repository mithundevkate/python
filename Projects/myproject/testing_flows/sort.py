def customSort(arr):
    # Write your code here
    # sort number ccording to index count
    #inp = input("Enter value of array:\n \n")
    #inp = [2,3,3,1,1,4,1,4,4,4,0]
    d = []
    z = []

    for i in arr:
        if i in arr:
            if arr.count(i) != 1:

                d.append(i)
            else:
                z.append(i)
    z.extend(d)
    #print (d)
    #print (z)
    p = (sorted(z,key=z.count))


    [print(x) for x in p]


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    #print (arr)
    customSort(arr)
