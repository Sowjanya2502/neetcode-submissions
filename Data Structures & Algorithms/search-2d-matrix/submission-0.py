class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.bs(target,matrix[i][:len(matrix[0])]):
                return True
        return False
        


    def bs(self,target,arr):
        left,right = 0,len(arr)-1
        while left<right:
            mid = (left+right)//2
            if target == arr[mid]:
                return True
            if target<arr[mid]:
                right = mid-1
            else:
                left = mid+1

        return True if arr and arr[left]==target else False
        