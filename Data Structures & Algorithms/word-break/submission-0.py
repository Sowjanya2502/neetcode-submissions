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
        dp = [False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]

         
        
        
        