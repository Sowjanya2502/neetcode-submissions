class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        presum = 0
        count = 0
        prefixsum[0]=1
        for num in nums:
            presum += num
            if presum-k in prefixsum:
                count += prefixsum[presum-k]
            prefixsum[presum]+=1
        return count
