class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        result=[]
        for s in strs:
            map1["".join(sorted(s))].append(s)
        for key, value in map1.items():
            result.append(map1[key])
        return result
        