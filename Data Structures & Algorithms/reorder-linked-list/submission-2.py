# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        actual = head
        first = head
        second = head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        sec = first.next
        prev = first.next = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        sec = prev
        while sec:
            tmp1,tmp2=actual.next, sec.next
            actual.next = sec
            sec.next = tmp1
            actual, sec = tmp1, tmp2
        
            

            

        
