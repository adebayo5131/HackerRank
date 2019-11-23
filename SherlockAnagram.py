def sherlockAndAnagrams(s): 
      
    # Returns total number of anagram 
    # substrings in s 
    legnthOfString = len(s) 
    
    #frequency dictionary
    Dictionary = dict() 
      
    # loop for length of substring 
    for i in range(legnthOfString ): 
        currentWord = '' 
        for j in range(i, legnthOfString ): 
            currentWord = ''.join(sorted(currentWord + s[j])) 
            Dictionary[currentWord] =  Dictionary.get(currentWord, 0) 
              
            # increase count corresponding 
            # to this dict array 
            Dictionary[currentWord] += 1
  
    numberOfanagram = 0
      
    # loop over all different dictionary  
    # items and aggregate substring count 
    for k, v in Dictionary.items(): 
        numberOfanagram  += (v*(v-1))//2
    return numberOfanagram  
  
# Driver Code 
s = "xyyx"
print(sherlockAndAnagrams(s)) 
