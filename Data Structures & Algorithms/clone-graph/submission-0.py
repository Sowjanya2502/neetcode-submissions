"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        return self.dfs(node,{})
    
    def dfs(self,node, cmap):
        if node in cmap:
            return cmap[node]
        cnode = Node(node.val)
        cmap[node] = cnode
        for neighbour in node.neighbors:
            c_neighbour = self.dfs(neighbour, cmap)
            cnode.neighbors.append(c_neighbour)
        return cnode
        