# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


class Solution:
    

    def isValidSudoku(self, board):
        def three(ele,i,j,board):
            
            a = i - i%3
            b = j - j%3
            c=0
            for i in range(a,a+3):
                for j in range(b,b+3):
                    if ele==board[i][j]:
                        c+=1
            if c>1:
                        return 0
            return 1
        
        def col(ele,j,board):
            c=0
            for i in range(9):
                if board[i][j]==ele:
                    c=c+1
            if c>1:
                return 0
            return 1
            
        def row(ele,i,board):
            if board[i].count(ele)>1:
                return 0
            return 1
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                   if not(col(board[i][j],j,board)):
                       return 0
                   if not(row(board[i][j],i,board)):
                       return 0
                   if not(three(board[i][j],i,j,board)):
                       return 0
        return 1
        