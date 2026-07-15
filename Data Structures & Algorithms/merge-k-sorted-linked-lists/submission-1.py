# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if len(lists)>(i+1) else None
                mergeLists.append(self.mergeList(l1,l2))
            lists = mergeLists
        return lists[0]
    def mergeList(self,list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                head.next = list1
                list1=list1.next
            else:
                head.next = list2
                list2=list2.next
            head = head.next
        head.next = list1 if list1 else list2
        return node.next
            


