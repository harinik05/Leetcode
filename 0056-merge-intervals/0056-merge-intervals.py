class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #1. Sort array by the first number
        intervals.sort(key=lambda x:x[0])
        mergedIntervals = []
        #2. For loop
        for interval in intervals:
            #a. Interval doesnt overlap with the previous 
            if not mergedIntervals or mergedIntervals[-1][1]<interval[0]:
                mergedIntervals.append(interval)
            
            #b. there is an overlap
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1])
                
        return mergedIntervals
            
            
            