# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        node=root
        node.left = self.removeLeafNodes(root.left, target)
        node.right = self.removeLeafNodes(root.right, target)
        if not node.left and not node.right and node.val == target:
            node = None
        return node
