# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res=[]
        while queue:
            NewNode = None
            qLen = len(queue)
            for i in range(qLen):
                tree = queue.popleft()
                if tree:
                    NewNode = tree
                    queue.append(tree.left)
                    queue.append(tree.right)
            if NewNode:
                res.append(NewNode.val)
        return res