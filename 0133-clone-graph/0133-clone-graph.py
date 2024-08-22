"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.hashmap = defaultdict(Node)
    def cloneGraph(self, node):
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
        
        
        
    