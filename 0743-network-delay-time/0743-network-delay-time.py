import heapq
# Dijstra's Algorithm

# Min heap ==> weight, node
# adjacency List -> node -> [(node, weight),...]

class Solution:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.minHeap = []
        self.visitedSet = defaultdict(int)
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #1. Create the adjacency list for this problem 
        for time in times:
            # Initialize everything in here
            ui, vi, wi  = time 
            # Put in adjacency list 
            self.adjacencyList[ui].append((vi, wi))
        
        #2. Initialize the min heap 
        #3. Call the BFS function 
        return self.dijstra(n,k)
        
    def dijstra(self, n,k):
        #1. Initialize the Min Heap 
        minTime = 0
        heapq.heappush(self.minHeap, (0, k))
        
        #2. While min heap 
        while self.minHeap:
            #a. Pop the first element 
            poppedElement = heapq.heappop(self.minHeap)
            time, node = poppedElement
            
            if self.visitedSet[node] != 1:
                # Mark as visited here once you unpacked
                self.visitedSet[node] = 1
                minTime = time
                #b. Go through all the neighbors 
                for neighbors in self.adjacencyList[node]:
                    v1,w1 = neighbors
                    if self.visitedSet[v1] == 0:
                        heapq.heappush(self.minHeap, (w1+ time, v1))
        
        #3. Check if all nodes were reached
        if len(self.visitedSet) == n:
            return minTime
        return -1
        
        
                    
                
        
        
        
        