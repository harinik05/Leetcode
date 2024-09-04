from collections import deque
class Solution(object):
    def __init__(self):
        self.ROWS = 0
        self.COLS = 0
        self.queue = deque()
        self.fresh = 0
        self.minutes = 0
        self.gridcpy = []
        self.directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.gridcpy = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        #1. Iterate through all the cells in the grid 
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == 1:
                    self.fresh+=1 
                elif grid[r][c] == 2:
                    self.queue.append((r,c))
        
        self.bfs()
        
        #2. Return the minutes 
        return self.minutes if self.fresh==0 else -1
    
    def bfs(self):
        #1. Initialize things in the queue 
        # DONE
        
        #2. Whle queue 
        while self.queue and self.fresh>0:
            # Increment the time at start of each level and loop through all the levels
            self.minutes+=1 
            for _ in range(len(self.queue)):
            
                cRow, cCol = self.queue.popleft()

                # loop through all the directions
                for direction in self.directions:
                    iRow, iCol = direction
                    row = cRow + iRow
                    col = cCol + iCol

                    if 0<=row<self.ROWS and 0<=col<self.COLS:
                        if self.gridcpy[row][col] == 1:
                            self.fresh-=1
                            self.gridcpy[row][col] = 2
                            self.queue.append((row, col))
        
    
                    
        