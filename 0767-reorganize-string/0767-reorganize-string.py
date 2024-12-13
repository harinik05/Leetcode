class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #1. Put string into the hashmap
        hashmap = Counter(s)
        
        #2. Put into max heap
        maxHeap = []
        for key, value in hashmap.items():
            maxHeap.append((-1*value, key))
        heapq.heapify(maxHeap)
        output = ""
        #3. While max heap 
        while maxHeap:
            # Pop the element 
            frequency, alphabet = heapq.heappop(maxHeap)
            
            # Check if this equals the previous element 
            if output == "" or alphabet != output[-1]:
                frequency+=1
                output+=alphabet
                if frequency!=0:
                    heapq.heappush(maxHeap, (frequency, alphabet))
            # now this means they are equal to each other
            else:
                if not maxHeap:
                    return "" # failing case
                
                # pop another element 
                second_frequency, second_alphabet = heapq.heappop(maxHeap)
                second_frequency+=1
                output+=second_alphabet
                if second_frequency!=0:
                    heapq.heappush(maxHeap, (second_frequency, second_alphabet))
                heapq.heappush(maxHeap, (frequency, alphabet))
        
        return output
                
        
                
                
        