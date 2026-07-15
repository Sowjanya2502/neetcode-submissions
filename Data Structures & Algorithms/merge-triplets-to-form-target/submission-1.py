class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        similar = set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            for i,value in enumerate(t):
                if value == target[i]:
                    similar.add(i)
        return len(similar)==3  
        