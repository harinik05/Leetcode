import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minHeap = []
        for number in self.nums:
            self.add(number)

    def add(self, val: int) -> int:
        
        #1. push the element in 
        heapq.heappush(self.minHeap,val)
            
        #2. check the length of minHeap (should be in descending order)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
       
        return self.minHeap[0]
            
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)