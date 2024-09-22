class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Find the closest values -> smallest values means min heap 
        #1. Create a hashmap and store all the elements to it 
        hashmap = defaultdict(int)
        minHeap = []
        for coordinates in points:
            #a. Calculate the distance
            x,y= coordinates
            
            #b. distance
            dist = math.sqrt(x**2 + y**2)
            
            # put into the hashmap 
            minHeap.append((dist, (x,y)))
            
        #2. Create the min heap 
        heapq.heapify(minHeap)
        output = []
        #3. Loop through k elements 
        for _ in range(k):
            #a. Smallest values 
            #smallestValue = heapq.heappoll(minHeap)[1]
            smallestValue = heapq.heappop(minHeap)
            
            #b. and put in array 
            output.append(list(smallestValue)[1])
            
        
        return output
        
  