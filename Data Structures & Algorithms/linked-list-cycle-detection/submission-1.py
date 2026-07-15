# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail,right = head, head
        while right and right.next:
            tail = tail.next
            right = right.next.next
            if tail == right:
                return True
        return False