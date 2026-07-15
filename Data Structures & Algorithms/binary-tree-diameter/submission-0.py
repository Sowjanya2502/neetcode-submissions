# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)
        diameter = left_height+right_height
        return max(diameter, max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.depth(root.left),self.depth(root.right))   

        