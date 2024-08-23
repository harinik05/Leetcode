class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        #1. Initialize the DP array 
      
        
        #2. Initialize with a bunch of 0s for text1.length and text2.length 
        first = len(text1)
        second = len(text2)
        
        #3. initialize everything as 0 
       
        dp = [[0 for i in range(second+1)] for j in range(first+1)]
        
        #4. for loop for the actual dp stuff 
        for i in range(first-1, -1, -1):
            for j in range(second-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] +1 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        