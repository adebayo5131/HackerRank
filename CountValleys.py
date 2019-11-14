def countingValleys(n, s):
    starts = 0
    valley =0
    for i in range(n):
        if s[i].startswith('U'):
            starts+=1
            if starts==0:
                valley +=1
        else:
            starts-=1
    return valley

s=['D','D','U','U','D','D','U','D','U','U','U','D']
n=len(s)
print(countingValleys(n,s))
