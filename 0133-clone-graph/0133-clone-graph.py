"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.hashmap = {}
        self.queue = deque();
    def cloneGraph(self, node):
        if not node:
            return None
        return self.BFSFunction(node)
    
    def BFSFunction(self, node):
        #1. Initialize the queue with some item 
        self.queue.append(node)
        createClone = Node(node.val, [])
        self.hashmap[node] = createClone
        
        #2. While the queue is not empty 
        while self.queue:
            current = self.queue.popleft()
            
            for neighbors in current.neighbors:
                if neighbors not in self.hashmap:
                    neighborClone = Node(neighbors.val, [])
                    self.hashmap[neighbors] = neighborClone
                    self.queue.append(neighbors)
                self.hashmap[current].neighbors.append(self.hashmap[neighbors])
                
        return self.hashmap[node] 
                    
         #3. Loop through all the directions (or neighbors)
        #4. Check the condition if yes add to the queue 
    def cloneGraphDFS(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return
        
        return self.DFSFunction(node)
        
    def DFSFunction(self, node):
        #1. Check all the necessary conditions
        if node in self.hashmap.keys():
            return self.hashmap[node]
        
        #2. Process the cell
        createdClone = Node(node.val, [])
        self.hashmap[node] = createdClone
            
        #3. Call the DFS function recursively 
        for neighbors in node.neighbors:
                createdClone.neighbors.append(self.DFSFunction(neighbors))
        
        return createdClone
        
        
        
    