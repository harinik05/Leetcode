class Solution(object):
    def __init__(self):
        self.NUMBER = 0
        self.queue = deque()
        self.indegreeArr = []
        self.adjacencyList = defaultdict(list)
        self.topoArr = []
        self.nodesSoFar = 0
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #1. Initialize your indegree array 
        self.NUMBER = numCourses
        self.indegreeArr = [0] * self.NUMBER
        
        #2. Determine the adjacency list 
        for number in prerequisites:
            self.adjacencyList[number[1]].append(number[0])
            self.indegreeArr[number[0]] +=1
        
        #3. Initialize the topological sort array 
        #a. Put the first element into the queue 
        for i in range(self.NUMBER):
            if self.indegreeArr[i] == 0:
                self.queue.append(i)
        
        #b. while queue 
        while self.queue:
            # c. pop the first element 
            firstElem = self.queue.popleft()
            self.nodesSoFar+=1
            
            self.topoArr.append(firstElem)
            
            
            #d. Go through all the neighbors 
            for neighbors in self.adjacencyList[firstElem]:
                self.indegreeArr[neighbors]-=1
                if self.indegreeArr[neighbors] == 0:
                    self.queue.append(neighbors)
        if self.nodesSoFar != self.NUMBER:
            return []
        
        return self.topoArr
        