class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        order = defaultdict(list)
        for t in trust:
            if t[0] in order.keys():
                return -1
            order[t[1]].append(t[0])
        for k,v in order.items():
            if len(order[k])==n-1:
                return k
        return -1