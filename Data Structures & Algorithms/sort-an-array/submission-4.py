class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return mergeSort(nums)
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left1=mergeSort(nums[0:mid])
    right1=mergeSort(nums[mid:len(nums)])
    return merge(left1, right1)

def merge(left, right):
    store = []
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            store.append(left[l])
            l+=1
        else:
            store.append(right[r])
            r+=1
    store = store+left[l:]
    store = store+(right[r:])
    return store




