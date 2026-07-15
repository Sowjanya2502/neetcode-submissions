# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res=[]
        while queue:
            res1=[]
            for i in range(len(queue)):
                tree = queue.popleft()
                if tree:
                    res1.append(tree.val)
                    queue.append(tree.left)
                    queue.append(tree.right)
            if res1:
                res.append(res1)
        return res

            
