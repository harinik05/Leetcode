class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxValue = 0
        
        left = 0
        right = len(height)-1
        
        
        while left<=right:
            currentArea = min(height[left], height[right]) *(right-left)
            maxValue = max(currentArea, maxValue)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        
        return maxValue
        
        