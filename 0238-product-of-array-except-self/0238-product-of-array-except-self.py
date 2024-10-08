class Solution:
    
    def productExceptSelf(self, nums: List[int])-> List[int]:
        #1. Initialize the data structures
        answerArr = [1] * len(nums)
        
        #2. Fill out the prefixes first 
        for i, number in enumerate(nums):
            if i-1<0:
                answerArr[i] = 1
            else:
                answerArr[i] = answerArr[i-1] * nums[i-1]
        
        
        #3. Fill out the suffixes now 
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            if i+1<len(nums):
                suffix*=nums[i+1]
                answerArr[i]*=suffix
        
        return answerArr
    
    # Solution that contains O(n) space complexity
    def productExceptSelf_WITHSPACE(self, nums: List[int]) -> List[int]:
        
        #1. Define my necessary data structures
        prefixArr = [1]*len(nums)
        suffixArr = [1] * len(nums)
        answerArr= [1] * len(nums)
        
        #2. Fill out the prefix array
        for i,number in enumerate(nums):
            if i-1<0:
                prefixArr[i] = 1
            else:
                prefixArr[i] = prefixArr[i-1] * nums[i-1]
        
        #3. Fill out the suffix array 
        for i in range(len(nums)-1,-1,-1):
            if i+1>=len(nums):
                suffixArr[i] = 1
            else:
                suffixArr[i] = suffixArr[i+1] * nums[i+1]
        
        #4. Fill out the answer arr
        for k in range(len(answerArr)):
            answerArr[k] = prefixArr[k] * suffixArr[k]
        
        
        #5. return the answer arr
        return answerArr
            
            
            
        