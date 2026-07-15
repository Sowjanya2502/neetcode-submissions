# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        l=0
        while l<left-1:
            prev=curr
            curr = curr.next
            l+=1
        nxt=None
        for i in range(right-left+1):
            tmp1 = curr.next
            curr.next = nxt
            nxt=curr
            curr = tmp1
        prev.next.next = curr
        prev.next = nxt
        return dummy.next
        


        

        

        

        