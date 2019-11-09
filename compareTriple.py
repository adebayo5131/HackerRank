def compareTriplets(a, b):

    ap = 0
    bp = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            ap+=1
        
        elif a[i] < b[i]:
            bp +=1
        
        else:
            a[i] == a[i]
    return (ap,bp)

a = [1,2,8,7]
b = [1,5,2,1]
print(compareTriplets(a,b))
