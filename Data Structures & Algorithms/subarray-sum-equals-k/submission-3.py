class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsummap ={0:1}
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum+=num
            if curr_sum - k in prefixsummap:
                res+=prefixsummap[curr_sum-k]
            freq = prefixsummap.get(curr_sum,0)
            prefixsummap[curr_sum]= freq+1
        return res





        