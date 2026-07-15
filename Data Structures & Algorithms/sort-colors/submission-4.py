class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        index = 0
        for i in range(3):
            for j in range(index, index + count[i]):
                nums[j] = i
                index += 1