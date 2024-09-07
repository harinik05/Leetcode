from collections import defaultdict
from collections import deque
# Lets implement some topological ordering logic into this for cycle detection 
class Solution(object):
    # Constructor 
    def __init__(self):
        # Initialize the variables 
        self.visitedHashmap = defaultdict(int) # have three states 0: not visited, 1: processing, 2: fully finished processing
        self.adjacencyList = defaultdict(list)
        self.NUMBER = 0
        self.queue = deque()
        self.indegreeArray = []
    
    def canFinish(self, numCourses, prerequisites):
        self.NUMBER = numCourses
        #1. Create an indegree array
        self.indegreeArray = [0] * self.NUMBER
        
        
        #1. Create adjacency list for this problem
        for pair in prerequisites:
            self.adjacencyList[pair[0]].append(pair[1])
            self.indegreeArray[pair[1]] +=1 
        
        #2. Queue with incoming edges (put anything that doesnt have dependencies)
        for i in range(self.NUMBER):
            if self.indegreeArray[i] == 0:
                self.queue.append(i)
        
        #3. while queue 
        nodesSoFar = 0
        while self.queue:
            # pop the first node 
            poppedNode = self.queue.popleft()
            nodesSoFar+=1
            
            # go through all the neighbors in popped node 
            for neighbors in self.adjacencyList[poppedNode]:
                self.indegreeArray[neighbors]-=1
                
                # check if the neighbor is 0 then append to the queue 
                if self.indegreeArray[neighbors] == 0:
                    self.queue.append(neighbors)
        
        return nodesSoFar == self.NUMBER
    
    
        
        
    def canFinishDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #1. Create a adjacency list for this problem 
        for pair in prerequisites:
            self.adjacencyList[pair[0]].append(pair[1])
        
        #2. Create a visited hashmap 
        self.NUMBER = numCourses
        for i in range(self.NUMBER):
            if self.visitedHashmap[i] == 0:
                #b. do the dfs of this particular element 
                output = self.dfs(i, prerequisites)
                
                if output== False:
                    return False
        
        return True
        
        
    #3. Define your DFS function 
    def dfs(self, i, prerequisites):
        #a. check all the conditions 
        if self.visitedHashmap[i]==1:
            return False
        if self.visitedHashmap[i]== 2:
            return True
      
        if not 0<=i<self.NUMBER:
            return False

        #b. process the cell 
        self.visitedHashmap[i] = 1
        

        #c. go through all neighbors and do the recursion 
        for neighbors in self.adjacencyList[i]:
            output = self.dfs(neighbors, prerequisites)
            
            if output == False:
                return False
        
        #d. processed set the status 
        self.visitedHashmap[i] = 2
        
        return True
            
            
            