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
                value = board[r][c]

                # Check if the value is a digit
                if value.isdigit():
                    # Check rows
                    if value in self.rows[r]:
                        return False
                    self.rows[r].add(value)

                    # Check columns
                    if value in self.columns[c]:
                        return False
                    self.columns[c].add(value)

                    # Check boxes
                    boxIndex = (r // 3) * 3 + (c // 3)
                    if value in self.boxes[boxIndex]:
                        return False
                    self.boxes[boxIndex].add(value)

        return True
