#DFS
class Solution:
    def __init__(self):
        self.area = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.area = 0
                self.DFS(grid, i, j)
                maxArea = max(self.area, maxArea)
        return maxArea
    
    
    def DFS(self, grid, r, c):
       
        #1. Check the necessary conditions
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
            return 
        if grid[r][c] == 0:
            return 
        
        #2. Process the cell
        grid[r][c] =0
        self.area +=1
        
        #3. Call the DFS as needed
        self.DFS(grid, r+1,c)
        self.DFS(grid, r-1, c)
        self.DFS(grid,r,c+1)
        self.DFS(grid, r, c-1)
        
        
        
        
        