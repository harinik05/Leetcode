class Solution(object):
    def __init__(self):
        self.visited = []
        self.queue = deque()
        
    def findCircleNum(self, isConnected):
        self.visited = [0]*len(isConnected)
        counter = 0
        for i in range(len(isConnected)):
            if self.visited[i] == 0:
                counter+=1
                self.bfs(i, isConnected)
        return counter
    
    def bfs(self, i, isConnected):
        #1. Put the first element in the queue 
        self.queue.append(i)
        self.visited[i] = 1
        
        #2. While queue exists 
        while self.queue:
            #a. Retrieve the first element 
            firstElem = self.queue.popleft()
            
            #b. Go through the neighbors 
            for k in range(len(isConnected[firstElem])):
                if isConnected[firstElem][k] == 1 and self.visited[k]==0:
                    self.queue.append(k)
                    self.visited[k] = 1
        
                    
    
    def findCircleNumDFS(self, isConnected):
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
                    
        