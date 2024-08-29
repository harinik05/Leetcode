# variant of kadanes DP algorithm 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #1. Initialize the values 
        currentMin = float('inf') #set the min to max
        maxProfit = 0 
        
        #2. For loop 
        for price in prices:
            #a. determine the min price 
            currentMin = min(currentMin, price)
            
            #b. Calculate the profit by minimizing the min 
            currentProfit = price-currentMin
            
            #c. determine the max profit 
            maxProfit = max(currentProfit, maxProfit)
        
        return maxProfit 
        
        