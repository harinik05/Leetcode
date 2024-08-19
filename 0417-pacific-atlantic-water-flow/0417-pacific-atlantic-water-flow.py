class Solution(object):
    
    def __init__(self):
        self.aMatrix = []
        self.pMatrix = []
        
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []
        
        self.aMatrix=[[False for _ in range(0,len(heights[0]))] for _ in range(len(heights))]
        self.pMatrix=[[False for _ in range(0,len(heights[0]))] for _ in range(len(heights))]
        rowCount = len(heights)
        colCount = len(heights[0])
        
        
        #horizontal
        for horizontalStuff in range(colCount):
            self.DFS(heights,0,horizontalStuff, -float('inf'), self.pMatrix )
            self.DFS(heights, rowCount-1, horizontalStuff, -float('inf'), self.aMatrix)
            
        #vertical
        for verticalStuff in range(rowCount):
            self.DFS(heights, verticalStuff, 0, -float('inf'), self.pMatrix)
            self.DFS(heights, verticalStuff, colCount-1, -float('inf'), self.aMatrix)
        
        #dfs/bfs stuff (done)
        
        output = []
        #find the overlap
        for i in range(rowCount):
            for j in range(colCount):
                if self.pMatrix[i][j] and self.aMatrix[i][j]:
                    output.append([i,j])
        return output
        
    def DFS(self, heights, r,c,previousValue, bMatrix):
        #1. Check the necessary conditions
        if(not heights):
            return 
        if not 0<=r<len(heights) or not 0<=c<len(heights[0]):
            return 
        if bMatrix[r][c] == True:
            return 
        if previousValue>heights[r][c]:
            return
        
        #2. Process the cell
        bMatrix[r][c] = True
        
        #3. Call the DFS as needed
        self.DFS(heights, r+1, c, heights[r][c], bMatrix)
        self.DFS(heights, r-1, c, heights[r][c], bMatrix)
        self.DFS(heights, r, c+1, heights[r][c], bMatrix)
        self.DFS(heights, r, c-1, heights[r][c], bMatrix)
        