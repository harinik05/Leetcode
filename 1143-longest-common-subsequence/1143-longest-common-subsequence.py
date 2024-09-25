class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # 1.) Initialize the DP array 
        ROWS = len(text1)
        COLS = len(text2)
        DP = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        
        #2.) Loop through everything 
        for r in range(ROWS,-1,-1):
            for c in range(COLS, -1, -1):
                #a. Check if something is extending beyond the index, keep in index 
                if r == ROWS or c == COLS:
                    DP[r][c] = 0
                
                #b. Check if the index where both characters are matching 
                elif text1[r] == text2[c]:
                    DP[r][c] = 1+DP[r+1][c+1]
                
                #c. Check if the characters were not matching 
                elif text1[r] != text2[c]:
                    DP[r][c] = max(DP[r+1][c], DP[r][c+1])
        
        return DP[0][0]
        
        