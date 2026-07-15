class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = set()
        for num in nums:
            count[num]+=1
            if count[num] > len(nums)//3:
                res.add(num)
                count[num]=0
        return list(res)