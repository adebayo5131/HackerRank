def makeAnagram(a, b):
    #Create an array with lenght of 26 representing the english alphabets
    arrOfwords= [0] * 26
    #Store each elements in string a and b in the array 
    #Keep count of each element denoting it with 1 when stored
    for i in a:
        #ord() gives the Unicode of the character
        # ord(h)-ord(a) = 7 
        # h is the 8 alphabet and 7 
        #which is the position of h in the arr starting from 0
        arrOfwords[ord(i) - ord('a')] += 1
    for i in b: 
        arrOfwords[ord(i) - ord('a')] -= 1

        #Take the abs of each element in the array and sum them
    return sum(map(abs, arrOfwords))
a = 'heb'
b = 'hea'
print(makeAnagram(a,b))
