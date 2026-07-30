# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        borrow=0
        result = node
        while l1 or l2 or borrow:
            a1=l1.val if l1 else 0
            a2=l2.val if l2 else 0
            add = a1+a2+borrow
            node.next = ListNode(add%10)
            borrow = add//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            node=node.next
        return result.next



        