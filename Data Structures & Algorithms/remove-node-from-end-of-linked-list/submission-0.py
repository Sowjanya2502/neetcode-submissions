# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while(temp != None):
            count += 1
            temp = temp.next
        nodeFromBeginning = count - n + 1
        prev = None
        temp = head
        for i in range(1, nodeFromBeginning):
            prev = temp
            temp = temp.next
        if(prev == None):
            head = head.next
            return head
        else:
            prev.next = prev.next.next
            return head