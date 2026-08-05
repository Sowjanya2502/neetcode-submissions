# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def array(node)->List[int]:
            if not node:
                return
            array(node.left)
            res.append(node.val)
            array(node.right)
        array(root)
        for i in range(len(res)):
            if i==k-1:
                return res[k-1]