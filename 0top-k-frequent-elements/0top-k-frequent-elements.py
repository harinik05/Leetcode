class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        outputArr = []
        
        #1. Put everything in a hashmap 
        for i,number in enumerate(nums):
            hashmap[number]+=1
            
        # other option -> use Counter(nums) for keeping frequency of hashmap elements
        
        #2. Put it into a min heap 
        maxHeap = [(-value, key) for key,value in hashmap.items()]
        
        #3. Heapify
        heapq.heapify(maxHeap)
        counter = 0
        
        #4. for loop 
        for _ in range(k):
            outputArr.append(heapq.heappop(maxHeap)[1])
        
        return outputArr