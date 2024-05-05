class Solution:
    # Greedy Solution
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Lacks optimal substructure, can't build from child costs
        Time Complexity: O(nlgn)
        Space Complexity: O(1)
        '''
        
        # 1. Sort the array
        people.sort()
        
        #2. Initialize two pointers
        start = 0
        end = len(people)-1
        counter = 0
        #3. While loop 
        while(start<=end):
            #1. Check the sum if limit is reached
            if(people[start]+people[end]<=limit):
                start+=1
                end-=1
            else:
                end-=1
            counter+=1
        
        return counter
        