class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map1=defaultdict(list)
        for t in trust:
            if t[0] in map1.keys():
                return -1
            map1[t[1]].append(t[0])
        for key,value in map1.items():
            if len(value)==n-1:
                return key
        return -1
        