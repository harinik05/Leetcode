class Solution(object):
    def __init__(self):
        self.MEMO = []
        self.ROWS = 0
        self.COLS = 0
        self.text1 = ""
        self.text2 = ""
    
    def memoizationFunction(self, i, j):
        #1.) Check if you're ending up in the rows 
        if i == self.ROWS or j == self.COLS:
            return 0
        #2. Check if the values are equal 
        elif (self.MEMO[i][j] == "*") and (self.text1[i] == self.text2[j]):
            self.MEMO[i][j] = self.memoizationFunction(i+1,j+1) +1
        
        #3. Check if the values aren't matching 
        elif(self.MEMO[i][j] == "*") and (self.text1 != self.text2[j]):
            self.MEMO[i][j] = max(self.memoizationFunction(i+1, j), self.memoizationFunction(i,j+1))
        
        #4. return the answer
        return self.MEMO[i][j]
        
    def longestCommonSubsequence(self, text1, text2):
        #1.) Initialize the DP array 
        self.text1 = text1
        self.text2 = text2
        self.ROWS = len(text1)
        self.COLS = len(text2)
        self.MEMO = [["*" for _ in range(self.COLS+1)] for _ in range(self.ROWS+1)]
        
        #2.) return the answer 
        return self.memoizationFunction(0,0)
    
    #Bottom Up Approach
    def longestCommonSubsequence_DP(self, text1, text2):
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
        
        