class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def capture(r,c):
            dirs = [(-1,0),(0,1),(0,-1),(1,0)]
            if (r<0 or c<0 or r== len(board) or c==len(board[0]) or board[r][c]!='O'):
                return
            board[r][c]='T'
            for d in dirs:
                next_r,next_c = r+d[0],c+d[1]
                capture(next_r, next_c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j]=='O' and (i in [0, len(board)-1] or j in [0,len(board[0])-1])):
                    capture(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
        
            


        
        