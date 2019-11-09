def miniMaxSum(arr):
    sum=0
    #sum up all numbers in the array
    for s in range (len(arr)):
        sum+=arr[s]
    #use max fun and min function to find the smallest and largest values in the array
    #subtract the smallest from array to get max sum
    #subtract the largest from arry to get min sum
    print(sum-max(arr),sum-min(arr))


arr = [8974, 69, 2, 221, 7]
miniMaxSum(arr)
