def dDiff(arr):
    left = 0
    right = 0
    length = len(a[2])
    total = 0

    for i in range (length):
        left += arr[i][i]
        right += arr[i][length -i -1]
        
    total = left-right
    return abs(total)


a = [[11,2,4],[4,3,6],[10,8,-12]]

print(dDiff(a))
        
