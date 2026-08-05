# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum1 = root.val
        def maxsum(node):
            if not node:
                return 0
            leftsum = maxsum(node.left)
            rightsum = maxsum(node.right)
            self.maxsum1 = max(self.maxsum1, max(leftsum,0)+max(rightsum,0)+node.val)
            return node.val+max(max(leftsum,0),max(rightsum,0))
        maxsum(root)
        return self.maxsum1

