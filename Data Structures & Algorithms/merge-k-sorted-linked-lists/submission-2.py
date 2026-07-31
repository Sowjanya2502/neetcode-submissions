# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Finallist=[]
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergedlists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if len(lists)>i+1 else None
                mergedlists.append(self.mergelist(l1,l2))
            lists = mergedlists
        return lists[0]
    def mergelist(self, l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
        head = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1=l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return node.next
        

        