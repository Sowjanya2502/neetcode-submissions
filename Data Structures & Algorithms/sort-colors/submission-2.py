class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        index = 0
        for i in range(len(nums)):
            count[nums[i]]+=1
        for i in range(3):
            while count[i]>0:
                nums[index]=i
                count[i]-=1
                index+=1