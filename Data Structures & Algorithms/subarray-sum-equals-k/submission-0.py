class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        presum = 0
        count = 0
        for num in nums:
            presum += num
            if presum == k:
                count += 1
            if presum-k in prefixsum:
                count += prefixsum[presum-k]
            prefixsum[presum] += 1
        return count

            
            