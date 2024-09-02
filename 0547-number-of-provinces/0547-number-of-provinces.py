class Solution(object):
    def __init__(self):
        self.visited = []
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        m = len(isConnected)
        n = len(isConnected[0])
        self.visited = [0] * m
        counter = 0
        # for loop for everything and do a DFS 
        for i in range(m):
                if self.visited[i] == 0:
                    counter+=1
                    self.dfs(i, isConnected)
        
        return counter
    
    def dfs(self, i, isConnected):
        # Check all the necessary condition 
        if self.visited[i] == 1:
            return 
        
        # Process the current cell 
        self.visited[i] = 1
        
        # Call the DFS function as needed
        for k in range(len(isConnected[i])):
            if(isConnected[i][k] == 1):
                self.dfs(k, isConnected)
                    
        