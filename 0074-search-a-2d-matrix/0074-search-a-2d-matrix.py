class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Lets redo this question with binary search 
        fullArray = []
        for rows in range(len(matrix)):
            for cols in range(len(matrix[0])):
                fullArray.append(matrix[rows][cols])
        
        
        #binary search 
        lo = 0
        hi = len(fullArray)-1
        
        
        while lo<=hi:
            pivot = (lo+hi)//2
            if fullArray[pivot]<target:
                lo+=1
            elif fullArray[pivot]>target:
                hi-=1
            else:
                return True
        return False
            