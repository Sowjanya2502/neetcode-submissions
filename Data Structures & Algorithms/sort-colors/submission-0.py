class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lis = quickSort(nums)
        for i in range(len(nums)):
            nums[i]=lis[i]
def quickSort(nums):
    if len(nums)<=1:
        return nums
    pivot = nums[-1]
    left = []
    right=[]
    for i in range(0,len(nums)-1):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quickSort(left)+[pivot]+quickSort(right)
        