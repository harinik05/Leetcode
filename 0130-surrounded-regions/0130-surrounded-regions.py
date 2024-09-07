# Lets first do a DFS solution
from collections import deque
class Solution(object):
    def __init__(self):
        self.visited = []
        self.ROWS = 0
        self.COLS = 0
        self.directions = [(-1,0),(0,1),(1,0),(0,-1)]
        self.queue = deque()
    
    #1. Actual solve
    def solve(self, board):
        #1. Complete initialization of variables 
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        #2. Create lists for the borders
        borderLists = [(r,c) for r in range(self.ROWS) for c in (0, self.COLS-1)] + [(r,c) for r in (0,self.ROWS-1) for c in range(self.COLS)]
        
        #3. Initialize the visited set 
        self.visited = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        
        #4. Go through all the borders list and then do the bfs
        for row, col in borderLists:
            if board[row][col] == "O" and self.visited[row][col] == 0:
                self.bfs(board, row, col)
        
        #5. Go through the entire thing
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "*":
                    board[r][c]="O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                    
                    
    def solveDFS(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #1. Initialize the variables 
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        #2. Create lists for the borders 
        borderLists = [(r,c) for r in range(self.ROWS) for c in(0, self.COLS-1)] + [(r,c) for r in (0,self.ROWS-1) for c in range(self.COLS)]
        
        #3. Initialize the self.visited set 
        self.visited = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        
        #4. Go through the borders list and then do dfs whenever appropriate 
        for row, col in borderLists:
            #a. If its not in visited and its 0 then do dfs
            if board[row][col] == 'O' and self.visited[row][col] == 0:
                self.dfs(board, row, col)
        
        #5. go through the entire thign now 
         #4. Go through the borders list and then do dfs whenever appropriate 
        for row in range(self.ROWS):
            for col in range(self.COLS):
            #a. If its not in visited and its 0 then do dfs
                if board[row][col] == "*":
                    board[row][col] = 'O'
                elif board[row][col] == "O":
                    board[row][col] = "X"

    
    def bfs(self, board, row, col):
        #1. Put the first element in the queue
        self.queue.append((row, col))
        self.visited[row][col] = 1
        board[row][col] = "*"
        
        #2. While queue 
        while self.queue:
            # Pop left
            r,c = self.queue.popleft()
            
            # go through the neighbors
            for direction in self.directions:
                ri, ci = direction
                rowF = r+ ri
                colF = c + ci
                
                # check the conditions now 
                if 0<=rowF<self.ROWS and 0<=colF<self.COLS and self.visited[rowF][colF] == 0 and board[rowF][colF]== "O":
                    board[rowF][colF] = "*"
                    self.visited[rowF][colF] = 1
                    self.queue.append((rowF, colF))
                    
                
                
                
        
        
        
    def dfs(self, board, row, col):

        #1. Check the conditions 
        if row<0 or row>=self.ROWS or col<0 or col>=self.COLS:
            return
        if self.visited[row][col] ==1:
            return
        if board[row][col] !='O':
            return
            
    
        #2. Process the current cell 
        self.visited[row][col] = 1
        board[row][col] = "*"
            
        #3. DFS function (do it recursively)
        self.dfs(board, row+1, col)
        self.dfs(board, row-1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row, col-1)
    
        