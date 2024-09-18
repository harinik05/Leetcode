class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Implement this using two pointer method as its sorted out already
        
        #1. Initialize two pointers in opposite ends (finding target - so performing a search)
        loPtr = 0
        hiPtr = len(numbers)-1
        
        #2. While lo < hi
        while loPtr< hiPtr:
            #1. Check the sum 
            totalSum = numbers[loPtr] + numbers[hiPtr]
            
            #2. Compare with target
            if totalSum < target:
                loPtr+=1
            elif totalSum > target:
                hiPtr-=1
            else:
                return [loPtr+1, hiPtr+1]
        
        return [-1, -1]
        