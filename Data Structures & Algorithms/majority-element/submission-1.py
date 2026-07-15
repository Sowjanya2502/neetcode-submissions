class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp1=defaultdict(int)
        for num in nums:
            mp1[num]+=1
            if mp1[num]>math.floor(len(nums)/2):
                return num
        
        