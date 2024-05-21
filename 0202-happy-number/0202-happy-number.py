class Solution:
    def isHappy(self, n: int) -> bool:
        
        #1. Initialize the set for storing all the values 
        sSet = set()
        flag = True
        
        #2. While loop as long as the flag is true
        while flag == True:
            #1. Determine the sum of squares
            totalSum = 0
            nStr = str(n)
            
            for characters in nStr:
                totalSum += (int(characters)**2)
            
            #2. Place the sum into the set if possible
            if totalSum in sSet:
                flag = False
            else:
                sSet.add(totalSum)
                
            #3. check if the sum is 1
            if totalSum == 1:
                return True
            n = totalSum
        return False
                
        