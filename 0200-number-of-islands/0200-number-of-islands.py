class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.DFS(grid, i, j)
                    islandCount+=1
        return islandCount
                    
    
    def DFS(self, grid, r, c):
        #1. Check all necessary conditions
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return 
        if grid[r][c] == "0":
            return 
        #2. Process cell (mark as visited)
        grid[r][c] = "0"
        #3. Call DFS as needed
        self.DFS(grid, r+1, c)
        self.DFS(grid, r-1, c)
        self.DFS(grid, r, c+1)
        self.DFS(grid, r, c-1)
        
        