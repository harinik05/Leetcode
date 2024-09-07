from collections import defaultdict

class Solution(object):
    # Constructor 
    def __init__(self):
        # Initialize the variables 
        self.visitedHashmap = defaultdict(int) # have three states 0: not visited, 1: processing, 2: fully finished processing
        self.adjacencyList = defaultdict(list)
        self.NUMBER = 0
        
    def canFinish(self, numCourses, prerequisites):
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
            
            
            