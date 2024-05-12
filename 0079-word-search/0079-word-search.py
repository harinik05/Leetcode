class Solution:
    # Backtrack function
    def backtrack(self, board, row, col, word):
        if len(word)==0:
            return True
        if row < 0 or col < 0 or row > len(board)-1 or col >len(board[0])-1 or self.visited[row][col] or board[row][col] != word[0]:
            return False
        self.visited[row][col] = True
        
        # right
        if self.backtrack(board,row,col+1,word[1:]):
            return True
        #down
        if self.backtrack(board, row+1,col,word[1:]):
            return True
        
        #left
        if self.backtrack(board,row, col-1,word[1:]):
            return True
        
        # up
        if self.backtrack(board, row-1,col, word[1:]):
            return True
        
        #no path is found
        self.visited[row][col] = False
        
        return False
        
    
    # Main exist function
    def exist(self, board: List[List[str]], word: str) -> bool:
        #1. Initialize the visited board
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        #2. loop thru all the elements
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.backtrack(board, row, col, word):
                        return True
        return False
                
                
        