# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        g_prev = dummy
        while True:
            kth = self.kthNode(g_prev,k)
            if not kth:
                break
            g_next = kth.next
            prev, curr = kth.next, g_prev.next
            while curr!=g_next:
                temp1 = curr.next
                curr.next = prev
                prev = curr
                curr = temp1
            temp = g_prev.next
            g_prev.next = kth
            g_prev = temp
        return dummy.next    

    def kthNode(self,cur,k):
        while cur and k>0:
            cur = cur.next
            k-=1
        return cur
                