from collections import deque

class Solution(object):
    def __init__(self):
        self.queue = deque()
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.islandCounter = 0
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Start BFS for a new island
                    area = self.BFS(grid, i, j)
                    self.islandCounter = max(self.islandCounter, area)
                    
                    
        return self.islandCounter
        
    def BFS(self, grid, startRow, startCol):
        self.queue.append((startRow, startCol))
        grid[startRow][startCol] = 0  # Mark as visited
        area = 1
        
        while self.queue:
            row, col = self.queue.popleft()
            
            for direction in self.directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                
                if (0 <= newRow < len(grid) and 
                    0 <= newCol < len(grid[0]) and 
                    grid[newRow][newCol] == 1):
                    
                    grid[newRow][newCol] = 0  # Mark as visited
                    area+=1
                    self.queue.append((newRow, newCol))
        return area