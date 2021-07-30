class Solution:
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkrow(board: List[List[str]], row) -> bool:
            x = [0]*10
            for j in range(9):
                if ( board[row][j] <= '9' and board[row][j] >=  '0'):
                    x[ int(board[row][j]) ] += 1
                    if ( x[ int(board[row][j])  ] > 1):
                        return(False)    
            return(True)
        
        def checkcol(board: List[List[str]], col) -> bool:
            x = [0]*10
            for j in range(9):
                if ( board[j][col] <= '9' and board[j][col] >=  '0'):
                    x[ int(board[j][col]) ] += 1
                    if ( x[ int(board[j][col])  ] > 1):
                        return(False)    
            return(True)
        
        def checkrec(board: List[List[str]], row, col) -> bool:
            x = [0]*10
            for j in range(row, row + 3):
                for v in range(col, col + 3):
                    if ( board[j][v] <= '9' and board[j][v] >=  '0'):
                        x[ int(board[j][v]) ] += 1
                        if ( x[ int(board[j][v])  ] > 1):
                            return(False)    
            return(True)
    
        for i in range(9):
            if (checkrow(board, i) == False):
                return(False)
            if (checkcol(board, i) == False):
                return(False)
        for i in range(0,9,3):
            for j in range(0,9,3):
                if (checkrec(board, i, j) == False):
                    return(False)
            
        return(True)
