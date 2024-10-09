from collections import defaultdict

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        visited = [0]*len(flowerbed)
        #1. For loop for every element in the flowerbed so far
        for i in range(len(flowerbed)):
            #a. put everything in the hashmap 
            
            
            #b. if the val is 1 then set itself and its adjacenceis 
            if flowerbed[i] == 1:
                visited[i] = 1
                
                #c. check if the i+1 is exceeding 
                if i+1<=len(flowerbed)-1:
                    visited[i+1] = 1
                
                if i-1>=0:
                    visited[i-1] = 1
           
            
            
        #2. for loop for every element that im adding 
        for i in range(len(flowerbed)):
            if n==0:
                break
            if visited[i] == 0 and flowerbed[i]==0:
                visited[i] = 1
                
                #c. check if the i+1 is exceeding 
                if i+1<=len(flowerbed)-1:
                    visited[i+1] = 1
                
                if i-1>=0:
                    visited[i-1] = 1
                n-=1
            
        #3. return the value we dont need rn 
        return n==0
            
            
            