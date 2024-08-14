from collections import defaultdict
import math 

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #1. create a hashmap 
        hm = defaultdict(list)
        distance = 0
        
        #2. loop through everything 
        for i in range(len(points)):
            #a. temp array 
            temp = points[i]
            
            #b. calculate the distance 
            distance = math.sqrt((temp[0]**2) + (temp[1]**2))
            
            #c. put everything in the hashmap
            hm[distance].append(temp)
            

        
    
        
        #3. sort the hashmap
        sorted_by_keys = sorted(hm.items())
        
        #4. pick the first k items 
        outputArr = []
        counter = 0
        for distanceCalculated, listOfPoints in sorted_by_keys:
            for point in listOfPoints:
                outputArr.append(point)
                counter+=1
                if counter==k:
                    break
            if counter == k:
                break
                
        
        return outputArr
            
            
            
        
