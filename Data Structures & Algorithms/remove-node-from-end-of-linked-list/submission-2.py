# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        node = head
        second = head.next
        length = 0
        count = 1
        while first:
            length+=1
            first = first.next
        if n == length:
            node = head.next
            return node
        first = head
        while count<length-n:
            count+=1
            first = first.next
        first.next = first.next.next
        return node
        





        

        