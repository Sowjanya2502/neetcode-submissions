# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False
        first = head.next
        second = head.next.next
        while second:
            if first.next == second.next:
                return True
            first = first.next
            second = second.next.next
        return False