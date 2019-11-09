def plusMinus(arr):
    positive = 0
    negative = 0
    neither = 0
    length = len(arr)

    for i in range(length):

        if arr[i] > 0:
            positive +=1
        elif arr[i] < 0:
            negative += 1
        else:
            neither+=1

    print(positive/length)
    print(negative/length)
    print(neither/length)


arr = [-4,3,-9,0,4,-1]
plusMinus(arr)
