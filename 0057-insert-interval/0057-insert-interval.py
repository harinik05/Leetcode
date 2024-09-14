class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        #1. Initialize the variables
        resultArr = []
        
        #2. Iterate thru the intervals 
        for i, interval in enumerate(intervals):
            #a. Check if the new interval is coming before 
            if newInterval[1] < interval[0]:
                resultArr.append(newInterval)
                return resultArr + intervals[i:]
            
            #b. no overlap -> newInterval[0] > interval[1]
            elif newInterval[0] > interval[1]:
                resultArr.append(interval)
                
            #c. overlapping interval
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        #3. append the new interval 
        resultArr.append(newInterval)
        return resultArr
                
        