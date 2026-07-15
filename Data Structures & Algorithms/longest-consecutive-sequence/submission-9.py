class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        count = 1
        max_count =0
        for num in res:
            if num - 1 not in res:
                count = 1
                while num +1 in res:
                    count += 1
                    num += 1
                max_count = max(count, max_count)
        return max_count
            
            
