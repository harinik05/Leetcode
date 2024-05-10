from typing import List

class Solution:
    # Constructor
    def __init__(self):
        self.n = 9
        self.rows = [set() for _ in range(self.n)]
        self.columns = [set() for _ in range(self.n)]
        self.boxes = [set() for _ in range(self.n)]
    
    # Valid sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(self.n):
            for c in range(self.n):
                # Value of the board
                value = board[r][c]
                if value == ".":
                    continue
                
                # Values in rows
                if value in self.rows[r]:
                    return False
                self.rows[r].add(value)

                # Values in columns
                if value in self.columns[c]:
                    return False
                self.columns[c].add(value)

                # Values in boxes
                boxIndex = (r // 3) * 3 + (c // 3)
                if value in self.boxes[boxIndex]:
                    return False
                self.boxes[boxIndex].add(value)
        
        return True
