def birthdayCakeCandles(ar):
 
    dic= {}
    highest =0
    for i in  (ar):
        dic.setdefault(i,0)
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    highest = max(dic.values())
    return highest

ar=[3,2,1,3]
result = birthdayCakeCandles(ar)
print(result)
