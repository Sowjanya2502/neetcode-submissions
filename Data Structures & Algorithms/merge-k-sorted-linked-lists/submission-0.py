# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists)>1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if len(lists)>(i+1) else None
                mergeLists.append(self.mergeList(l1,l2))
            lists = mergeLists
        return lists[0]

    def mergeList(self, l1, l2):
        head = node =ListNode()
        while l1 and l2:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return node.next