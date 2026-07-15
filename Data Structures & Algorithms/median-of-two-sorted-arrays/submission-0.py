class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        curr=0
        prev=0
        p1=0
        p2=0
        for i in range((len(nums1)+len(nums2))//2+1):
            prev = curr
            if p1<len(nums1) and p2<len(nums2):
                if nums1[p1]>nums2[p2]:
                    curr=nums2[p2]
                    p2+=1
                else:
                    curr=nums1[p1]
                    p1+=1
            elif p1<len(nums1):
                curr=nums1[p1]
                p1+=1
            else:
                curr=nums2[p2]
                p2+=1

        if (len(nums1)+len(nums2))%2==1 :
            return curr
        else:
            return (curr+prev)/2