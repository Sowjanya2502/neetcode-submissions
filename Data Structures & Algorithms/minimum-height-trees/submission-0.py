class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        map1 = defaultdict(list)
        for u,v in edges:
            map1[u].append(v)
            map1[v].append(u)
        minHeight = n
        res = []
        def dfs(node, root):
            height =0
            for ni in map1[node]:
                if ni == root:
                    continue
                height = max(height, 1+dfs(ni,node))
            return height
        for i in range(n):
            curr_height = dfs(i,-1)
            if curr_height == minHeight:
                res.append(i)
            if curr_height<minHeight:
                res = [i]
                minHeight = curr_height
        return res
