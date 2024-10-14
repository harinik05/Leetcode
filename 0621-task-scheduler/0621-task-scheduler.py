from collections import defaultdict
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        #1. Initialize the required variables for this problem 
        maxHeap = []
        queue = deque() # FIFO
        time = 0

        #2. Create a frequency table for the max heap from this particular scenario 
        frequencyMap = defaultdict(int)

        for letter in tasks:
            frequencyMap[letter]+=1
        
        for key,value in frequencyMap.items():
            heapq.heappush(maxHeap,[-value,key])

        #heapq.heapify(maxHeap)

        #3. while heap and pop things out 
        while maxHeap or queue:
            
            #b. increment thr time 
            time+=1
            if maxHeap: 
                #a. Pop out the largest element 
                largestValue = heapq.heappop(maxHeap)
                largestValue[0]+=1

                #c. add the idle time here and keep track of it
                if largestValue[0]!=0:
                    queue.append([largestValue,time+n])
            
            #d. add values to the maxheap
            if queue and time == queue[0][1]:
                poppedValue = queue.popleft()
                heapq.heappush(maxHeap,poppedValue[0])
        
        return time
