class Solution:
    #1. Helper function to find the sum 
    def findSum(self,number):
        sNum = str(number)
        total = 0
        for char in sNum:
            total+=(int(char)**2)
        return total
        
    def isHappy(self, n: int) -> bool:
        #1. Total sum 
        totalSum =n
        setOfSums = set()
        while totalSum!=1 and totalSum not in setOfSums:
            setOfSums.add(totalSum)
            totalSum = self.findSum(totalSum)
            
        
        return totalSum==1
        
        