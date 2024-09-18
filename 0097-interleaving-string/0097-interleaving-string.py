class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        #1. Initialize the DP array 
        dp = [[False for c in range(len(s2)+1)] for r in range(len(s1)+1)]
        
        #2. Check if the lengths have some problem 
        COLS = len(s2)
        ROWS = len(s1)
        
        if COLS + ROWS!=len(s3):
            return False
        
        dp[0][0] = True
        #3. For loop 
        for r in range(ROWS+1):
            for c in range(COLS+1):
                #a. In the first row
                if(r == 0 and c>0):
                    dp[0][c] = dp[0][c-1] if (s2[c-1] == s3[r+c-1]) else False
               
                
                #2. In the first col
                if(r>0 and c==0):
                    dp[r][0] = dp[r-1][0] if (s1[r-1] == s3[r+c-1]) else False
               
                
                #3. So lets say that its other stuff
                if(r>0 and c>0):
                    dp[r][c] = (dp[r][c-1] if (s2[c-1] == s3[r+c-1]) else False) or (dp[r-1][c] if (s1[r-1] == s3[r+c-1]) else False) 
              
        return dp[ROWS][COLS]
        
        
                    
                    
                    
                
                
                
        