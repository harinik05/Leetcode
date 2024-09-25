class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #1. Heapify the original array to be a max heap 
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        #2. while maxHeap 
        while len(maxHeap)>1:
            #a. Pop the max element 
            largest = heapq.heappop(maxHeap)
            smallest = heapq.heappop(maxHeap)
            
            #b. push the element 
            temp = abs(largest)-abs(smallest)
            heapq.heappush(maxHeap, temp*-1)
        
        return -maxHeap[0]
        
        