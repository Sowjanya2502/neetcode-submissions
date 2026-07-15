class TrieNode:
    def __init__(self):
        self.children={}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c]=TrieNode()
                node = node.children[c]
            node.word =word
        res=[]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    self.dfs(board, r, c, root.children[board[r][c]],res)
        return res

    def dfs(self,board: List[List[str]], r:int, c:int, node:TrieNode, res:List[str]) -> None:
        if node.word:
            res.append(node.word)
            node.word = None
        temp = board[r][c]
        board[r][c]='#'
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for di in dirs:
            next_r, next_c = r+di[0], c+di[1]
            if (self.iswithinbounds(board, next_r,next_c) and board[next_r][next_c] in node.children):
                self.dfs(board, next_r, next_c, node.children[board[next_r][next_c]], res)
        board[r][c]=temp
    
    def iswithinbounds(self, board: List[List[str]], r: int, c: int):
        return 0<=r<len(board) and 0<=c<len(board[0])
            
        