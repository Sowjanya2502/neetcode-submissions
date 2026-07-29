# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        remove = head
        length = head
        cnt =0
        itr =1
        remove1=ListNode()
        while length:
            cnt+=1
            length = length.next
        if n == cnt:
            first = head.next
            return first
        while itr < cnt-n:
            remove = remove.next
            itr+=1
        remove.next=remove.next.next
        return first
        
        