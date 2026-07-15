# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr =[]
        def bfs(root):
            if not root:
                return 0
            bfs(root.left)
            curr.append(root.val)
            bfs(root.right)

        bfs(root)
        return curr[k-1]
            

