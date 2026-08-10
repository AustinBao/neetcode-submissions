class Solution:    
    def check_row(board):
        for row in board:
            dots = row.count(".")
            if len(row) - dots + 1 != len(set(row)):
                return False
        return True


    def check_col(board):
        for i in range(9):
            col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i], board[6][i], board[7][i],
                board[8][i]]
            dots = col.count(".")
            if len(col) - dots + 1 != len(set(col)):
                return False
        return True


    def check_three_by_three(board):
        for row in range(1, 9, 3):
            for col in range(1, 9, 3):
                threebythree = [board[row - 1][col - 1], board[row - 1][col], board[row - 1][col + 1],
                                board[row][col - 1], board[row][col], board[row][col + 1],
                                board[row + 1][col - 1], board[row + 1][col], board[row + 1][col + 1]]
                dots = threebythree.count(".")
                if len(threebythree) - dots + 1 != len(set(threebythree)):
                    return False
                col += 3
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = True
        check_col = True
        check_three_by_three = True


        for row in board:
            dots = row.count(".")
            if len(row) - dots + 1 != len(set(row)):
                check_row = False

        for i in range(9):
            col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i], board[6][i], board[7][i],
                board[8][i]]
            dots = col.count(".")
            if len(col) - dots + 1 != len(set(col)):
                check_col = False

        for row in range(1, 9, 3):
            for col in range(1, 9, 3):
                threebythree = [board[row - 1][col - 1], board[row - 1][col], board[row - 1][col + 1],
                                board[row][col - 1], board[row][col], board[row][col + 1],
                                board[row + 1][col - 1], board[row + 1][col], board[row + 1][col + 1]]
                dots = threebythree.count(".")
                if len(threebythree) - dots + 1 != len(set(threebythree)):
                    check_three_by_three = False
                col += 3


        return check_col and check_row and check_three_by_three


    
    

