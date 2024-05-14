class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #1. Initialize the dp array
        dp = [[0 for _ in range(len(obstacleGrid[0]))]for _ in range(len(obstacleGrid))]
        #First row must be all ones
        # First row must be all ones until obstacle
        for c in range(len(obstacleGrid[0])):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = 1
            else:
                break
                
        # First column must be all ones until obstacle
        for r in range(len(obstacleGrid)):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = 1
            else:
                break
        
        #2. for loop
        for row in range(1,len(obstacleGrid)):
            for col in range(1,len(obstacleGrid[0])):
                #a. Determine the unique paths
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
                    
                #b. else
                else:
                    dp[row][col]=0
        
        return dp[len(dp)-1][len(dp[0])-1]