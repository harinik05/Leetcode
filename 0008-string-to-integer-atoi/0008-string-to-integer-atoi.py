'''
O(n) time complexity 
O(1) space complexity
'''
MAX_NUMBER = 2**31-1
MIN_NUMBER = -2**31
class Solution(object):
    
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #1. Ignore whitespaces first 
        #2. Determine the sign - if nothing or if its a number then its negative
        #3. Convert this to some int, stop at some non int tho 
        #4. Return the answer
        
        s_nows = s.lstrip()
        if s_nows=="":
            return 0
        i = 0
        sign = s_nows[i]
        negative = False
        if sign == "+":
            i+=1
        elif sign == "-":
            i+=1
            negative = True 
        
        finalResult = 0
        for j in range(i,len(s_nows)):
            if not s_nows[j].isdigit():
                break
            # final result - build this up
            finalResult = 10*finalResult + int(s_nows[j])
            
        number = -1 if negative else 1
        finalNumber = finalResult * number
        if finalNumber>MAX_NUMBER and number==1:
            return MAX_NUMBER
        
        elif finalNumber<MIN_NUMBER and number==-1:
            return MIN_NUMBER
        return finalNumber
                