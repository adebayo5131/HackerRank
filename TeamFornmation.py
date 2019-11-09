def Tf(arr):
    maxV = 0
    minV =0
    ntf =0
    sumV=0

    for i in arr:
        if arr[i] > 0:
            maxV +=1
            print(maxV)
        elif arr[i] < 0:
            minV += 1
            print(minV)
        else:
            sumV = len(arr)
            print(sumV)
            

arr=[ 4, 1, 3 ,-4, -3 ]

Tf(arr)
