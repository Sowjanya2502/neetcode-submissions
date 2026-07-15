class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums)):
            if nums[i] < 0:
                nums[i]=0
        for num in nums:
            if 1<=abs(num)<=len(nums):
                if nums[abs(num)-1]>0:
                    nums[abs(num)-1] = -1*abs(nums[abs(num)-1])
                elif nums[abs(num)-1] == 0:
                    nums[abs(num)-1] = -(len(nums)+1)
        for i in range(1,len(nums)+1):
            if nums[i-1]<0:
                count+=1
            else:
                return i
        return count+1

            



            

        
