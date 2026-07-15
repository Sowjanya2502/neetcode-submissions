class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1,l2=0,0
        while l1<m and l2<n:
            if nums1[l1]>nums2[l2]:
                prev = nums1[l1]
                nums1[l1]=nums2[l2]
                nums1[m]=prev
                l1+=1
                l2+=1
                m+=1
            else:
                l1+=1
        if l2<n:
            for i in range(l1, len(nums1)):
                nums1[i]=nums2[l2]
                l2+=1
        nums1.sort()


            
        
        