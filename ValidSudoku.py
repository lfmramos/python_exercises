"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to store the presence of digits in rows, columns, and boxes
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        # Iterate over each cell in the board
        for i in range(9):
            for j in range(9):
                # Check if the cell is filled
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3
                    
                    # Check if the digit is already present in the current row, column, or box
                    if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                        return False
                    else:
                        rows[i][num] = 1
                        columns[j][num] = 1
                        boxes[box_index][num] = 1
        
        return True