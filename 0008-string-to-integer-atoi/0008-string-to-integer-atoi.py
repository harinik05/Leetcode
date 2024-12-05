class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #1. Ignore the whitespace 
        noWS = s.lstrip()
        if not noWS:
            return 0
        #2. Determine the sign by checking the next char
        i = 0
        sign = 1
        # Set up the sign and then break once this is done
        if noWS[i] == "+":
            sign = 1
            i+=1
        elif noWS[i] == "-":
            sign = -1
            i+=1
        
        #3. Conversion - read the integer skip zeros
        # you need to add 1 to i -> why? you need to go past the current index 
        
        result = 0
        for j in range(i,len(noWS),1):
    
            if not noWS[j].isdigit():
                break
            
            result = result*10 + int(noWS[j])
        
        
        finalResult = result * sign if -2**31 <= (result) <= 2**31 -1 else "FIX"
        if finalResult == "FIX" and sign == -1:
            finalResult = -2**31
        elif finalResult == "FIX" and sign == 1:
            finalResult = 2**31 -1
        
        return finalResult
        
        #4. Finally check if the range then round it 
        
        
        