# class TrieNode:
#     def __init__(self):
#         self.children={}
#         self.word = None
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # root = TrieNode
        # for word in wordDict:
        #     node = root
        #     for c in word:
        #         if c is not in node.children:
        #             node.children[c]=TrieNode()
        #         node = node.children[c]
        #     node.word = word
        # node1=root
        # for new in s:
        #     if new in node1.children:
        #         node1=node1.children
        #         if node1.word:
        #             node1 = root    
        #     else:
        #         return False
        memo={len(s):True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if ((s[i:i+len(w)]==w) and (i+len(w)<=len(s))):
                    if dfs(i+len(w)):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        return dfs(0)
                    
                


            
            

         
        
        
        