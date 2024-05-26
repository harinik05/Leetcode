from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. Put everything from the nums array on the hashmap 
        hashmap = defaultdict(int)
        
        #2. For loop the whole nums array
        for i in range(len(nums)):
            #a. put it in the hashmap
            hashmap[nums[i]]+=1
        
        #3. Sort the hashmap by the values
        sorted_values = {k:v for k,v in sorted(hashmap.items(), key=lambda item:item[1], reverse = True)}
        
        #4. choose the top k elements from here 
        outputArr = []
        counter = 0
        for key,items in sorted_values.items():
            if counter == k:
                break
            outputArr.append(key)
            counter+=1
        return outputArr
            
            
        
        
            
            