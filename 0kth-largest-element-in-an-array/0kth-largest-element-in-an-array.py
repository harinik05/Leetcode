class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #1. Create the heap 
        minHeap = []
        
        #2. Populate the heap 
        for i in range(len(nums)):
            #a. Push the element into the heap
            heapq.heappush(minHeap, nums[i])
            
            #b. while its less than k 
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return minHeap[0]
            
    def findKthLargest_MAXHEAP(self, nums: List[int], k: int) -> int:
        #1. Heapify this list 
        maxHeap = [-nums[i] for i in range(len(nums))]
        heapq.heapify(maxHeap)
        
        #2. For loop 
        counter = 0
        finalResult = 0
        for _ in range(k):
            finalResult = maxHeap[0] * -1
            heapq.heappop(maxHeap)
       
        return finalResult
            
            
            
            
            