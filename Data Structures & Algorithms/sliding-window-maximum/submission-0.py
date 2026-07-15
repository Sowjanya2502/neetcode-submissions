class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        max_element = 0
        for i in range(0, len(nums)-k+1):
            l = i
            max_element = nums[l]
            while l<i+k:
                max_element = max(max_element, nums[l])
                l+=1
            res.append(max_element)
        return res