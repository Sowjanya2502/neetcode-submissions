class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            col = set()
            row=set()
            sq=set()
            for j in range(0, len(board)):
                if board[i][j].isdigit():
                    if int(board[i][j]) in col:
                        return False
                    col.add(int(board[i][j]))
                if board[j][i].isdigit():
                    if int(board[j][i]) in row:
                        return False
                    row.add(int(board[j][i]))
                row_indx = 3*(i//3)
                col_indx = 3*(i%3)
                r = row_indx+(j//3)
                c = col_indx+(j%3)
                if board[r][c].isdigit():
                    if int(board[r][c]) in sq:
                        return False
                    sq.add(int(board[r][c]))
        return True       
