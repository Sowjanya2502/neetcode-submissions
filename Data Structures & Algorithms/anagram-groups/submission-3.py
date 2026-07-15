class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_result = defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            map_result[st].append(s)
        return [list(s) for s in map_result.values()]
            