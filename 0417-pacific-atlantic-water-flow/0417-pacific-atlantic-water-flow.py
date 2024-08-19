# Breath first search solution
class Solution(object):
    def __init__(self):
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        self.pVisited = []
        self.aVisited = []
        self.pQueue = deque()
        self.aQueue = deque()
        
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #1. Take care of the empty matrix 
        if not heights or not heights[0]:
            return []
        
        #2. Determine the lengths of the matrix 
        rows = len(heights)
        cols = len(heights[0])
        
        self.pVisited = [[False for _ in range(cols)] for _ in range(rows)]
        self.aVisited = [[False for _ in range(cols)] for _ in range(rows)]
        
        
        #3. horizontal
        for i in range(0,cols,1):
            self.pQueue.append((0,i))
            self.aQueue.append((rows-1,i))
            self.pVisited[0][i] = True
            self.aVisited[rows-1][i] = True
        
        #4. vertical
        for j in range(0, rows, 1):
            self.pQueue.append((j,0))
            self.aQueue.append((j, cols-1))
            self.pVisited[j][0]= True
            self.aVisited[j][cols-1] = True
        
        #5. Complete the breath first search 
        self.BFS(heights, self.pQueue, self.pVisited)
        self.BFS(heights, self.aQueue, self.aVisited)
        res = []
        for r in range(rows):
            for c in range(cols):
                if self.pVisited[r][c] and self.aVisited[r][c]:
                    res.append([r,c])
        return res
                    
    
    
    def BFS(self, heights, queue, visited):
        #1. Define the step variable 
      
        while(queue):
            row,col = queue.popleft()
            for direction in self.directions:
                newRow = row+ direction[0]
                newCol = col+direction[1]
                
                if 0<=newRow<len(heights) and 0<=newCol<len(heights[0]):
                    if not visited[newRow][newCol] and heights[newRow][newCol] >= heights[row][col]:
                        visited[newRow][newCol] = True
                        queue.append((newRow, newCol))
                    
                
            
        
        
        
        