class Solution:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.visitedSet = defaultdict(bool)
    
    def dfs(self, inputNode):
        #a. Check the ncessaruy conditions 
        if self.visitedSet.get(inputNode) == True:
            return 
        
        #b. Process the cell
        self.visitedSet[inputNode] = True
        
        #c. DFS of all the neighbors 
        for neighbor in self.adjacencyList[inputNode]:
            self.dfs(neighbor)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #1. Initialize the adjacency list 
        for edge1, edge2 in edges:
            self.adjacencyList[edge1].append(edge2)
            self.adjacencyList[edge2].append(edge1)
        
       
        counter = 0
        #2. Call the loop 
        for i in range(n):
            if self.visitedSet.get(i)!=True:
                counter+=1
            self.dfs(i)
        
        return counter
            
                
                
        
        
        
        