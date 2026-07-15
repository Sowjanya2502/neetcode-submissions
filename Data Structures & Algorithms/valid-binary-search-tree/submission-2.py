# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], val_BST: List[int])-> List[int]:
        if root:
            self.inorder(root.left, val_BST)
            val_BST.append(root.val)
            self.inorder(root.right, val_BST) 
        return val_BST

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_val = self.inorder(root, [])
        return inorder_val == sorted(list(set(inorder_val)))